from pathlib import Path
import json,shutil,hashlib
import numpy as np,rasterio
from rasterio.warp import reproject,Resampling
ROOT=Path('data/raster_2024_2026')
summary=[]
for year in [2024,2025,2026]:
 d=ROOT/str(year);cal=json.loads((d/'sentinel_calibration.json').read_text());print(year,cal['quantification_value'],cal['offset_dn'])
 with rasterio.open(d/'s2_B04.tif') as src:red=src.read(1,masked=True).astype('float32').filled(np.nan);p=src.profile.copy()
 with rasterio.open(d/'s2_B08.tif') as src:nir=src.read(1,masked=True).astype('float32').filled(np.nan);assert src.transform==p['transform']
 scl=np.zeros(red.shape,dtype='uint8')
 with rasterio.open(d/'s2_SCL.tif') as src:reproject(source=rasterio.band(src,1),destination=scl,src_transform=src.transform,src_crs=src.crs,dst_transform=p['transform'],dst_crs=p['crs'],src_nodata=0,dst_nodata=0,resampling=Resampling.nearest)
 red=(red+cal['offset_dn']['B04'])/cal['quantification_value'];nir=(nir+cal['offset_dn']['B08'])/cal['quantification_value']
 valid=np.isin(scl,[4,5,6])&np.isfinite(red)&np.isfinite(nir)&((red+nir)>0)
 ndvi=np.full(red.shape,np.nan,dtype='float32');np.divide(nir-red,nir+red,out=ndvi,where=valid)
 p.update(count=1,dtype='float32',nodata=-9999,compress='deflate')
 with rasterio.open(d/'ndvi.tif','w',**p) as dst:dst.write(np.where(np.isfinite(ndvi),ndvi,-9999).astype('float32'),1);dst.set_band_description(1,f'NDVI {year}; original Sentinel XML offsets applied; SCL 4,5,6')
 item=json.loads((d/'landsat_item.json').read_text())
 with rasterio.open(d/'landsat_lwir11.tif') as src:dn=src.read(1);p=src.profile.copy()
 with rasterio.open(d/'landsat_qa_pixel.tif') as src:qa=src.read(1);assert src.transform==p['transform']
 valid=((qa&63)==0)&(dn!=0);meta=item['assets']['lwir11']['raster:bands'][0]
 lst=dn.astype('float32')*meta['scale']+meta['offset']-273.15;lst[~valid]=np.nan
 p.update(count=1,dtype='float32',nodata=-9999,compress='deflate')
 with rasterio.open(d/'lst_celsius.tif','w',**p) as dst:dst.write(np.where(np.isfinite(lst),lst,-9999).astype('float32'),1);dst.set_band_description(1,f'Landsat LST Celsius {year}; QA_PIXEL bits 0-5 excluded')
 summary.append({'year':year,'ndvi_retained':float(np.isfinite(ndvi).mean()),'ndvi_percentiles':np.nanpercentile(ndvi,[5,50,95]).tolist(),'lst_retained':float(np.isfinite(lst).mean()),'lst_C_percentiles':np.nanpercentile(lst,[5,50,95]).tolist()})
 sources=json.loads((d/'raster_sources.json').read_text())
 for name,recipe in [('ndvi.tif','(calibrated B08-B04)/(B08+B04); SCL nearest neighbour, retain classes 4,5,6; finite values and positive denominator'),('lst_celsius.tif','ST DN * metadata scale + offset - 273.15; exclude QA_PIXEL bits 0-5 and ST DN=0')]:
  sources[name]={'operation':'Derived teaching raster','recipe':recipe,'sha256':hashlib.sha256((d/name).read_bytes()).hexdigest()}
 (d/'raster_sources.json').write_text(json.dumps(sources,indent=2))
(ROOT/'derived_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))


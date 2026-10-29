05 — Distance, networks and accessibility
Extract this ZIP beside the notebook before running in Colab. The data/ directory matches notebook 04.
All variables are defined in this notebook. Run cells in order.
The main exercise loads the documented walking graph. The optional appendix includes its full PBF preparation code.
Original OSM PBF: https://osmit-estratti.wmcloud.org/output/pbf/comuni/022205_Trento.osm.pbf
APSS: https://servizi.apss.tn.it/opendata/FARM001.csv
OSM attribution: © OpenStreetMap contributors; ODbL, https://www.openstreetmap.org/copyright
APSS catalogue: https://dati.trentino.it/it/dataset/farmacie-pat
The PBF and metadata remain readable source material; graph preparation choices and limitations are explicit.
Validated locally: 18 main code cells plus the disabled optional preparation cell, excluding package installation. The network was also prepared from the original PBF during validation. Not tested in a signed-in Colab account.

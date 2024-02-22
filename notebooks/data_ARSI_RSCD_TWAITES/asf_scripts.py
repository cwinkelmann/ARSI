import asf_search as asf
import pandas as pd

search_results = asf.geo_search(
        platform=asf.PLATFORM.SENTINEL1,
        intersectsWith='POINT(-117.599330 35.769500)',
        start='2019-06-10',
        end='2019-07-21',
        processingLevel=asf.PRODUCT_TYPE.SLC,
        beamMode=asf.BEAMMODE.IW,
        flightDirection=asf.FLIGHT_DIRECTION.ASCENDING,
    )
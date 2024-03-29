# Overview

Basic python3 script that can load data from `dump1090-mutability` or `dump1090-fa` JSON files into a dictionary, which can then be used for any purpose.

> Details for flights where flight information is not yet available are skipped.

By default, the script prints the details into a pretty tabular form.

Use `-h` or `--help` to see the available options.

```shell
$ python3 flightStats.py -h
usage: flightStats.py [-h] [-v] (--dump1090-fa | --dump1090-mutability) (--latest | --history) [--csv]

dump1090 Flight Stats

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --dump1090-fa         Read flight stats from dump1090-fa JSON files
  --dump1090-mutability
                        Read flight stats from dump1090-mutability JSON files
  --latest              Get latest flight stats (from aircraft.json)
  --history             Get historical flight stats (from history_n.json)
  --csv                 Dump data into a CSV file: flights_<RFC3339-timestamp>.csv
```

## Usage

Example showing data from `dump1090-fa` file `aircraft.json`

```shell

$ python3 flightStats.py --dump1090-fa --latest
2024-03-04 19:31:19,907 - INFO - ---------- START ----------
2024-03-04 19:31:19,907 - INFO - Set to load flight stats from dump1090-fa
2024-03-04 19:31:19,907 - INFO - Set to load latest flight stats
2024-03-04 19:31:19,907 - INFO - Trying to load data from /var/run/dump1090-fa/aircraft.json
2024-03-04 19:31:19,907 - INFO - Data loaded successfully from file!
2024-03-04 19:31:19,907 - INFO - Parsing aircraft information
2024-03-04 19:31:19,907 - INFO - Skipping dataset [ICAO: 800521 ] due to missing flight information!
2024-03-04 19:31:19,907 - INFO - Skipping dataset [ICAO: 8014e5 ] due to missing flight information!
2024-03-04 19:31:19,907 - INFO - Skipping dataset [ICAO: 801465 ] due to missing flight information!
+--------+----------+------------+------------+-------+-------+-------+--------+---------+--------------+--------+---------------+-------------+-------------+----------+------------+-----------+--------------------+---------+---------+-------+------+------------+-----------+---------+---------+-------+------------+--------+--------+------------+--------+--------+-------------+------------+-------+-------+
| hex    | flight   |   alt_baro |   alt_geom |    gs |   ias |   tas |   mach |   track |   track_rate |   roll |   mag_heading |   baro_rate |   geom_rate |   squawk | category   |   nav_qnh |   nav_altitude_mcp |     lat |     lon |   nic |   rc |   seen_pos |   version |   nac_p |   nac_v |   sil | sil_type   | mlat   | tisb   |   messages |   seen |   rssi | emergency   |   nic_baro |   gva |   sda |
+========+==========+============+============+=======+=======+=======+========+=========+==============+========+===============+=============+=============+==========+============+===========+====================+=========+=========+=======+======+============+===========+=========+=========+=======+============+========+========+============+========+========+=============+============+=======+=======+
| 80138c | IAD990   |       8900 |       9500 | 213.8 |   180 |   212 |  0.32  |   199.1 |        -0.38 |   -4.4 |         199.7 |       -1120 |       -1152 |     2643 | A0         |    1010   |               6000 | 13.3705 | 77.4376 |     8 |  186 |       35.2 |         0 |       8 |       0 |     2 | unknown    | []     | []     |        154 |    6.4 |  -22.9 |             |            |       |       |
+--------+----------+------------+------------+-------+-------+-------+--------+---------+--------------+--------+---------------+-------------+-------------+----------+------------+-----------+--------------------+---------+---------+-------+------+------------+-----------+---------+---------+-------+------------+--------+--------+------------+--------+--------+-------------+------------+-------+-------+
| 8015c0 | IGO429   |       5950 |       6000 | 203.1 |   180 |   202 |  0.304 |    91.4 |        -0.03 |   -0.7 |          91.4 |           0 |          32 |     0553 | A3         |    1015.2 |               6016 | 13.2091 | 77.4447 |     8 |  186 |        1.4 |         2 |       9 |       2 |     3 | perhour    | []     | []     |        252 |    0.2 |  -20.6 | none        |          1 |     2 |     3 |
+--------+----------+------------+------------+-------+-------+-------+--------+---------+--------------+--------+---------------+-------------+-------------+----------+------------+-----------+--------------------+---------+---------+-------+------+------------+-----------+---------+---------+-------+------------+--------+--------+------------+--------+--------+-------------+------------+-------+-------+
| 896440 | ETD238   |       5025 |       5125 | 176   |   158 |   176 |  0.26  |    90.7 |        -0.09 |    1.6 |          92.3 |        -896 |        -704 |     1720 | A3         |    1015.2 |               7008 | 13.2081 | 77.5692 |     8 |  186 |        0.2 |         2 |       9 |       1 |     3 | perhour    | []     | []     |        468 |    0.2 |  -23.6 | none        |          1 |     1 |     3 |
+--------+----------+------------+------------+-------+-------+-------+--------+---------+--------------+--------+---------------+-------------+-------------+----------+------------+-----------+--------------------+---------+---------+-------+------+------------+-----------+---------+---------+-------+------------+--------+--------+------------+--------+--------+-------------+------------+-------+-------+
2024-03-04 19:31:19,909 - INFO - ---------- END ----------
```

Example showing data from `dump1090-fa` reading the `history_n.json` files

```shell
$ python3 flightStats.py --dump1090-fa --history
2024-03-04 19:32:33,951 - INFO - ---------- START ----------
2024-03-04 19:32:33,951 - INFO - Set to load flight stats from dump1090-fa
2024-03-04 19:32:33,951 - INFO - Set to load historical flight stats
2024-03-04 19:32:33,952 - INFO - Trying to load data from /var/run/dump1090-fa/history_63.json
2024-03-04 19:32:33,952 - INFO - Data loaded successfully from file!
2024-03-04 19:32:33,952 - INFO - Trying to load data from /var/run/dump1090-fa/history_62.json
2024-03-04 19:32:33,952 - INFO - Data loaded successfully from file!
<----snipped---->
2024-03-04 19:32:33,966 - INFO - Parsing aircraft information
2024-03-04 19:32:33,966 - INFO - Skipping dataset [ICAO: 896440 ] due to missing flight information!
2024-03-04 19:32:33,966 - INFO - Skipping dataset [ICAO: 800521 ] due to missing flight information!
2024-03-04 19:32:33,966 - INFO - Skipping dataset [ICAO: 8014e5 ] due to missing flight information!
2024-03-04 19:32:33,966 - INFO - Parsing aircraft information
<----snipped---->
+--------+----------+------------+------------+-------+-------+-------+--------+---------+--------------+--------+---------------+-------------+-------------+----------+------------+-----------+--------------------+---------+---------+-------+------+------------+-----------+---------+---------+-------+------------+------------------------------------------------------------------------------------+--------+------------+--------+--------+-------------+------------+-------+-------+---------------+--------------------+---------------------------------------+
| hex    | flight   |   alt_baro |   alt_geom |    gs |   ias |   tas |   mach |   track |   track_rate |   roll |   mag_heading |   baro_rate |   geom_rate |   squawk | category   |   nav_qnh |   nav_altitude_mcp |     lat |     lon |   nic |   rc |   seen_pos |   version |   nac_p |   nac_v |   sil | sil_type   | mlat                                                                               | tisb   |   messages |   seen |   rssi | emergency   |   nic_baro |   gva |   sda |   nav_heading |   nav_altitude_fms | nav_modes                             |
+========+==========+============+============+=======+=======+=======+========+=========+==============+========+===============+=============+=============+==========+============+===========+====================+=========+=========+=======+======+============+===========+=========+=========+=======+============+====================================================================================+========+============+========+========+=============+============+=======+=======+===============+====================+=======================================+
| 80138c | IAD990   |       7100 |       7625 | 210.3 |   180 |   206 |  0.308 |   160.3 |        -0.53 |   -5.6 |         161.7 |       -1088 |       -1024 |     2643 | A0         |    1015   |               6000 | 13.2763 | 77.4118 |     8 |  186 |        8.1 |         0 |       8 |       0 |     2 | unknown    | []                                                                                 | []     |        265 |    0.3 |  -24.1 |             |            |       |       |               |                    |                                       |
+--------+----------+------------+------------+-------+-------+-------+--------+---------+--------------+--------+---------------+-------------+-------------+----------+------------+-----------+--------------------+---------+---------+-------+------+------------+-----------+---------+---------+-------+------------+------------------------------------------------------------------------------------+--------+------------+--------+--------+-------------+------------+-------+-------+---------------+--------------------+---------------------------------------+
<----snipped---->
```

### Dump data to CSV File

Using the `--csv` option the JSON data will be dumped to a CSV file. See Example below

```shell
$ python3 flightStats.py --dump1090-fa --latest --csv
2024-03-13 18:05:08,654 - INFO - ---------- START ----------
2024-03-13 18:05:08,654 - INFO - Set to load flight stats from dump1090-fa
2024-03-13 18:05:08,654 - INFO - Set to load latest flight stats
2024-03-13 18:05:08,654 - INFO - Trying to load data from /var/run/dump1090-fa/aircraft.json
2024-03-13 18:05:08,654 - INFO - Data loaded successfully from file!
2024-03-13 18:05:08,654 - INFO - Parsing aircraft information
2024-03-13 18:05:08,655 - INFO - Skipping dataset [ICAO: 800303 ] due to missing flight information!
2024-03-13 18:05:08,655 - INFO - Skipping dataset [ICAO: 8004a7 ] due to missing flight information!
2024-03-13 18:05:08,655 - INFO - Skipping dataset [ICAO: 800db2 ] due to missing flight information!
+--------+----------+------------+------------+-------+---------+-------------+----------+-----------+--------------------+-----------+---------+---------+-------+------------+--------+--------+------------+--------+--------+
| hex    | flight   |   alt_baro |   alt_geom |    gs |   track |   baro_rate |   squawk |   nav_qnh |   nav_altitude_mcp |   version |   nac_p |   nac_v |   sil | sil_type   | mlat   | tisb   |   messages |   seen |   rssi |
+========+==========+============+============+=======+=========+=============+==========+===========+====================+===========+=========+=========+=======+============+========+========+============+========+========+
| 800cbe | IGO7389  |       7400 |       7825 | 198.7 |   298.9 |        -576 |     0237 |    1015.2 |               6000 |         0 |      10 |       0 |     2 | unknown    | []     | []     |          9 |    7.9 |    -24 |
+--------+----------+------------+------------+-------+---------+-------------+----------+-----------+--------------------+-----------+---------+---------+-------+------------+--------+--------+------------+--------+--------+
2024-03-13 18:05:08,655 - INFO - Dumping CSV data to file: [ ./flights_2024-03-13T12:35:08.655779+00:00.csv ]
2024-03-13 18:05:08,656 - INFO - ---------- END ----------
```

Generated CSV File.

```csv
$ cat flights_2024-03-13T12\:35\:08.655779+00\:00.csv
sil,sil_type,nac_p,mlat,tisb,version,alt_baro,nav_altitude_mcp,messages,alt_geom,baro_rate,seen,squawk,nac_v,flight,gs,track,nav_qnh,hex,rssi
2,unknown,10,[],[],0,7400,6000,9,7825,-576,7.9,0237,0,IGO7389 ,198.7,298.9,1015.2,800cbe,-24.0
```
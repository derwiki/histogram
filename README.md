# histogram

### Overview
This is a simple command line tool that accepts a newline seperated list of
integers (e.g. a CSV file) through STDIN and prints an ASCII histogram to
STDOUT.

### Usage
Print full histogram:

    python histogram.py < timings.csv

Print the first 100 bins of the histogram:

    python histogram.py 100 < timings.csv

### Example
    $ python histogram.py 100 < timings.csv
    72453 items, 2302 keys
    0-99	1	
    100-199	1	
    200-299	4	
    300-399	1	
    400-499	1	
    500-599	12	
    600-699	52	=
    700-799	199	=====
    800-899	322	========
    900-999	727	====================
    1000-1099	1118	===============================
    1100-1199	1596	============================================
    1200-1299	1923	=====================================================
    1300-1399	2303	===============================================================
    1400-1499	2631	=========================================================================
    1500-1599	2751	============================================================================
    1600-1699	2879	================================================================================
    1700-1799	2825	==============================================================================
    1800-1899	2744	============================================================================
    1900-1999	2581	=======================================================================
    2000-2099	2517	=====================================================================
    2100-2199	2412	===================================================================
    2200-2299	2210	=============================================================
    2300-2399	2146	===========================================================
    2400-2499	1950	======================================================
    2500-2599	1849	===================================================
    2600-2699	1635	=============================================
    2700-2799	1546	==========================================
    2800-2899	1498	=========================================
    2900-2999	1335	=====================================
    3000-3099	1222	=================================
    3100-3199	1061	=============================
    3200-3299	1033	============================
    3300-3399	996	===========================
    3400-3499	965	==========================
    3500-3599	841	=======================
    3600-3699	793	======================
    3700-3799	733	====================
    3800-3899	725	====================
    3900-3999	638	=================
    4000-4099	588	================
    4100-4199	566	===============
    4200-4299	524	==============
    4300-4399	468	=============
    4400-4499	480	=============
    4500-4599	429	===========
    4600-4699	433	============
    4700-4799	411	===========
    4800-4899	382	==========
    4900-4999	392	==========
    5000-5099	308	========
    5100-5199	340	=========
    5200-5299	289	========
    5300-5399	277	=======
    5400-5499	286	=======
    5500-5599	257	=======
    5600-5699	250	======
    5700-5799	233	======
    5800-5899	217	======
    5900-5999	234	======
    6000-6099	227	======
    6100-6199	217	======
    6200-6299	213	=====
    6300-6399	207	=====
    6400-6499	193	=====
    6500-6599	207	=====
    6600-6699	161	====
    6700-6799	170	====
    6800-6899	172	====
    6900-6999	156	====
    7000-7099	147	====
    7100-7199	148	====
    7200-7299	149	====
    7300-7399	138	===
    7400-7499	137	===
    7500-7599	127	===
    7600-7699	128	===
    7700-7799	114	===
    7800-7899	124	===
    7900-7999	114	===
    8000-8099	110	===
    8100-8199	119	===
    8200-8299	107	==
    8300-8399	103	==
    8400-8499	99	==
    8500-8599	117	===
    8600-8699	99	==
    8700-8799	94	==
    8800-8899	100	==
    8900-8999	85	==
    9000-9099	93	==
    9100-9199	79	==
    9200-9299	62	=
    9300-9399	94	==
    9400-9499	74	==
    9500-9599	68	=
    9600-9699	52	=
    9700-9799	66	=
    9800-9899	57	=
    9900-9999	83	==
    10000-10099	66	=
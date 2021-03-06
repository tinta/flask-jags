# coding=utf-8

all_teams = [
        ["TSG Kirchhellen", 51.603171, 6.917154, "http://uwr1.de/vereine/tsg-kirchhellen", ""],
        ["TSV Malsch", 48.8786745, 8.3373208, "http://uwr1.de/vereine/tsv-malsch", "http://www.uwr-malsch.de/"],
        ["TSC Shark Mannheim", 49.4848, 8.47609, "http://uwr1.de/vereine/tsc-shark-mannheim", "http://www.shark-mannheim.de/"],
        ["Bönnsche Sterntaucher e.V.", 50.73247, 7.09614, "http://uwr1.de/vereine/boennsche-sterntaucher", "http://www.boennsche-sterntaucher.de/"],
        ["TC Hannover", 52.37215, 9.73588, "http://uwr1.de/vereine/tc-hannover", "http://www.tauch-club-hannover.de/"],
        ["Tauchteam Mönchengladbach", 51.1912657, 6.4420437, "http://uwr1.de/vereine/tauchteam-moenchengladbach", "http://www.tauchteam-mg.de/"],
        ["Torpedo Dresden e.V.", 51.0509517, 13.7335724, "http://uwr1.de/vereine/torpedo-dresden", "http://www.torpedo-dresden.de/"],
        ["SV Rheine", 52.27681, 7.43925, "http://uwr1.de/vereine/sv-rheine", "http://www.schwimmverein-rheine-1968.de/"],
        ["TSG Würzburg (Würzburger Planktons)", 49.7944, 9.92802, "http://uwr1.de/vereine/tsg-wuerzburg-wuerzburger-planktons", "http://unterwasserrugby.blogspot.com/"],
        ["TC Manta Zwickau", 50.7144, 12.497, "http://uwr1.de/vereine/tc-manta-zwickau", "http://www.tc-manta-zwickau.de/"],
        ["STC München 1950 e.V.", 48.1393222, 11.5802687, "http://uwr1.de/vereine/stc-muenchen-1950", "http://www.stc-muenchen.de/"],
        ["SSC Karlsruhe", 49.0081278, 8.4037412, "http://uwr1.de/vereine/ssc-karlsruhe", "http://www.ssc-karlsruhe.de/"],
        ["DUC Hamburg e.V.", 53.5538018, 9.9915906, "http://uwr1.de/vereine/duc-hamburg", "http://www.uwr-hh.de/"],
        ["PSV-Oldenburg", 53.1370267, 8.2153482, "http://uwr1.de/vereine/psv-oldenburg", ""],
        ["DUC Bottrop", 51.5222415, 6.9241967, "http://uwr1.de/vereine/duc-bottrop", "http://www.duc-bottrop.de/"],
        ["DUC Hamm", 51.6803972, 7.8174219, "http://uwr1.de/vereine/duc-hamm", "http://www.duc-hamm.de/"],
        ["TC Muräne Karlsruhe", 49.0081278, 8.4037412, "http://uwr1.de/vereine/tc-muraene-karlsruhe", "http://www.tc-muraene.de/"],
        ["Tauch-Club Stelle e.V.", 53.3840782, 10.1114878, "http://uwr1.de/vereine/tauch-club-stelle", "http://tauch-club-stelle.de/"],
        ["DUC Köln e.V.", 50.94028, 6.95976, "http://uwr1.de/vereine/duc-koeln", "http://www.uwr-koeln.de/"],
        ["TSC Lünen", 51.6181172, 7.5245434, "http://uwr1.de/vereine/tsc-luenen", "http://www.TSC-Luenen.de/"],
        ["TSG Meerbusch e.V.", 51.2615802, 6.6772827, "http://uwr1.de/vereine/tsg-meerbusch", "http://www.tsg-meerbusch.de/"],
        ["TSC Mülheim/Ruhr e.V.", 51.4272288, 6.8862528, "http://uwr1.de/vereine/tsc-muelheim-ruhr", "http://www.tsc-muelheim.de/"],
        ["Pulchra Amphora e.V. Neuss", 51.1982772, 6.6951504, "http://uwr1.de/vereine/pulchra-amphora-neuss", "http://www.pulchra-amphora.de/"],
        ["TSG Porz (Köln)", 50.8888426, 7.0570863, "http://uwr1.de/vereine/tsg-porz-koeln", "http://www.porzer-taucher.de/"],
        ["Piranhas Paderborn", 51.715252, 8.7521108, "http://uwr1.de/vereine/piranhas-paderborn", "http://www.piranhas-paderborn.de/"],
        ["TC Manta Saarbrücken", 49.2347178, 6.9942281, "http://uwr1.de/vereine/tc-manta-saarbruecken", "http://www.tcmanta.de/"],
        ["TYC-Sepia Saarlouis", 49.3156784, 6.7503482, "http://uwr1.de/vereine/tyc-sepia-saarlouis", "http://www.tcsepia.de/"],
        ["TCO Weinheim", 49.55186, 8.66579, "http://uwr1.de/vereine/tco-weinheim", "http://www.tco-weinheim.de/"],
        ["Tauchclub Octopus Rosenheim e.V.", 47.85646, 12.1243, "http://uwr1.de/vereine/tauchclub-octopus-rosenheim", "http://www.tco-ro.de/"],
        ["UC Baltic Flensburg e.V.", 54.7804304, 9.4358238, "http://uwr1.de/vereine/uc-baltic-flensburg", "http://www.uc-baltic.de/"],
        ["TC „submarin“ Pößneck", 50.6933253, 11.5908687, "http://uwr1.de/vereine/tc-submarin-poessneck", "http://www.tc-submarin.de/"],
        ["TC Reutlingen", 48.4909048, 9.2058529, "http://uwr1.de/vereine/tc-reutlingen", "http://www.tauchclub-reutlingen.de/"],
        ["WSC Langenau", 48.49692, 10.11927, "http://uwr1.de/vereine/wsc-langenau", "http://www.wsc-langenau.de/"],
        ["TSC Friedrichshafen", 47.6520789, 9.478363, "http://uwr1.de/vereine/tsc-friedrichshafen", "http://www.tscf.de/"],
        ["TC Stuttgart", 48.7769457, 9.181298, "http://uwr1.de/vereine/tc-stuttgart", "http://www.tauchclub-stuttgart.de/"],
        ["SV-Böblingen", 48.6856661, 9.0152538, "http://uwr1.de/vereine/sv-boeblingen", "http://sv-boeblingen.de/"],
        ["UWR Ottobrunn im SVO", 48.065697, 11.662315, "http://uwr1.de/vereine/uwr-ottobrunn-im-svo", "http://www.uwr-ottobrunn.de/"],
        ["TSC Neptun Augsburg", 48.3654866, 10.8949841, "http://uwr1.de/vereine/tsc-neptun-augsburg", "http://www.TSC-Neptun.de/"],
        ["SC Wasserfreunde München", 48.1393222, 11.5802687, "http://uwr1.de/vereine/sc-wasserfreunde-muenchen", "http://www.scw-muenchen.de/"],
        ["STC Graz", 47.0708246, 15.4396679, "http://uwr1.de/vereine/stc-graz", "http://www.stc.or.at/seite34.html"],
        ["Aquanavt", 53.9820058, 37.4729777, "http://uwr1.de/vereine/aquanavt", "http://aquanavt-uwrc.ru/"],
        ["CSP Betta", 55.7554992, 37.6187446, "http://uwr1.de/vereine/csp-betta", "http://uwrc-betta.ru"],
        ["DUC Darmstadt", 49.87236, 8.6502, "http://uwr1.de/vereine/duc-darmstadt", "http://www.duc-darmstadt.net/cms/_rubric/index.php?rubric=5/"],
        ["TSG Konstanz", 47.6619483, 9.1724341, "http://uwr1.de/vereine/tsg-konstanz", "http://www.tsgk-ev.de/"],
        ["1. Paderborner Schwimmverein", 51.7152388, 8.7521128, "http://uwr1.de/vereine/1.-paderborner-schwimmverein", "http://www.paderborner-sv.de/urugby"],
        ["Unterwasser Club Langen e.V.", 49.99242, 8.66697, "http://uwr1.de/vereine/unterwasser-club-langen", "http://UCLangen.de/ "],
        ["TC Heilbronn", 49.1416306, 9.2218249, "http://uwr1.de/vereine/tc-heilbronn", "http://www.uwr-hn.de"],
        ["BUR Berlin e.V.", 52.5233825, 13.4107591, "http://uwr1.de/vereine/bur-berlin", "http://"],
        ["Tauchclub Bamberg", 49.89946, 10.91063, "http://uwr1.de/vereine/tauchclub-bamberg", "http://www.uwr-ba.de/"],
        ["Öcher Otter Unterwasserrugby", 50.7680669, 6.08015, "http://uwr1.de/vereine/oecher-otter-unterwasserrugby", "http://uwraachen.de"],
        ["Unterwasser-Club Osnabrück e.V. (UCO)", 52.253868, 8.047598, "http://uwr1.de/vereine/unterwasser-club-osnabrueck-uco", "http://www.uco-ev.de/"],
        ["FTG Pfungstadt", 49.79074, 8.60854, "http://uwr1.de/vereine/ftg-pfungstadt", "http://uwr-pfungstadt.de/"],
        ["1. TSC Pforzheim", 48.8859385, 8.7208104, "http://uwr1.de/vereine/1.-tsc-pforzheim", "http://tsc-pforzheim.de/"],
        ["TSA Sterkrade", 51.548217, 6.823442, "http://uwr1.de/vereine/tsa-sterkrade", "http://www.tsa-sterkrade.de/"],
        ["SV Derne", 51.569288, 7.51961, "http://uwr1.de/vereine/sv-derne", "http://uwrsvd.de/"],
        ["EKUS (Erster Kärntner Unterwassersportclub)", 46.6260758, 14.3084406, "http://uwr1.de/vereine/ekus-erster-kaerntner-unterwassersportclub", "http://www.ekus.at"],
        ["Austin Underwater Activitites", 30.2824982, -97.7445281, "http://uwr1.de/vereine/austin-underwater-activitites", "http://www.facebook.com/texas.underwater"],
        ["Killeen Underwater Activities", 31.137512, -97.7786813, "http://uwr1.de/vereine/killeen-underwater-activities", "http://www.facebook.com/killeen.underwater"],
        ["The East Haven Makos", 41.2762081, -72.8684337, "http://uwr1.de/vereine/the-east-haven-makos", "http://www.facebook.com/pages/The-East-Haven-Makos/173298612713823"],
        ["Ecomares", 6.235925, -75.575137, "http://uwr1.de/vereine/ecomares", "http://www.ecomares.tk/"],
        ["Deportivo Galicia Rugby Sub", 10.491016, -66.902061, "http://uwr1.de/vereine/deportivo-galicia-rugby-sub", "http://deportivogaliciarugbysub.wordpress.com/"],
        ["Castores Club", 4.5980556, -74.0758333, "http://uwr1.de/vereine/castores-club", "http://www.castoresuwr.com/"],
        ["Quelonios", 3.456855, -76.522438, "http://uwr1.de/vereine/quelonios", "http://www.quelonios.com/"],
        ["Orcas", 6.235925, -75.575137, "http://uwr1.de/vereine/orcas", "http://www.facebook.com/orcasuwrugby"],
        ["PiraNas", 4.15, -73.6333333, "http://uwr1.de/vereine/piranas", "http://www.facebook.com/pages/Club-Pirañas/223460391033145"],
        ["Cachalotes", 4.8142778, -75.6945583, "http://uwr1.de/vereine/cachalotes", "http://www.facebook.com/groups/46441750159"],
        ["Leones Marinos", 4.8142778, -75.6945583, "http://uwr1.de/vereine/leones-marinos", "http://www.facebook.com/groups/157815481289"],
        ["Vikingos", 4.8142778, -75.6945583, "http://uwr1.de/vereine/vikingos", "http://www.facebook.com/group.php?gid=31715161262"],
        ["Barracudas", 3.456855, -76.522438, "http://uwr1.de/vereine/barracudas", "http://www.facebook.com/Clubbarracudasdelvalle"],
        ["Dolphins", 3.456855, -76.522438, "http://uwr1.de/vereine/dolphins", "http://www.facebook.com/group.php?gid=16568458069"],
        ["Barcelona Rugby Subacuàtic ", 41.387917, 2.1699187, "http://uwr1.de/vereine/barcelona-rugby-subacutic", "http://www.facebook.com/bcnrugbysub"],
        ["Unicauca", 2.45, -76.6166667, "http://uwr1.de/vereine/unicauca", "http://www.facebook.com/rugbysubacuaticounicauca"],
        ["Underwater Rugby 101", 64.135338, -21.89521, "http://uwr1.de/vereine/underwater-rugby-101", "http://www.facebook.com/pages/Underwater-Rugby-101-Reykjavik/129951517075087"],
        ["UWRugbees Mittelhessen Pohlheim", 50.528959, 8.7246, "http://uwr1.de/vereine/uwrugbees-mittelhessen-pohlheim", "http://uwrugbees.de"],
        ["PI Copenhagen", 55.704789, 12.576191, "http://uwr1.de/vereine/pi-copenhagen", ""],
        ["Mastini del Blu Rugby Subacqueo", 40.8400969, 14.2516357, "http://uwr1.de/vereine/mastini-del-blu-rugby-subacqueo", "http://www.facebook.com/pages/Mastini-del-Blu-Rugby-Subacqueo/143506792366585"],
        ["Cape Town UWR", -33.9248685, 18.4240553, "http://uwr1.de/vereine/cape-town-uwr", "http://www.facebook.com/pages/South-African-Underwater-Rugby-Federation/182965645069746"],
        ["Izmir UWR Team", 38.41885, 27.12872, "http://uwr1.de/vereine/izmir-uwr-team", "http://kisi.deu.edu.tr/lcavas/"],
        ["VFL Sindelfingen Rugby Ducks", 48.71939, 9.0174, "http://uwr1.de/vereine/vfl-sindelfingen-rugby-ducks", "http://www.vfl-tauchen.de/"],
        ["USZ Zürich", 47.367347, 8.5500025, "http://uwr1.de/vereine/usz-zuerich", "http://www.usz-zuerich.ch"],
        ["Hämeenlinnan Sukeltajat", 60.9917, 24.2470759, "http://uwr1.de/vereine/haemeenlinnan-sukeltajat", ""],
        ["FA TJ CZU Praha", 50.1328946, 14.377322, "http://uwr1.de/vereine/fa-tj-czu-praha", "http://http://www.facebook.com/groups/306425879378956/"],
        ["Club Osos Madrid", 40.3991971, -3.7709875, "http://uwr1.de/vereine/club-osos-madrid", "http://www.clubososmadriduwr.es.gd/"],
        ["University of New South Wales ", -33.9183831, 151.2259812, "http://uwr1.de/vereine/university-of-new-south-wales", "http://www.facebook.com/groups/37293163237/"],
        ["PF České Budějovice", 48.9739084, 14.4750235, "http://uwr1.de/vereine/pf-esk-budjovice", "http://uwrugby.com"],
        ["UWRC Wien", 48.2083556, 16.3677601, "http://uwr1.de/vereine/uwrc-wien", "http://uwrc.at"],
        ["Felix DF", 57.7001754, 11.9899519, "http://uwr1.de/vereine/felix-df", "http://felixdf.net"],
        ["Nutrias CASA-UCV", 10.4901764, -66.8100125, "http://uwr1.de/vereine/nutrias-casa-ucv", "http://rugbysubcasaucv.wordpress.com/"],
        ["Eslovs Underwater rugby Association", 55.8349581, 13.3094322, "http://uwr1.de/vereine/eslovs-underwater-rugby-association", "http://esurf.se"],
        ["Diving-80", 63.6708348, 22.6971162, "http://uwr1.de/vereine/diving-80", "http://www.diving80.fi"],
        ["Firenze Rugby Subacqueo", 43.7785151, 11.2835443, "http://uwr1.de/vereine/firenze-rugby-subacqueo", "http://firenzerugbysub.wordpress.com/"],
        ["TC Münster", 51.9514808, 7.6255388, "http://uwr1.de/vereine/tc-muenster", "http://www.tauchclub-muenster.de/"],
        ["UWR Martillos de Miranda", 10.491016, -66.902061, "http://uwr1.de/vereine/uwr-martillos-de-miranda", "http://http://www.facebook.com/groups/198110433560492/"],
        ["Amager undervandsrugby ", 55.6623686, 12.609015, "http://uwr1.de/vereine/amager-undervandsrugby", "http://amager-uv.dk"],
        ["Molde UVK", 62.7336444, 7.1429988, "http://uwr1.de/vereine/molde-uvk", "http://www.facebook.com/pages/Molde-UVK/289933134354630"],
        ["BSI Boblen", 60.3917193, 5.3169189, "http://uwr1.de/vereine/bsi-boblen", "http://www.boblen.no/index.php?option=com_frontpage&Itemid=1"],
        ["Leviatanes UWR ", 10.0636111, -69.3347222, "http://uwr1.de/vereine/leviatanes-uwr", "http://www.facebook.com/pages/Leviatanes-UWR-Rugby-Subacuático/177090705681672"],
        ["1. Tauchclub Offennburg 1975 E.V.", 48.5005097, 7.9419146, "http://uwr1.de/vereine/1.-tauchclub-offennburg-1975-e.v.", "http://fb.com/UWROG"],
        ["TGR Bielefeld", 52.0212965, 8.5302966, "http://uwr1.de/vereine/tgr-bielefeld", "http://www.tgr-bielefeld.de/"],
        ["Cllub Pirañas Peñafiel", 41.6595521, -4.709429, "http://uwr1.de/vereine/cllub-piraas-peafiel", "http://www.clubpiranas.wordpress.com"],
        ["SALUK Salzburg", 47.7225194, 13.068517, "http://uwr1.de/vereine/saluk-salzburg", ""],
        ["Najadit ry", 60.2131525, 24.8224393, "http://uwr1.de/vereine/najadit-ry", ""],
        ["DUC Krefeld II", 51.35234, 6.61605, "http://uwr1.de/vereine/duc-krefeld-ii", "http://www.duc-krefeld.de"],
        ["Swimming Luxembourg", 49.5971041, 6.1370664, "http://uwr1.de/vereine/swimming-luxembourg", "http://ennerwaasserrugby.wordpress.com/"],
        ["Pinagor", 59.940555, 30.313611, "http://uwr1.de/vereine/pinagor", "http://pinagor-club.ru/"],
        ["Fs Duisburg", 51.406588, 6.794475, "http://uwr1.de/vereine/fs-duisburg", "http://www.fsduisburg.de"],
        ["UWR Rostock 071", 54.0863499, 12.0960117, "http://uwr1.de/vereine/uwr-rostock-071", "http://www.uwr-rostock-071.de"],
        ["Tauchclub Qualle e.V.", 52.2630024, 10.5214314, "http://uwr1.de/vereine/tauchclub-qualle", "http://www.tc-qualle.de"],
        ["UWR Auckland", -36.8484597, 174.7633315, "http://uwr1.de/vereine/uwr-auckland", ""],
        ["UWR Canberra", -35.2819998, 149.1286843, "http://uwr1.de/vereine/uwr-canberra", ""],
        ["Wasserwacht Landshut UWR", 48.5392247, 12.1459218, "http://uwr1.de/vereine/wasserwacht-landshut-uwr", ""],
        ["SC 53 Landshut UWR", 48.5392247, 12.1459218, "http://uwr1.de/vereine/sc-53-landshut-uwr", "http://www.sc53-landshut.de/"],
        ["TC Oberland", 47.8552232, 11.4871747, "http://uwr1.de/vereine/tc-oberland", ""],
        ["DS El Rio", 59.8705229, 17.6233124, "http://uwr1.de/vereine/ds-el-rio", "http://www.facebook.com/dselrio"],
        ["DK Nemo", 59.293358, 17.9772293, "http://uwr1.de/vereine/dk-nemo", "http://dknemo.se"],
        ["Dykkergruppa NTNUI", 63.4121309, 10.4296322, "http://uwr1.de/vereine/dykkergruppa-ntnui", "http://www.dykkergruppa.no"],
        ["OSV Orca", 52.6526472, 4.7710316, "http://uwr1.de/vereine/osv-orca", "http://www.osvorca.nl/"],
        ["Fysalis", 37.8948989, 23.7158948, "http://uwr1.de/vereine/fysalis", "http://www.facebook.com/groups/underwater.rugby.athens/"],
        ["PURE Underwater Rugby", 51.463874, -0.229168, "http://uwr1.de/vereine/pure-underwater-rugby", "http://https://www.facebook.com/PUREUnderwaterRugby"],
        ["Aqualund", 55.6999028, 13.1834172, "http://uwr1.de/vereine/aqualund", "http://www.aqualund.nu/"],
        ["SV Langenfeld", 51.11542, 6.94111, "http://uwr1.de/vereine/sv-langenfeld", "http://www.sv-langenfeld.de/Pub/Index/35"],
        ["UWR Tiszavirág SE", 47.4942449, 19.0424828, "http://uwr1.de/vereine/uwr-tiszavirg-se", "http://www.uwr.hu/"],
        ["Milano Rugby Sub", 45.4643855, 9.1883469, "http://uwr1.de/vereine/milano-rugby-sub", "http://www.rugbysub.it"],
        ["Urheilusukeltajat", 60.1733244, 24.9410248, "http://uwr1.de/vereine/urheilusukeltajat", "http://www.urheilusukeltajat.fi/joomla3"],
        ["Caribes UWR", 10.491016, -66.902061, "http://uwr1.de/vereine/caribes-uwr", ""],
        ["Brescia", 45.5694645, 10.2345418, "http://uwr1.de/vereine/brescia", "http://www.rugbysub.it/rugby-sub-brescia/"],
        ["Aqua Quick", 56.112244, 10.191191, "http://uwr1.de/vereine/aqua-quick", "http://www.aqua-quick.dk"],
        ["Tudserne", 55.352659, 10.337757, "http://uwr1.de/vereine/tudserne", "http://www.tudserne.dk"],
        ["Geofyzika Brno", 49.2144396, 16.6069664, "http://uwr1.de/vereine/geofyzika-brno", "http://https://www.facebook.com/pages/UWR-Geofyzika-Brno/207309206099339"],
        ["Murena", 60.3888182, 25.6732323, "http://uwr1.de/vereine/murena", "http://www.murena.fi"],
        ["Riihimäen Urheilusukeltajat", 60.7416544, 24.7698683, "http://uwr1.de/vereine/riihimaeen-urheilusukeltajat", "http://riusuk.net/uppopallo"],
        ["UW-Rugby Bâle", 47.5707891, 7.614628, "http://uwr1.de/vereine/uw-rugby-bale", "http://www.uwrugbybale.ch/Rugby.html"],
        ["Club de actividades subacuáticas Ecomares", 6.235925, -75.575137, "http://uwr1.de/vereine/club-de-actividades-subacuticas-ecomares", "http://https://www.facebook.com/ecomaresclub"],
        ["Havbasserne", 55.8159691, 12.3512162, "http://uwr1.de/vereine/havbasserne", "http://www.havbasserne.dk"],
        ["Aalborg Students (AASI) UWR", 57.038555, 9.941972, "http://uwr1.de/vereine/aalborg-students-aasi-uwr", "http://aasi.dk/svoemning"],
        ["Vaasan Pyöriäiset", 63.0870406, 21.6193788, "http://uwr1.de/vereine/vaasan-pyoeriaeiset", "http://www.pyoriaiset.com/"],
        ["1.PHRK Bratislava", 48.1728923, 17.1256201, "http://uwr1.de/vereine/1.phrk-bratislava", "http://www.uw-rugby.sk"],
        ["Dråben", 55.0603559, 10.6072248, "http://uwr1.de/vereine/drben", "http://www.draaben.dk"],
        ["TSS Trelleborg", 55.3746952, 13.1613272, "http://uwr1.de/vereine/tss-trelleborg", "http://www.trelleborguvrugby.se/"],
        ["Egersund Dykkeklubb", 58.4514216, 5.9998032, "http://uwr1.de/vereine/egersund-dykkeklubb", "http://www.egersund-dykkeklubb.no/"],
        ["kongsberg dykkerklubb", 59.6715889, 9.6420352, "http://uwr1.de/vereine/kongsberg-dykkerklubb", "http://idrett.speaker.no/organisation.asp?orgelementid=54201"],
        ["Sandefjord Dykkerklubb", 59.1345005, 10.1929727, "http://uwr1.de/vereine/sandefjord-dykkerklubb", "http://www.sdk.no"],
        ["DSSC Duisburg", 51.438029, 6.7741932, "http://uwr1.de/vereine/dssc-duisburg", ""],
        ["Ålesund Sportsdykkerklubb", 62.467569, 6.3500376, "http://uwr1.de/vereine/lesund-sportsdykkerklubb", "http://www.aasdk.no"],
        ["Akkaren Sportsdykkerklubb", 59.8698493, 10.8141584, "http://uwr1.de/vereine/akkaren-sportsdykkerklubb", "http://akkaren.no/"],
        ["Ørland Froskemannsklubb", 63.66292, 9.6807942, "http://uwr1.de/vereine/rland-froskemannsklubb", "http://www.facebook.com/groups/171048022922598/"],
        ["Skovshoved Undersøiske Gruppe", 55.746555, 12.552495, "http://uwr1.de/vereine/skovshoved-undersiske-gruppe", "http://www.s-u-g.dk/"],
        ["Bø Undervannsrugby", 59.4103995, 9.0623454, "http://uwr1.de/vereine/b-undervannsrugby", "http://www-studbo.hit.no/~bouvr/"],
        ["Bølgen Dykkeklubb", 58.3462058, 8.5889996, "http://uwr1.de/vereine/blgen-dykkeklubb", "http://student.grm.hia.no/bolgen/"],
        ["Mandal Dykkerklubb", 58.0261639, 7.440936, "http://uwr1.de/vereine/mandal-dykkerklubb", "http://mandal-dykkerklubb.no/joom/index.php?option=com_content&view=article&id=79&Itemid=63"],
        ["Namsos UV-Rugby klubb", 64.445557, 11.5259298, "http://uwr1.de/vereine/namsos-uv-rugby-klubb", ""],
        ["Squeeze undervannsrugbylag", 59.1387619, 9.6721566, "http://uwr1.de/vereine/squeeze-undervannsrugbylag", "http://www.squeeze.sig.no"],
        ["Sunndal Undervannsrugbyklubb", 62.6439837, 8.729954, "http://uwr1.de/vereine/sunndal-undervannsrugbyklubb", "http://https://www.facebook.com/groups/sunndal.undervannsrugby/"],
        ["Kristiansund Dykkerklubb", 63.1237553, 7.7327528, "http://uwr1.de/vereine/kristiansund-dykkerklubb", "http://www.kdk.no/vare-aktiviteter/uv-rugby"],
        ["Arendal Undervannsklubb", 58.4627514, 8.757857, "http://uwr1.de/vereine/arendal-undervannsklubb", "http://www.arendaluvk.no/"],
        ["Bodø Sportsdykkerklubb", 67.2855762, 14.5537491, "http://uwr1.de/vereine/bod-sportsdykkerklubb", "http://www.bsdk.net/undervannsrugby/"],
        ["Horten Undervannsklubb", 59.4143517, 10.4787341, "http://uwr1.de/vereine/horten-undervannsklubb", "http://hortenuvk.com/"],
        ["Karmøy Sportsdykkerklubb", 59.2741752, 5.3255634, "http://uwr1.de/vereine/karmy-sportsdykkerklubb", "http://www.ndf.no/?menuid=213&klubbid=64"],
        ["Sarpsborg Dykkerklubb", 59.289801, 11.1029563, "http://uwr1.de/vereine/sarpsborg-dykkerklubb", "http://www.sarpsborgdykk.no/"],
        ["Eidsvoll Dykkeklubb", 60.3288695, 11.2569692, "http://uwr1.de/vereine/eidsvoll-dykkeklubb", "http://idrett.speaker.no/organisation.asp?id=54156"],
        ["Verdal Sportsdykkerklubb", 63.8348125, 11.4295337, "http://uwr1.de/vereine/verdal-sportsdykkerklubb", "http://www.vsdk.no/"],
        ["Steinkjer Sportsdykkere", 64.0177685, 11.4915218, "http://uwr1.de/vereine/steinkjer-sportsdykkere", "http://www.Steinkjersportsdykkere.no/"],
        ["Inderøy Undervannsklubb", 63.9117592, 11.1899859, "http://uwr1.de/vereine/indery-undervannsklubb", "http://www.iuk.no"],
        ["HSP Münster", 51.95484, 7.52728, "http://uwr1.de/vereine/hsp-muenster", "http://muenster.hochschulsport-nrw.de/angebote/aktueller_zeitraum/_Unterwasserrugby.html"],
        ["Sandnes og Jæren Dykkerklubb", 58.9281926, 5.8506145, "http://uwr1.de/vereine/sandnes-og-jren-dykkerklubb", "http://sjdk.trep.no/"],
        ["Jyväskylän Uppopalloilijat", 62.2366242, 25.7273648, "http://uwr1.de/vereine/jyvaeskylaen-uppopalloilijat", ""],
        ["MSDK Torpederna", 55.5996534, 12.9926225, "http://uwr1.de/vereine/msdk-torpederna", "http://www.msdk.se"],
        ["Isbjörnarna", 63.8320594, 20.2831807, "http://uwr1.de/vereine/isbjoernarna", "http://www.isbjornarna.com"],
        ["Flipper", 55.7060426, 12.5143053, "http://uwr1.de/vereine/flipper", "http://www.flipper.dk"],
        ["NZUWR Wellington", -41.3150858, 174.79322, "http://uwr1.de/vereine/nzuwr-wellington", "http://www.nzuwr.org.nz"],
        ["NZUWR Auckland", -36.8767852, 174.6338659, "http://uwr1.de/vereine/nzuwr-auckland", "http://www.nzuwr.org.nz"],
        ["The Brisbane Gauls", -27.4991588, 153.0000416, "http://uwr1.de/vereine/the-brisbane-gauls-the-official-brisbane-underwater-rugby-team", "http://unidive.org/"],
        ["Tampereen Urheilusukeltajat", 61.4990475, 23.8052907, "http://uwr1.de/vereine/tampereen-urheilusukeltajat", "http://www.taursu.fi/"],
        ["Triton Beroun", 49.9672047, 14.0862836, "http://uwr1.de/vereine/triton-beroun", "http://www.triton-beroun.cz/"],
        ["Medusas", 4.5980556, -74.0758333, "http://uwr1.de/vereine/medusas", ""],
        ["TSI SURK", 69.647768, 18.938665, "http://uwr1.de/vereine/tsi-surk", "http://www.facebook.com/tsisurk"],
        ["Victoria UWR", -37.845861, 144.96386, "http://uwr1.de/vereine/victoria-uwr", "http://www.facebook.com/#!/groups/1429964573884202/"],
        ["Hipocampos", 3.4205556, -76.5222222, "http://uwr1.de/vereine/hipocampos", "http://clubdebuceohipocampos.com/"],
        ["TSC Bremen", 53.1013476, 8.8611632, "http://uwr1.de/vereine/tsc-bremen", "http://tsc-bremen.de/"],
        ["Bordeaux", 44.8009702, -0.6037738, "http://uwr1.de/vereine/bordeaux", "http://www.facebook.com/pages/Rugby-Subaquatique-Bordeaux/354263638045580"],
        ["Toronto UWR Club", 43.653226, -79.3831843, "http://uwr1.de/vereine/toronto-uwr-club", "http://underwaterrugby.ca", "http://www.meetup.com/Toronto-Underwater-Rugby-Club/"],
        ["Unterwasserrugby Kaiserslautern", 49.4400657, 7.7491265, "http://uwr1.de/vereine/unterwasserrugby-kaiserslautern", "http://uwr-kl.de"],
        ["First Asian Team Underwater Rugby (Singapore), FATUWR", 1.296968, 103.8025403, "http://uwr1.de/vereine/first-asian-team-underwater-rugby-singapore-fatuwr", "http://www.fatuwr.com"],
        ["Hydromania", 60.2654735, 24.8517629, "http://uwr1.de/vereine/hydromania", "http://www.hydromania.org/newsite/"],
        ["Oulun Vesimiehet", 65.0091589, 25.4978333, "http://uwr1.de/vereine/oulun-vesimiehet", "http://www.vesimiehet.fi/toiminta/uppopallo/"],
        ["Meri-Lapin Uppopalloseura", 65.8402461, 24.1771577, "http://uwr1.de/vereine/meri-lapin-uppopalloseura", "http://www.melups.com/Home"],
        ["Rauman Laitesukeltajat", 61.1229263, 21.4972177, "http://uwr1.de/vereine/rauman-laitesukeltajat", "http://www.raumanlaitesukeltajat.fi/?page_id=224"],
        ["Saaristomeren Sukeltajat", 60.47817, 22.2607195, "http://uwr1.de/vereine/saaristomeren-sukeltajat", "http://www.saaristomerensukeltajat.fi/index.php"],
        ["Joensuun Urheilusukeltajat", 62.6031443, 29.7437132, "http://uwr1.de/vereine/joensuun-urheilusukeltajat", "http://www.joensuunurheilusukeltajat.fi/"],
        ["Espoon Urheilusukeltajat", 60.1784487, 24.8074576, "http://uwr1.de/vereine/espoon-urheilusukeltajat", ""],
        ["Kotka Divers", 60.4577657, 26.937622, "http://uwr1.de/vereine/kotka-divers", "http://www.kotkadivers.net/"],
        ["Lakeuden Sukeltajat", 62.78511, 22.8301036, "http://uwr1.de/vereine/lakeuden-sukeltajat", "http://www.lakeudensukeltajat.fi/index.php/home.html"],
        ["Nokian Urheilusukeltajat", 61.478516, 23.5142666, "http://uwr1.de/vereine/nokian-urheilusukeltajat", "http://www.nokianurheilusukeltajat.net/"],
        ["Keski-Uudenmaan Sukeltajat", 60.4009738, 25.0296799, "http://uwr1.de/vereine/keski-uudenmaan-sukeltajat", "http://www.keskiuudenmaansukeltajat.fi/"],
        ["Ylivieskan Urheilusukeltajat", 64.066852, 24.5264389, "http://uwr1.de/vereine/ylivieskan-urheilusukeltajat", "http://ylivieskanurheilusukeltajat.omasivu.fi/uppopallo/"],
        ["Sukellusseura Vesikot", 60.8740204, 26.7147226, "http://uwr1.de/vereine/sukellusseura-vesikot", "http://www.vesikot.fi/"],
        ["Hyvinkään Urheilusukeltajat", 60.631039, 24.8331858, "http://uwr1.de/vereine/hyvinkaeaen-urheilusukeltajat", "http://www.hyvinkaanurheilusukeltajat.fi/"],
        ["Kokkolan Merisaukot", 63.8456084, 23.1324363, "http://uwr1.de/vereine/kokkolan-merisaukot", "http://www.merisaukot.fi/"],
        ["DUC Krefeld", 51.35047, 6.61416, "http://uwr1.de/vereine/duc-krefeld", "http://duc-krefeld.de/unterwasserrugby/"],
        ["Underwater Rugby Tasmania", -42.8783318, 147.3221138, "http://uwr1.de/vereine/underwater-rugby-tasmania", "https://underwaterrugbytasmania.wordpress.com/"],
]


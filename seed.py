"""Seed file to populate all airline info for all 3 airline alliances in database."""

from models import db, User, Flight, Airline, UserAirline
from app import app

# Create all tables
# db.drop_all()
db.create_all()

### Instantiate all  airlines from 3 major alliances with Airline class

# ONEWORLD (15)
a1 = Airline(
    name="Alaska Airlines",
    iata_code="AS",
    reward_program="Mileage Plan",
    alliance="Oneworld",
    logo="/static/pics/logos/AS_name.png",
    symbol="/static/pics/logos/AS_logo.png",
    url="https://www.alaskaair.com/"
)
a2 = Airline(
    name="American Airlines",
    iata_code="AA",
    reward_program="AAdvantage",
    alliance="Oneworld",
    logo="/static/pics/logos/AA_name.png",
    symbol="/static/pics/logos/AA_logo.png",
    url="https://www.aa.com/homePage.do"
)
a3 = Airline(
    name="British Airways",
    iata_code="BA",
    reward_program="Executive Club",
    alliance="Oneworld",
    logo="/static/pics/logos/BA_name.png",
    symbol="/static/pics/logos/BA_logo.png",
    url="https://www.britishairways.com/travel/home/public/en_us/"
)
a4 = Airline(
    name="Cathay Pacific",
    iata_code="CX",
    reward_program="Cathay",
    alliance="Oneworld",
    logo="/static/pics/logos/CX_name.png",
    symbol="/static/pics/logos/CX_logo.png",
    url="https://www.cathaypacific.com/cx/en_US.html"
)
a5 = Airline(
    name="Finnair",
    iata_code="AY",
    reward_program="Finnair Plus",
    alliance="Oneworld",
    logo="/static/pics/logos/AY_name.png",
    symbol="/static/pics/logos/AY_logo.png",
    url="https://www.finnair.com/us-en/finnair-plus"
)
a6 = Airline(
    name="Iberia",
    iata_code="IB",
    reward_program="Iberia Plus",
    alliance="Oneworld",
    logo="/static/pics/logos/IB_name.png",
    symbol="/static/pics/logos/IB_logo.png",
    url="https://www.iberia.com/us/all-iberiaplus/"
)
a7 = Airline(
    name="Japan Airlines",
    iata_code="JL",
    reward_program="Mileage Bank",
    alliance="Oneworld",
    logo="/static/pics/logos/JL_name.png",
    symbol="/static/pics/logos/JL_logo.png",
    url="https://www.jal.co.jp/jp/en/jalmile/flyon/guide.html"
)
a8 = Airline(
    name="Malaysia Airlines",
    iata_code="MH",
    reward_program="Enrich",
    alliance="Oneworld",
    logo="/static/pics/logos/MH_name.png",
    symbol="/static/pics/logos/MH_logo.png",
    url="https://www.malaysiaairlines.com/hq/en.html"
)
a9 = Airline(
    name="Qantas",
    iata_code="QF",
    reward_program="Frequent Flyer",
    alliance="Oneworld",
    logo="/static/pics/logos/QF_name.png",
    symbol="/static/pics/logos/QF_logo.png",
    url="https://www.qantas.com/us/en/frequent-flyer/discover-and-join/join.html"
)
a10 = Airline(
    name="Qatar Airways",
    iata_code="QR",
    reward_program="Privilege Club",
    alliance="Oneworld",
    logo="/static/pics/logos/QR_name.png",
    symbol="/static/pics/logos/QR_logo.png",
    url="https://www.qatarairways.com/en/homepage.html"
)
a11 = Airline(
    name="Royal Air Maroc",
    iata_code="AT",
    reward_program="Safar Flyer",
    alliance="Oneworld",
    logo="/static/pics/logos/AT_name.png",
    symbol="/static/pics/logos/AT_logo.png",
    url="https://www.royalairmaroc.com/us-en/home"
)
a12 = Airline(
    name="Royal Jordanian",
    iata_code="RJ",
    reward_program="Royal Club",
    alliance="Oneworld",
    logo="/static/pics/logos/RJ_name.png",
    symbol="/static/pics/logos/RJ_logo.png",
    url="https://www.rj.com/en"
)
a13 = Airline(
    name="SriLankan Airlines",
    iata_code="UL",
    reward_program="Fly SmiLes",
    alliance="Oneworld",
    logo="/static/pics/logos/UL_name.png",
    symbol="/static/pics/logos/UL_logo.png",
    url="https://www.srilankan.com/flysmiles/home/register"
)
a14 = Airline(
    name="Fiji Airways",
    iata_code="FJ",
    reward_program="Tabua Club",
    alliance="Oneworld",
    logo="/static/pics/logos/FJ_name.png",
    symbol="/static/pics/logos/FJ_logo.png",
    url="https://www.fijiairways.com/en-us/"
)
a15 = Airline(
    name="Oman Air",
    iata_code="WY",
    reward_program="Sinbad",
    alliance="Oneworld",
    logo="/static/pics/logos/WY_name.png",
    symbol="/static/pics/logos/WY_logo.png",
    url="https://sindbad.omanair.com/"
)

# STAR ALLIANCE (26)
a16 = Airline(
    name="Aegean Airlines",
    iata_code="A3",
    reward_program="Miles & Bonus",
    alliance="Star Alliance",
    logo="/static/pics/logos/A3_name.png",
    symbol="/static/pics/logos/A3_logo.png",
    url="https://en.aegeanair.com/milesandbonus/"
)
a17 = Airline(
    name="Air Canada",
    iata_code="AC",
    reward_program="Aeroplan",
    alliance="Star Alliance",
    logo="/static/pics/logos/AC_name.png",
    symbol="/static/pics/logos/AC_logo.png",
    url="https://www.aircanada.com/ca/en/aco/home/aeroplan.html"
)
a18 = Airline(
    name="Air China",
    iata_code="CA",
    reward_program="Phoenix Miles",
    alliance="Star Alliance",
    logo="/static/pics/logos/CA_name.png",
    symbol="/static/pics/logos/CA_logo.png",
    url="https://www.airchina.us/US/GB/phoenix-miles/"
)
a19 = Airline(
    name="Air India",
    iata_code="AI",
    reward_program="Flying Returns",
    alliance="Star Alliance",
    logo="/static/pics/logos/AI_name.png",
    symbol="/static/pics/logos/AI_logo.png",
    url="https://www.airindia.in/about-flying-returns-new.htm"
)
a20 = Airline(
    name="Air New Zealand",
    iata_code="NZ",
    reward_program="Airpoints",
    alliance="Star Alliance",
    logo="/static/pics/logos/NZ_name.png",
    symbol="/static/pics/logos/NZ_logo.png",
    url="https://www.airnewzealand.com/ord"
)
a21 = Airline(
    name="ANA",
    iata_code="NH",
    reward_program="ANA Mileage Club",
    alliance="Star Alliance",
    logo="/static/pics/logos/NH_name.png",
    symbol="/static/pics/logos/NH_logo.png",
    url="https://www.ana.co.jp/en/us/amc/"
)
a22 = Airline(
    name="Asiana Airlines",
    iata_code="OZ",
    reward_program="Asiana Club",
    alliance="Star Alliance",
    logo="/static/pics/logos/OZ_name.png",
    symbol="/static/pics/logos/OZ_logo.png",
    url="https://flyasiana.com/C/US/EN/index?site_preference=NORMAL"
)
a23 = Airline(
    name="Austrian",
    iata_code="OS",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/OS_name.png",
    symbol="/static/pics/logos/OS_logo.png",
    url="https://www.austrian.com/us/en/miles-and-more"
)
a24 = Airline(
    name="Avianca",
    iata_code="AV",
    reward_program="Life Miles",
    alliance="Star Alliance",
    logo="/static/pics/logos/AV_name.png",
    symbol="/static/pics/logos/AV_logo.png",
    url="https://www.avianca.com/us/en/experience/lifemiles-program/"
)
a25 = Airline(
    name="Brussels Airlines",
    iata_code="SN",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/SN_name.png",
    symbol="/static/pics/logos/SN_logo.png",
    url="https://www.brusselsairlines.com/us/en/contact/feedback/general/loyalty-programs"
)
a26 = Airline(
    name="COPA Airlines",
    iata_code="CM",
    reward_program="Connect Miles",
    alliance="Star Alliance",
    logo="/static/pics/logos/CM_name.png",
    symbol="/static/pics/logos/CM_logo.png",
    url="https://www.copaair.com/en/web/us/enrollment"
)
a27 = Airline(
    name="Croatia Airlines",
    iata_code="OU",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/OU_name.png",
    symbol="/static/pics/logos/OU_logo.png",
    url="https://www.croatiaairlines.com/miles-and-more"
)
a28 = Airline(
    name="Egyptair",
    iata_code="MS",
    reward_program="EgyptAir Plus",
    alliance="Star Alliance",
    logo="/static/pics/logos/MS_name.png",
    symbol="/static/pics/logos/MS_logo.png",
    url="https://www.egyptairplus.com/MS_Member_WebSite/frequent.jsp"
)
a29 = Airline(
    name="Ethiopian Airlines",
    iata_code="ET",
    reward_program="Sheba Miles",
    alliance="Star Alliance",
    logo="/static/pics/logos/ET_name.png",
    symbol="/static/pics/logos/ET_logo.png",
    url="https://www.ethiopianairlines.com/US/en"
)
a30 = Airline(
    name="EVA Air",
    iata_code="BR",
    reward_program="Infinity MileageLands",
    alliance="Star Alliance",
    logo="/static/pics/logos/BR_name.png",
    symbol="/static/pics/logos/BR_logo.png",
    url="https://www.evaair.com/en-us/index.html"
)
a31 = Airline(
    name="LOT Polish Airlines",
    iata_code="LO",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/LO_name.png",
    symbol="/static/pics/logos/LO_logo.png",
    url="https://www.lot.com/us/en"
)
a32 = Airline(
    name="Lufthansa",
    iata_code="LH",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/LH_name.png",
    symbol="/static/pics/logos/LH_logo.png",
    url="https://www.lufthansa.com/br/en/homepage"
)
a33 = Airline(
    name="SAS",
    iata_code="SK",
    reward_program="EuroBonus",
    alliance="Star Alliance",
    logo="/static/pics/logos/SK_name.png",
    symbol="/static/pics/logos/SK_logo.png",
    url="https://www.flysas.com/us-en/"
)
a34 = Airline(
    name="Shenzhen Airlines",
    iata_code="ZH",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/ZH_name.png",
    symbol="/static/pics/logos/ZH_logo.png",
    url="https://global.shenzhenair.com/zhair/ibe/common/flightSearch.do"
)
a35 = Airline(
    name="Singapore Airlines",
    iata_code="SQ",
    reward_program="KrisFlyer",
    alliance="Star Alliance",
    logo="/static/pics/logos/SQ_name.png",
    symbol="/static/pics/logos/SQ_logo.png",
    url="https://www.singaporeair.com/en_UK/us/home"
)
a36 = Airline(
    name="South African Airways",
    iata_code="SA",
    reward_program="SAA Voyager",
    alliance="Star Alliance",
    logo="/static/pics/logos/SA_name.png",
    symbol="/static/pics/logos/SA_logo.png",
    url="https://www.flysaa.com/"
)
a37 = Airline(
    name="SWISS",
    iata_code="LX",
    reward_program="Miles & More",
    alliance="Star Alliance",
    logo="/static/pics/logos/LX_name.png",
    symbol="/static/pics/logos/LX_logo.png",
    url="https://www.swiss.com/ua/en/homepage"
)
a38 = Airline(
    name="TAP Portugal",
    iata_code="TP",
    reward_program="Miles & Go",
    alliance="Star Alliance",
    logo="/static/pics/logos/TP_name.png",
    symbol="/static/pics/logos/TP_logo.png",
    url="https://www.flytap.com/en-us/"
)
a39 = Airline(
    name="Thai Airways International",
    iata_code="TG",
    reward_program="Royal Orchid Plus",
    alliance="Star Alliance",
    logo="/static/pics/logos/TG_name.png",
    symbol="/static/pics/logos/TG_logo.png",
    url="https://www.thaiairways.com/en_TH/rop/index.page"
)
a40 = Airline(
    name="Turkish Airlines",
    iata_code="TK",
    reward_program="Miles & Smiles",
    alliance="Star Alliance",
    logo="/static/pics/logos/TK_name.png",
    symbol="/static/pics/logos/TK_logo.png",
    url="https://www.turkishairlines.com/en-tr/"
)
a41 = Airline(
    name="United Airlines",
    iata_code="UA",
    reward_program="MileagePlus",
    alliance="Star Alliance",
    logo="/static/pics/logos/UA_name.png",
    symbol="/static/pics/logos/UA_logo.png",
    url="https://www.united.com/en/us/"
)

# SKYTEAM (17)
a42 = Airline(
    name="Aerolineas Argentinas",
    iata_code="AR",
    reward_program="Aerolineas Plus",
    alliance="Sky Team",
    logo="/static/pics/logos/AR_name.png",
    symbol="/static/pics/logos/AR_logo.png",
    url="https://www.aerolineas.com.ar/en-eu"
)
a43 = Airline(
    name="Aeromexico",
    iata_code="AM",
    reward_program="Club Premier",
    alliance="Sky Team",
    logo="/static/pics/logos/AM_name.png",
    symbol="/static/pics/logos/AM_logo.png",
    url="https://aeromexico.com/en-us"
)
a44 = Airline(
    name="Air Europa",
    iata_code="UX",
    reward_program="Air Europa SUMA",
    alliance="Sky Team",
    logo="/static/pics/logos/UX_name.png",
    symbol="/static/pics/logos/UX_logo.png",
    url="https://www.aireuropa.com/us/en/home"
)
a45 = Airline(
    name="Air France",
    iata_code="AF",
    reward_program="Flying Blue",
    alliance="Sky Team",
    logo="/static/pics/logos/AF_name.png",
    symbol="/static/pics/logos/AF_logo.png",
    url="https://wwws.airfrance.fr/splash"
)
a46 = Airline(
    name="China Airlines",
    iata_code="CI",
    reward_program="Dynasty Flyer",
    alliance="Sky Team",
    logo="/static/pics/logos/CI_name.png",
    symbol="/static/pics/logos/CI_logo.png",
    url="https://www.china-airlines.com/us/en"
)
a47 = Airline(
    name="Czech Airlines",
    iata_code="OK",
    reward_program="OK Plus",
    alliance="Sky Team",
    logo="/static/pics/logos/OK_name.png",
    symbol="/static/pics/logos/OK_logo.png",
    url="https://www.csa.cz/cz-en/frequent-flyers/"
)
a48 = Airline(
    name="Delta Air Lines",
    iata_code="DL",
    reward_program="Skymiles",
    alliance="Sky Team",
    logo="/static/pics/logos/DL_name.png",
    symbol="/static/pics/logos/DL_logo.png",
    url="https://www.delta.com/"
)
a49 = Airline(
    name="Garuda Indonesia",
    iata_code="GA",
    reward_program="GarudaMiles",
    alliance="Sky Team",
    logo="/static/pics/logos/GA_name.png",
    symbol="/static/pics/logos/GA_logo.png",
    url="https://www.garuda-indonesia.com/other-countries/en/index"
)
a50 = Airline(
    name="ITA Airways",
    iata_code="AZ",
    reward_program="MilleMiglia",
    alliance="Sky Team",
    logo="/static/pics/logos/AZ_name.png",
    symbol="/static/pics/logos/AZ_logo.png",
    url="https://www.ita-airways.com/en_us/homepage.html"
)
a51 = Airline(
    name="Kenya Airways",
    iata_code="KQ",
    reward_program="Flying Blue",
    alliance="Sky Team",
    logo="/static/pics/logos/KQ_name.png",
    symbol="/static/pics/logos/KQ_logo.png",
    url="https://www.kenya-airways.com/us/en/"
)
a52 = Airline(
    name="KLM",
    iata_code="KL",
    reward_program="Flying Blue",
    alliance="Sky Team",
    logo="/static/pics/logos/KL_name.png",
    symbol="/static/pics/logos/KL_logo.png",
    url="https://www.klm.com/"
)
a53 = Airline(
    name="Korean Air",
    iata_code="KE",
    reward_program="SKYPASS",
    alliance="Sky Team",
    logo="/static/pics/logos/KE_name.png",
    symbol="/static/pics/logos/KE_logo.png",
    url="https://www.koreanair.com/us/en"
)
a54 = Airline(
    name="MEA",
    iata_code="ME",
    reward_program="Cedar Miles",
    alliance="Sky Team",
    logo="/static/pics/logos/ME_name.png",
    symbol="/static/pics/logos/ME_logo.png",
    url="https://www.mea.com.lb/"
)
a55 = Airline(
    name="Saudi Arabian Airlines",
    iata_code="SV",
    reward_program="ALFURSAN",
    alliance="Sky Team",
    logo="/static/pics/logos/SV_name.png",
    symbol="/static/pics/logos/SV_logo.png",
    url="https://www.saudia.com/"
)
a56 = Airline(
    name="TAROM",
    iata_code="RO",
    reward_program="Flying Blue",
    alliance="Sky Team",
    logo="/static/pics/logos/RO_name.png",
    symbol="/static/pics/logos/RO_logo.png",
    url="https://www.tarom.ro/en/skyteam"
)
a57 = Airline(
    name="Vietnam Airlines",
    iata_code="VN",
    reward_program="LotusMiles",
    alliance="Sky Team",
    logo="/static/pics/logos/VN_name.png",
    symbol="/static/pics/logos/VN_logo.png",
    url="https://www.vietnamairlines.com/us/en/home"
)
a58 = Airline(
    name="Xiamen Airlines",
    iata_code="MF",
    reward_program="Egret Miles",
    alliance="Sky Team",
    logo="/static/pics/logos/MF_name.png",
    symbol="/static/pics/logos/MF_logo.png",
    url="https://www.xiamenair.cn/en-cn/"
)

db.session.add_all([
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, 
    a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, 
    a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, 
    a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, 
    a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, 
    a51, a52, a53, a54, a55, a56, a57, a58
    ])

db.session.commit()

print("FINISHED SEEDING!")
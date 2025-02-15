import nextcord
from nextcord.ext import commands
import random
import os

DISCORD_TOKEN = 'MTI5OTQwMTk2ODU3MzM1NDA3Nw.GCm-nd.XTJUf-UMkJyrx1vmwpeFPaTVZpAF0wNNAPZUN8'

intents = nextcord.Intents.default()
intents.message_content = True
discord_bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

img = "https://cdn.discordapp.com/attachments/1337159372190777406/1337514039445557369/1000109936-removebg-preview.png?ex=67a7b884&is=67a66704&hm=b0ec08fbaf4c6c2f788070b54e2c6240ab262113b9cdf79a3c5b8a655b7094c0&"
amazon = "https://www.primevideo.com/region/eu/offers/ref=atv_dp_atf_tv_signup_3p_bb_t1IAAAAAAA0wg0?force_return_url=1&return_url=%2Fregion%2Feu%2Fdetail%2F0TECOCN1ZHH3W56S1J6SXHQ0UQ%2Fref%3Datv_dp_sign_suc_3P&benefitId=maxes&skipMarketingPage=1"

def luhn_check(card_number):
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def generate_card_number(bin_prefix, length=16):
    card_number = bin_prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - len(bin_prefix) - 1)])
    check_digit = 0
    for i in range(10):
        if luhn_check(card_number + str(i)):
            check_digit = i
            break
    return card_number + str(check_digit)

def generate_random_cvc():
    return str(random.randint(100, 999))

def get_channel_tier(channel_id):
    if channel_id == 1337158788544860170:
        return "free"
    elif channel_id == 1337160660571787426:
        return "basic"
    elif channel_id == 1337161100625576067:
        return "super"
    return "scam"

embed404 = nextcord.Embed(
    title="Wrong Name",
    description="❌  Check the stock for the platforms we accept.",
    color=0x141318
)
embed404.set_thumbnail(url=img)

embed444 = nextcord.Embed(
    title="Oops!",
    description="❌  Looks like you have to upgrade to\na better tier to access this platform!",
    color=0x141318
)
embed444.set_thumbnail(url=img)

steam = {
    "amuckupbeatmantis": "Angrysalt40",
    "farflungdampflamingo": "Itchystick12",
    "obsoletesophisticatedstarling": "Shortcopper86",
    "looseglamorousbeaver": "Busygiraffe74",
    "abrasiveskillfulmanatee": "Bigcamel84",
    "wrathfulanimatedgull": "Wackyred55",
    "savorylightchinchilla": "Newanimal35",
    "vigorousfortunatenarwhal": "Lushwheel95",
    "internalmysteriouscrab": "Slimnose49",
    "adjoiningwakefulcaterpillar": "Ultraroad24",
    "frequentsoresnail": "Megaflower10",
    "spuriousfluffyeland": "Longwhale43",
    "roomypossessiveswan": "Mistymark24",
    "brainymutedunlin": "Oddbike88",
    "secretdazzlinggaur": "Graydugong68",
    "faintwarlikecurlew": "Ivorypatch82",
    "nostalgicbroaddragonfly": "Dampcat64",
    "grotesquefadedchough": "Badfork17",
    "excellentgrubbyarmadillo": "Coldpanther28",
    "crowdeddirtyllama": "Wackybrown41",
    "puzzledgrumpyseal": "Graysoup11",
    "pluckyajarhornet": "Wildgoose81",
    "scandalouswideeyedkouprey": "Kinddingo21",
    "rudewackybee": "Curlyfork17",
    "nondescriptstickycapybara": "Goldmass56",
    "haltingmanytermite": "Wildclass20",
    "idioticerraticgorilla": "Busywinter90",
    "fanaticalmelodichornet": "Weirdkey30",
    "dynamicslimwhale": "Shorttiger61",
    "widesloppydogfish": "Coldanimal68",
    "peacefulshallowcrocodile": "Wildgeese78",
    "beneficialalivegaur": "Windywhite24",
    "dramaticaquaticmandrill": "Megahyena68",
    "flakytemporaryturkey": "Messyface64",
    "goodaccidentaltiger": "Happyship30",
    "pricklyincandescentmink": "Windyend64",
    "scarcelyricalchimpanzee": "Hotmatch24",
    "harshcurvymosquito": "Bigtest42",
    "handsomeglamorousstingray": "Icybean19",
    "iratecageyporcupine": "Limemustang15",
    "abortiveabstractedmallard": "Cutesand46",
    "lovingfertilecat": "Bravecow98",
    "elasticimpartialmanatee": "Graydoe38",
    "unsuitablecutcrane": "Tallengine75",
    "spottyboilingnewt": "Wisesound13",
    "puffysedatestork": "Goodjoke25",
    "quackdaffypheasant": "Freeface27",
}

disney = {
    "Adiilie644@gmail.com": "yTPX8L_MmGkCHc-",
    "Carlos": "Arline2003",
    "DARKIE777": "Squeak777!",
    "Disney1": "Natalia1234",
    "Disney2": "Fercho1981",
    "Disney3": "disney9473",
    "Login": "Jenblue89",
    "Magdalena.maciejewska99@gmail.com": "Krysia123.",
    "antoniobigoderocha1@gmail.com": "Tpb.f1211#",
    "bohananakil": "Hamburger1$",
    "bryceronious": "Sports0607!",
    "chang.julius": "Kanelbulle11",
    "chulien2510@gmail.com": "matou07400",
    "contatocarlinhos4@gmail.com": "98070955@@1",
    "darkie777": "Squeak777!",
    "disney4": "Ian44ron",
    "disney5": "disney1548",
    "fmcclain17": "Devaughn16",
    "futurswim@icloud.com": "sWimmer21",
    "gabriel": "i@Crt3pAuTft7Gv",
    "giovanniedapp1@gmail.com": "2020Ilx!",
    "harrismarquis70@yahoo.com": "wwey5509",
    "hateifyagotta": "Abbey2323",
    "joaosteam675@gmail.com": "Lisboa2023",
    "joaquimbrito_ba@gmail.com": "emporio01",
    "joshandkylie88@hotmail.com": "Smiley88",
    "mayfieldcheryl3@gmail.com": "Brian1119",
    "miracefesari1": "EFE6171@@@A61",
    "monia.frisoni@gmail.com": "Thomas2002",
    "muireannodwyer@eircom.net": "Ronhartom3",
    "nkrund@gmail.com": "nkrund@02",
    "omimdocede@hotmail.com": "w_H%bLNN8Py@Wp5",
    "richellemcd1997": "Winter1997",
    "riley.joisten@gmail.com": "w3ert6y7",
    "shawnjohnson.co@gmail.com": "Denver01",
    "suzannbellestri@gmail.com": "bellestri1005",
    "tamara91rodriguez@gmail.com": "-Always1991-",
    "thierry.merlet1@outlook.com": "Thierry57230",
    "toomeybd@gmail.com": "Gamestop0130",
    "tratau@gmail.com": "tratau@932",
    "vimala5394": "Shevita12",
    "viwem53711@musezoo.com": "viwem53711",
    "zseba32@gmail.com": "psG-$rTKr@jSr8z"
}

crunchyroll = {
    "ar1526114@gmail.com": "0800hijodelanoche",
    "rtorres066@hotmail.com": "2369644@Rtvx2",
    "brenotlou.lb@gmail.com": "Feluca2010!",
    "measurx@gmail.com": "Tahir3900",
    "kelvin.acacio@icloud.com": "35710207apolo123",
    "kevin012_soccer@hotmail.com": "triodelmal2022",
    "josemiguelpaulino06@gmail.com": "jose0697",
    "miguebarletta@gmail.com": "tutankamon",
    "marco.mk.usa@gmail.com": "#Sosuke120598",
    "cristianriver6668@gmail.com": "mancos3272",
    "gawaynewellington22@gmail.com": "mouad..com",
    "silvafelipe342@gmail.com": "88083291",
    "kartikyadav1511@gmail.com": "Explore@9",
    "ilhanhamadi@gmail.com": "ilhandu53",
    "angelius32@gmail.com": "Oxku2025",
    "erlineli24@gmail.com": "real1991",
    "zeloube@gmail.com": "futanari",
    "beiyui@yandex.com": "superbeacon.p05",
    "Exilados2021@outlook.com": "west-virginia",
    "danikacastanier@gmail.com": "danika513",
    "josegatica99@hotmail.com": "1524394285",
    "martinplenacio22@gmail.com": "Mariano1.2.3",
    "seba.css@hotmail.com": "Seba903",
    "Miguebarletta@gmail.com": "tutankamon",
    "chafalotelauty@gmail.com": "191167Horacio",
    "idmelinkup@gmail.com": "Sirevicky@1",
    "azorsa08@gmail.com": "10dejunio",
    "727dsnyder@frhsd.com": "DianKane19",
    "aleesaguirre02@gmail.com": "apolo2244",
    "alejandrogabante7@gmail.com": "Chocolate7",
    "mauricioursino95@gmail.com": "Telefono10",
    "erickpradow99@gmail.com": "erickw99",
    "matiasnicolassanchez.95@gmail.com": "Matias07",
    "konku@hotmail.com": "99071601389Jh",
    "fetenbk752004@gmail.com": "@Mobsessedwithu2",
    "neruka.official@gmail.com": "sankyuu885",
    "indiec@hotmail.fr": "123456",
    "solwarriors2@gmail.com": "Catking201322",
    "juanmaagonzalez777@gmail.com": "juanMAA666",
    "gisex94870@tenjb.com": "m)(^e,H^xC,3?(3",
    "samuel32bg@gmail.com": "samcook22",
    "landas321@gmail.com": "fausto@631",
    "sodre.felipe.sousa@gmail.com": "vida2009",
    "migkellysr@gmail.com": "key-ner",
    "arjunthesaint@gmail.com": "carbonstrength2",
    "gabotecuervodivino@gmail.com": "jesygab0907",
    "ldepetris98@gmail.com": "Tzx678renault",
    "davidpalma@hotmail.cl": "Alh_84;2",
    "ezequiel4km26@hotmail.com": "AnimeFull4",
    "rc.terezzino@uol.com.br": "Zz2vta09",
    "frost.ellam@gmail.com": "Helloagain1",
    "danaailyn17@gmail.com": "Dana2221",
    "16juarezo052@student.hbuhsd.edu": "omar1990",
}

nike = {
    "+34600836023": "enfinserafin74",
    "+8613005567310": "Aa599039929",
    "+8615063959751": "Reborn123456",
    "+8618851825169": "Gg19880419",
    "+8618951262705": "Liuwei2000",
    "+905458152862": "emirhan3421",
    "01109408": "Steph7572!",
    "013.709.466-35": "Sc40391510",
    "02086805999": "Colina15",
    "0484119791": "senbensen123",
    "0528055888": "galz1902",
    "0642754210014": "Patnasnor93700**",
    "0652909285": "Nassjb93700&",
    "0789444669": "micalili33",
    "0852930957": "Tuiphanu045",
    "0855683320": "Pawee978",
    "0902261896": "Guy225511",
    "09459620056": "eldestjohn10",
    "095-420-5180": "Aisara55",
    "1012604": "Babe92211",
    "1150449": "educationart007",
    "1301009012": "lagav211",
    "13796161": "Baiabeno123",
    "14314456736": "gunner23",
    "1510654760279": "Mm045350806!",
    "15743446": "Maya8384",
    "160968281": "Clave123",
    "1850153584": "sebas2000",
    "198.466.188-40": "Joao150807$",
    "2001106942": "Leonardo0302",
    "2018.itm.thiagobrandao": "Thiago7979",
    "210771522": "Nicolaas12",
    "215.250.668-54": "Formigaa1#",
    "215053377": "Esteban11.",
    "226873366": "pmcsgvitoria1981",
    "2292472772": "Elemento115",
    "23037943": "Naoesquece1",
    "2446885004": "barcu050",
    "2852496152": "quiyana244",
    "29813214": "Miracnike35",
    "30334470": "Sevahc21",
    "30449101": "Password1975!",
    "31267839492": "hanaiku23",
    "33408826811": "cbzinha10@",
    "406.598.978-73": "murilo94",
    "4240476": "Bartek2348",
    "44642772": "Kostas1985!",
    "48512139661": "theendriu83",
    "49534638372": "Muck4321",
    "49534638372": "Yusuf336",
    "5015201165": "Joy18012",
    "52606140b": "Emmeta17",
    "5518253835": "Campeones1",
    "55362098": "Lawand10?",
    "5561555456": "catrin06",
    "57338742": "Insada05",
    "59939065": "Sultan11",
    "604374801": "Wojtek2007",
    "63129388": "An191211",
    "63530272": "NIKEchenie2522",
    "63807841": "Alexcam8713",
    "66847905": "basketball001",
    "6934154817": "aristos1990",
    "70017757": "Basketba11",
    "7062436": "iirreennee44",
    "78128293": "Crv101279",
    "792926071": "Tauzen1974",
    "79778585": "Alegria5",
    "80122780": "Vikash15@",
    "84577910": "BoloDeChocolate1704",
    "8615727888729": "Love14410",
    "8618788170758": "Wo18788170758",
    "87030276": "Btnmaleo2",
    "9076247697": "Ash2003$",
    "90774605": "Spaceall2022",
    "92936236": "enea2006",
    "9466788100": "vadikgoyal123",
    "99438483": "Ridzwan89",
    "ADRTWOR4": "Saba2015",
    "ANOOSHASULEMAN@GMAIL.COM": "Zoya2015!",
    "ARCOSDOURADOS": "Loja@2025",
    "Aaajohnsoninfo@gmail.com": "Ariohna27",
    "Aak.dhiman@gmail.com": "Nike1122891",
    "Aaomaom034@gmail.com": "Aaomaom123456789",
    "Abcars73@mail.com": "Abab1973",
    "Abdulsalamyoada58@gmail.com": "Syoadasalam7",
    "Abidsyach1501@gmail.com": "Asprsk1521",
    "Abling": "Katherineabling1103",
    "Abrahambersabe21@gmail.com": "Almendrita7",
    "Acegervacio09@gmail.com": "Alkace21",
    "Adeline.bley@gmail.com": "Afrika225.",
    "Affiqt123@gmail.com": "Ibrahim2008",
}

facebook = {
    "03121596977": "IloveyouATTIA",
    "0603783761": "de_rate2001nokia",
    "0611404209": "nouraforever",
    "0622786544": "stivan24031997@1997",
    "0660154711": "AMINE198580",
    "0662472157": "smail@1997@2002",
    "0664090453": "allahoakbaroooo",
    "0676400421": "erlind.avniballa",
    "0697585195": "angel_ndr2307",
    "0703150641": "workosgmlafftaff1",
    "0772013247": "0772013247",
    "0781136838": "Jpce1994",
    "0782139880": "00001982",
    "0792098952": "0792098952",
    "0885943050": "messi12345",
    "212618705425": "nada-2011",
    "5800": "Dinnar016",
    "6981091771": "resetmasiipeza1312",
    "6981091771": "zzo23000",
    "75460745": "75914705",
    "935472072": "Ospausante",
    "944283845": "944283845",
    "AMINE198580@GMAIL.COM": "SIHAM1996",
    "Admin": "ou0655053396",
    "Myscdemous@yahoo.com": "justme256",
    "Ninjaaxs": "dimitris2006?",
    "Shumno": "EdwardElricFODA08*",
    "UNKNOWN": "P@ssw0rd2020",
    "abir125023": "xlr8pin5xlr8pin5",
    "alam4bit": "alam7700",
    "alam4bit@gmail.com": "Alam7700",
    "alam4bit@yahoo.com": "long7700",
    "alassane314@gmail.com": "Bayelaye314.",
    "angelicamorenafa@gmail.com": "Garoto2014",
    "anthonysimonet@inbox.com": "Ro9ET9g8",
    "artemisosfphasa": "olibiakara4ever",
    "arti.hasa1": "ArtiAudiTT98@",
    "asif00iqbal": "Aa0147852",
    "azad4bit@gmail.com": "alam7700",
    "benmaameridjamel1956@gmail.com": "amina2007",
    "carmandocardona@gmail.com": "Fernanda96",
    "delroydennie@ymail.com": "daviandennie1",
    "eduardomartin96nez@gmail.com": "61204333",
    "eriballa9@gmail.com": "Arben.2017",
    "hatedblaster": "Virtuoso1998",
    "i.want.to.smoke.weed": "kuchakfables(123)",
    "jaouadovic40": "zurholle01",
    "jocker.103": "sex@sex",
    "jocker.lmahbol": "jocker12jockerjocker12jocker",
    "kaka.chocha@gmail.com": "wxcvbn1234",
    "khalidmerzig@gmail.com": "88khaliD88",
    "kitiibwasarah@gmail.com": "070304788282",
    "lmach.103": "jocker.103",
    "lukenialino.brazuane.1": "Marinela",
    "m.h.h.95.89@gmail.com": "2447427mh",
    "m.h.h.95.89@gmail.com": "85077170a",
    "marko.jamnic@hotmail.com": "kolkodanasimasjaja",
    "mdsadaf81@gmail.com": "01912441166",
    "mutenha": "bruno1994",
    "mzlle_veronika@hotmail.com": "veronika@00002018",
    "n1ck_liv@hotmail.com": "nikoslivanos",
    "napstarr@gmail.com": "sniff123",
    "nikhforos2009@windowslive.com": "984779192a",
    "nokbutte@gmail.com": "Clean41For99Ever",
    "nzanzuaustine@yahoo.com": "Trailblazer,2017",
    "oussama284@yahoo.com": "96840626",
    "oussamaboukerfa21@gmail.com": "tatousskikda",
    "oussilat@gmail.com": "khalid10",
    "panagiwtis_kot": "panos01056",
    "rockingdinnar": "Dinnar016",
    "s_is_my_life@ymail.com": "MC180403957",
    "sabbirul.newaz": "01964097519",
    "sajjad.bplan@gmail.com": "Dinnar@016",
    "semllaliyoussef@gmail.com": "168743adilamouchanni",
    "simoahbari99": "0639194920mo",
    "space3stev": "6989122464Stema",
    "tamirr2@hotmail.com": "yaman@123@",
    "tomsblazek@live.com": "loeKIm",
    "uap.tushar@gmail.com": "uap@1120506542"
}

netflix = {
    "adejokebankole@yahoo.com": "Damilola198",
    "burotti@gmail.com": "@Bu0720943",
    "deyalabella2915@gmail.com": "kimberly29",
    "morwesi.sebesho99@gmail.com": "snoma26",
    "diegoedsondp@gmail.com": "76b24fb600",
    "clfitness9290@gmail.com": "290",
    "jonny-hdrock@hotmail.com": "supernatural",
    "francescopugliese.fp@libero.it": "17061996",
    "jonathanjrgensen@gmail.com": "fyqd4360",
    "lucienerrosa@gmail.com": "Rosalaura33@",
    "eksamli@live.com": "Newin2022",
    "robchretien@gmail.com": "soleil25",
    "lizzw88@gmail.com": "Cvbm1506",
    "rajrobinthomas@gmail.com": "095113544",
    "arielacevedo@yahoo.com": "Eldiess0897",
    "va3481298@gmail.com": "279153A",
    "ray.kiswani@outlook.com": "Noor1307",
    "djimark@gmail.com": "Aga161276",
    "Salmaeldeev@gmail.com": "Newyork-260795",
    "stephane6trudel@gmail.com": "netflix180",
    "dawn.roberts@net-centers.org": "Kar**24311",
    "cedwards@daemen.edu": "Nzcm1111",
    "feathergreen@yahoo.com": "Net1988!",
    "ninibutnana@gmail.com": "Hemphill4101",
    "perrygreenfield@me.com": "G00pajo!"
}

discord = {
    "16150133": "4492106570",
    "AionMK": "rL95+fWsK^4NZa+",
    "Alejandro030987": "tequeteque01",
    "Barbosa490": "Password1!",
    "Bmwr45": "Bg5QMGii5p_bgpM",
    "Borjaml": "c8R-_9eyE_FD36*",
    "Boshrufus33": "bd*/2CNp,*9_p-T",
    "Boshrufus": "&%$qYYd-+5-BctX",
    "Clepox": "!&8VP_2KAL$c*yb",
    "Cosmeticsurgery930": "Sh@#12345",
    "DJISR4ELBEATS": "451603",
    "DjAlex1980": "djgogo1975",
    "Dr.hernandoborja": "ra7mxyl163000@",
    "Edoder": "EdoDer30$",
    "Fran3349": "hello3349",
    "GabrieLopez9021": "Glopez19-20",
    "Gancigabriele": "Cavallo2",
    "Ghostqu": "T7tk@VTzED7/Mt.",
    "Guarachin": "m@RILOLI678m@NOLO",
    "Guido.Leonardo": "puticimo69",
    "Guillegax": "hammock2040",
    "HalcyonRyan": "C4lorie-Synt4x",
    "Hrvonic": "Hopperxl123.",
    "Iris_Louisiana": "zednanreh19",
    "Israel3301": "C*a_ja3P=u_J.$Q*aSXoIsra*",
    "Jamco": "jajaja00",
    "Jds07": "JdsCarlos-0761",
    "Joao_Chaves": "Regulus1000",
    "Macflowers": "MuPaD2SX%j#2#W/",
    "Mitchel": "52580mar",
    "Motorikk": "Dandito2500",
    "Nackas1979": "ConnorA2010",
    "Noistodos": "*+%iMjF7!KPJ$+P",
    "PORNOBOSS": "perverz666",
    "Peik": "#w?,h@KqrNF,wF7",
    "PikkuPoeka": "jupe1996",
    "Playstop": "Berl1ncllng",
    "Primlink": "Primlink@12345",
    "ROXY.CO": "suzi4167",
    "Rowica67": "Vinylvreter1",
    "SaintJohn88": "Biafra88",
    "Sux2bu2": "Kelli1963!",
    "TackleBarry": "=J-LF97y6vxWWTe",
    "The_Politzanian": "Ramanauskas1",
    "UNKNOWN": "cutter8124",
    "Urdiartes@gmail.com": "dUrDiArTeS2019",
    "Xaxtar": "Gr@nde2005",
    "Yogyety": "/X-@Gh6qJVa5zM/",
    "agamal81": "mesh3aref",
    "alex1712": "alfaomega1",
    "amyblackcat3": "wrw2*%sJX@RPK$i",
    "andre1233": "ak3156",
    "angelesfortun": "angelesmaki15",
    "arno.cuylle@gmail.com": "Ac_171197_Ac",
    "arthobbie": "Art@space2020",
    "avicoggr67": "24195040",
    "awaelkhalij": "/fCPyKd&./L2/%!",
    "bacuruglum": "XXXzzz@123",
    "barbosa490@yahoo.com": "Password1!",
    "batho.gabor1986@gmail.com": "kolera1986__",
    "berno87": "Brabant2187",
    "bilal_akbar": "Radio1122@",
    "bisemanal11": "Bu74psZx9EZe-#c",
    "bjoernnn": "Cecilie12",
    "danivn": "Tranvandan123.",
    "dcdirk21@gmail.com": "Party2231?",
    "djarg@rocketmail.com": "B8iuFFXWTBTeAtq",
    "djfabiomix": "Carolina2021",
    "djmarkjohnstone@hotmail.com": "Tyler8910@",
    "drntb": "dorian1997",
    "dwsiddall": "eDw@rds1",
    "eduardo": "eduardo91",
    "edymaracas": "pAgASARRI_1969_loveevol",
    "emmawatson786": "Abid786@#",
    "evmoris": "khylee908",
    "fernandorivera1009": "87TCzPhmze@xQ3J",
    "fjbdacanay@yahoo.com": "@Jologsako1972",
    "fliptheswitch1962@gmail.com": "Kelli1963!",
    "garciaguitar7@gmail.com": "Nessie77",
    "gmoraleso@telefonica.net": "IBgm7340",
    "grantsgirl@live.com": "grapes79",
    "hamy132": "Tranvandan123.",
    "hlangr": "393078hl",
    "hostein": "B00yaShaka413",
    "ian.j.aplin": "cheesecakes4me",
    "imsudhar": "9790190313",
    "ing.florestoro": "4h85mBXxCqD.PL!",
    "iosif2": "tinhorse23@#",
    "jamilehti12345": "Jamil49v",
    "jaydeemk2": "spectroman1",
    "jessica_kissa@hotmail.com": "livia06",
    "johnnysalsa507pty@gmail.com": "3CatC5eCrSk",
    "julenarenal@gmail.com": "45822485E",
    "jumprydz": "MU-_)BuR9&Z!nSZ",
    "kamikase": "kamikase84",
    "koolinkanton": "Kelli1963!",
    "kyvinnie@yahoo.com": "Kelli1963!",
    "labovic.radomir@gmail.com": "Discogs2021",
    "libraclint": "Maeve2020",
    "lopes6522": "Lopes6523",
    "mcank1945": "f5d8635-4",
    "mgrdjp": "48931032Gg",
    "mica.angry": "GqFB95itr@kZcRH",
    "michaeldwsd": "@Sp#offpage313",
    "nicholasgomesz": "discodesucesso13",
    "otto.ventura@yahoo.com": "Apu5i2ux@&A\"Q{%|",
    "petirico": "616014391",
    "pinedes627@yahoo.com": "didier627",
    "powerwouz": "alkmaar1820",
    "prod.moddedmusic@moddedmusic.net": "password1",
    "raven77": "pVNs,pbHcaX-W32",
    "razvantorr": "AstraH2008",
    "reviews_ma": "36V6w?ynb$sFSvx",
    "rpmbilbao@gmail.com": "@Laor#rpmb110256",
    "ryancooper23": "P!@#$1234qwe",
    "saintjohn88": "Biafra88",
    "samuelcincelli": "sorastant1994",
    "sandycheeks0809": "Nalley10",
    "satpal123@hotmail.com": "1seagate7",
    "seoservices9800": "shariar9800",
    "sosa24330": "tentos12",
    "taketangentleman": "bcadtnhn20010618",
    "thierrypsilon": "trx450r6",
    "tommytommy456": "Alfaromeo456",
    "unknown": "Sleetgrout666",
    "vimaloco": "vTUyEeQcTYR_D5N",
    "vinniethed": "Kelli1963!",
    "xOwNx": "P1234567$",
    "xxivvo": "7mb_#XNP*N%y*UE",
    "zeusez": "Ce1l52d1"
}

platforms = {
    "adobe": "426578990015|02|25|First connect to USA via VPN.",
    "amazon": "60457811436|09|27|Check out <#1321531783233278045>",
    "amazonmusic": "442755053118|02|28|\u200b",
    "amazonprime": "415231384013|10|26|\u200b",
    "amazonvisa": "414840|03|28|Check out <#1321531783233278045>",
    "appleicloud+": "481582039943|05|25|First connect to USA via VPN.",
    "applemusic": "524105613301|09|32|First connect to UAE via VPN.",
    "appletv": "524105613301|09|32|First connect to UAE via VPN.",
    "bestbuy": "5859752142|03|27|\u200b",
    "bookmate": "416916144416|03|29|\u200b",
    "canva": "5211883104402|07|29|First connect to Colombia via VPN.",
    "chess": "518189299624|09|27|First connect to USA via VPN.",
    "crunchyroll": "460972938009|07|26|First connect to Turkey via VPN.",
    "curiositystream": "521188310440|08|29|First connect to USA via VPN.",
    "customgpt": "519535405916|05|27|On checkout use the code AFFILIATEPARTNER.",
    "deezer": "471361000006|11|31|First connect to USA via VPN.",
    "discordnitro": "519535244479|03|28|First connect to Algeria via VPN.",
    "disney": "491282312953|03|30|First connect to Mexico via VPN.",
    "duolingo": "557692005313|03|29|\u200b",
    "express": "519535289291|02|27|Check out <#1321531783233278045>",
    "fubo": "519535972862|09|26|First connect to USA via VPN.",
    "flixole": "441103714655|09|27|First connect to USA via VPN.",
    "googleone": "535674|06|28|\u200b",
    "googlepay": "519535289291|02|27|Check out <#1321531783233278045>",
    "hbo": "478200206908|04|28|First connect to Spain via VPN, then Sign Up [here](amazon).",
    "hotspot": "519535289291|02|27|Check out <#1321531783233278045>",
    "mcafee": "515462002070|09|27|First connect to USA via VPN.",
    "microsoft": "521188310440|07|29|First connect to UAE via VPN.",
    "mubi": "557501000004|03|26|\u200b",
    "netflix": "559888039281|09|29|First connect to Thailand via VPN.",
    "norton": "533949411675|04|27|First connect to USA via VPN.",
    "peloton": "414734205434|09|31|First connect to USA via VPN.",
    "pluralsight": "521188310835|11|24|First connect to USA via VPN.",
    "viki": "414734204614|06|25|First connect to USA via VPN.",
    "soundcloud": "519535289291|02|27|Check out <#1321531783233278045>",
    "spotify": "442657112008|03|29|First connect to USA via VPN.",
    "stripe": "62430389526|06|31|First connect to Mexico via VPN.",
    "target": "5859752142|08|29|\u200b",
    "tidal": "426578990015|02|25|First connect to USA via VPN.",
    "windscribe": "356343149500|02|27|First connect to USA via VPN.",
    "youtube": "519535244479|03|28|First connect to Algeria via VPN."
}

os.system('cls')

@discord_bot.command(name="genvcc")
async def gen(ctx, platform: str):
    tier = get_channel_tier(ctx.channel.id)
    platform = platform.replace(" ", "").lower()
    if tier == "scam":
        return
    elif platform not in platforms:
        await ctx.send(embed=embed404)
        return
    elif platform not in allowed_vcc[tier]:
        await ctx.send(embed=embed444)
        return

    vpn_country = platforms[platform].split('|')[-1]
    bin_prefix, exp_month, exp_year = platforms[platform].split('|')[:-1]
    card_number = generate_card_number(bin_prefix)
    cvc = generate_random_cvc()
    expiration_date = f"{exp_month}/{exp_year}"

    embed = nextcord.Embed(
        title="Virtual Credit Card",
        description=f"**💳  Your VCC Info:**\n**Card Number:** {card_number}\n**CVC/CVV:** {cvc}\n**Expiration Date:** {expiration_date}\n-# {vpn_country}",
        color=0x141318
    )
    embed.set_thumbnail(url=img)

    try:
        await ctx.author.send(embed=embed)
        embed2 = nextcord.Embed(
        title="VCC Generated",
        description="**📨  Your Virtual Credit Card has been sent to your DMs!**",
        color=0x141318)
        embed2.set_thumbnail(url=img)
        await ctx.send(embed=embed2)
    except nextcord.Forbidden:
        embed3 = nextcord.Embed(
        title="Error",
        description="**❌  I can't send you a DM. Please check your DM settings.**",
        color=0x141318)
        embed2.set_thumbnail(url=img)
        await ctx.send(embed=embed3)

@discord_bot.command(name="genacc")
async def gen(ctx, platform: str):
    tier = get_channel_tier(ctx.channel.id)
    platform = platform.replace(" ", "").lower()
    
    if tier == "scam":
        return
    
    if platform not in allowed_acc[tier]:
        await ctx.send(embed=embed444)
        return
    
    if platform == "steam":
        user, password = random.choice(list(steam.items()))
    elif platform == "disney":
        user, password = random.choice(list(disney.items()))
    elif platform == "crunchyroll":
        user, password = random.choice(list(crunchyroll.items()))
    elif platform == "nike":
        user, password = random.choice(list(nike.items()))
    elif platform == "facebook":
        user, password = random.choice(list(facebook.items()))
    elif platform == "netflix":
        user, password = random.choice(list(netflix.items()))
    elif platform == "discord":
        user, password = random.choice(list(discord.items()))
    else:
        await ctx.send(embed=embed404)
        return

    embed44 = nextcord.Embed(
        title=f"{platform.capitalize()} Account",
        description=f"**🔑   Your Account Info:**\n**User:** {user}\n**Password:** {password}",
        color=0x141318
    )
    embed44.set_thumbnail(url=img)

    try:
        await ctx.author.send(embed=embed44)
        embed4 = nextcord.Embed(
            title="Account Generated",
            description="**📨  Your Account Info has been sent to your DMs!**",
            color=0x141318
        )
        embed4.set_thumbnail(url=img)
        await ctx.send(embed=embed4)
    except nextcord.Forbidden:
        embed3 = nextcord.Embed(
            title="Error",
            description="**❌  I can't send you a DM. Please check your DM settings.**",
            color=0x141318
        )
        await ctx.send(embed=embed3)

allowed_vcc = {
    "free": ["youtube", "crunchyroll", "disney", "mcafee", "bestbuy"],
    "basic": ["amazon", "bestbuy", "crunchyroll", "mcafee", "adobe", "netflix", "spotify",
    "disney", "youtube", "hbo", "applemusic", "googlepay", "fubo", "tidal", "pluralsight",
    "express", "hotspot", "soundcloud", "duolingo", "viki", "mubi", "flixole"],
    "super": list(platforms.keys())
}

allowed_acc = { "free": [], "basic": ["steam", "crunchyroll", "facebook", "discord"],
    "super": ["steam", "crunchyroll", "disney", "nike", "facebook", "netflix", "discord"]}

@discord_bot.command(name="stock")
async def stock(ctx):
    tier = get_channel_tier(ctx.channel.id)
    if tier == "scam":
        return
    accounts = "\n".join([platform.capitalize() for platform in allowed_acc[tier]])
    vccs = "\n".join([platform.capitalize() for platform in allowed_vcc[tier]])
    tier = tier.capitalize()
    embed = nextcord.Embed(
        title=f"📈  {tier} Gen Stock",
        description=(
            "**Accounts:**\n"
            f"{accounts}\n\n"
            "**VCCs:**\n"
            f"{vccs}"
        ),
        color=0x141318
    )
    if accounts == "":
        embed = nextcord.Embed(
        title=f"📈  {tier} Gen Stock",
        description=(
            "**VCCs:**\n"
            f"{vccs}"
        ),
        color=0x141318
        )
        embed.set_thumbnail(url=img)
        embed.set_thumbnail(url=img)
        await ctx.send(embed=embed)
        return
    embed.set_thumbnail(url=img)
    embed.set_thumbnail(url=img)
    await ctx.send(embed=embed)

@discord_bot.command(name="help")
async def help_command(ctx):
    if get_channel_tier(ctx.channel.id) == "scam":
        return
    embed = nextcord.Embed(
        title="❔  Available Commands",
        color=0x141318)
    embed.add_field(name="!genvcc <platform>", value="Generate a virtual credit card for the specified platform.", inline=False)
    embed.add_field(name="!genacc <platform>", value="Generate an account for the specified platform.", inline=False)
    embed.add_field(name="!stock", value="Check the available platforms.", inline=False)

    embed.set_thumbnail(url=img)
    await ctx.send(embed=embed)

discord_bot.run(DISCORD_TOKEN)

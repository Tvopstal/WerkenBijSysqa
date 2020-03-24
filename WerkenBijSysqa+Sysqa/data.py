import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


#dataschermresoluties werkenbij homepagina DESKTOP
#1920 1080
homepageDesktopWindowSizeWidth = 1920
homepageDesktopWindowSizeHeight = 1080
homepageDesktopLogoTextSize = {'height': 35, 'width': 245}
homepageDesktopLogoTextPosition = {'x': 352, 'y': 29}


#dataschermresoluties werkenbij homepagina TABLET
#1280 800
homepageTabletWindowSizeWidth = 1280
homepageTabletWindowSizeHeight = 800
homepageTabletLogoTextSize = {'height': 35, 'width': 245}
homepageTabletLogoTextPosition = {'x': 32, 'y': 29}


#dataschermresoluties werkenbij homepagina MOBILE
#1280 800
homepageMobileWindowSizeWidth = 720
homepageMobileWindowSizeHeight = 1280


#data voor werkenBijSysqapagina
werkenBijSysqaPaginaHome = "https://www.werkenbijsysqa.nl/"
werkenBijSysqaPaginaVacatures = "https://www.werkenbijsysqa.nl/vacatures"
werkenBijSysqaPaginaVacatures2 = "https://www.werkenbijsysqa.nl/vacatures/"
werkenBijSysqaPaginaVerhalen = "https://www.werkenbijsysqa.nl/verhalen-en-videos"
werkenBijSysqaPaginaKennismaken = "https://www.werkenbijsysqa.nl/kennismaken-met-sysqa/"
werkenBijSysqaPaginaKennismaken2 = "https://www.werkenbijsysqa.nl/kennismaken-met-sysqa"
werkenBijSysqaPaginaKennismakenFooter = "https://www.werkenbijsysqa.nl/kennismaken-met-sysqa"
werkenBijSysqaPaginaVerhalenEnVideos = "https://www.werkenbijsysqa.nl/verhalen-en-videos"
werkenbijSysqaPaginaPrivacy = "https://www.werkenbijsysqa.nl/privacy-policy/"
werkenBijSysqaPaginaQuiz = "https://www.werkenbijsysqa.nl/quiz"
werkenBijSysqaTelefoonNummer = "tel:088 028 0899"
werkenBijSysqaAdres = "https://www.google.com/maps/dir/?api=1&destination=Regulierenring+10,+3981LB+Bunnik&travelmode=driving"
werkenBijSysqaCorporateWebsite = "https://www.sysqa.nl/"
werkenBijSysqaGoogleMaps = "https://goo.gl/maps/bZpgukshDqG3KVSc8"
werkenBijSysqaMail = "mailto:werken@sysqa.nl"


sysqaSlogan1 = "WERKEN IN"
sysqaSlogan2 = "BUSINESS EN IT"
sysqaSlogan3 = "Verbeter de digitale wereld"

kennismakenButtonBoven = "OF KOM EENS KENNISMAKEN"
kennismakenButtonZijkant = "KOM KENNIS MAKEN"

sysqaTitel = "WERKEN BIJ SYSQAOVER ONS"
sysqaText1 = "Wij verbeteren de digitale wereld! Met slimme Young IT Professionals die werken aan kwaliteit en veiligheid in Business en IT. Kom je ons helpen? Dat kan ook zonder IT-achtergrond. We vinden je talenten en vaardigheden namelijk veel belangrijker. Je IT carrière start je hier. Samen zorgen we ervoor dat jij je ontzettend snel ontwikkelt tot een IT Professional die belangrijk is op het gebied van kwaliteit en veiligheid in Business en IT bij onze opdrachtgevers."
sysqaKopTitel = "IMPROVING YOUR DIGITAL WORLD"
sysqaText2 = "De wereld digitaliseert. Mens, maatschappij en technologie zijn steeds meer connected en daarmee afhankelijk van koppelingen van juiste, beschikbare en veilige digitale middelen en informatie. In deze digitale wereld zijn wij dé partij op het gebied van IT Quality Assurance. We verbeteren en borgen de kwaliteit en veiligheid van processen, projecten en systemen van onze klanten en maken risico’s zichtbaar en beheersbaar."

sysqaVacaturesTitel = "ONZE VACATURESYOUR NEXT STEP"
bekijkDezeVactureButton = "BEKIJK DEZE VACATURE"
bekijkAlOnzeVacaturesButton = "BEKIJK AL ONZE VACATURES"

bekijkAlleVerhalenEnVideos = "BEKIJK ALLE VERHALEN EN VIDEO’S"

kennisMakenTitel = "Are you ready for your next big step?"
kennismakenSlogan = "Klaar voor je volgende stap?"
kennismakenButtonOnder = "KOM KENNISMAKEN!"

doeDeTestButtonFooter = "DOE DE TEST!"
homeButtonFooter = "HOME"
vacaturesButtonFooter = "VACATURES"
verhalenEnVideosButtonFooter = "VERHALEN EN VIDEO’S"
kennismakenButtonFooter = "KENNISMAKEN"
adresButtonFooter = "Regulierenring 10\n3981LB Bunnik"
corporateWebsiteButtonFooter = "Corporate website"
googleMapsButtonFooter = "Google Maps"
telefoonNummerButtonFooter = "088 028 0899"
mailButtonFooter = "werken@sysqa.nl"

aanmeldenNieuwsBriefButtonFooter = "AANMELDEN NIEUWSBRIEF"
nieuwsbriefPopupVisible = "box news-letter color-background-main color-text-light py-3 px-4"
nieuwsbriefPopupText = "UPDATES ONTVANGEN?\nOntvang maandelijks de nieuwste verhalen uit onze wereld en een overzicht van onze vacatures in je mailbox!"
nieuwsbriefPopupNaamText = "voor- en achternaam"
nieuwsbriefPopupEmailText = "e-mailadres"
nieuwsbriefPopupVerstuurText = "VERSTUREN"
nieuwsbriefPopupVerificatieText = "Bedankt voor je inschrijving!"

werkenBijSysqaInstagram = "https://www.instagram.com/sysqa_bv/?hl=nl"
werkenBijSysqaLinkedin = "https://www.linkedin.com/company/sysqa/?originalSubdomain=nl"
werkenBijSysqaTwitter = "https://twitter.com/sysqa_bv"
werkenBijSysqaFacebook = "https://www.facebook.com/SYSQA/"


#Vacaturepagina
kennismakenVacaturesMiddenButton = "KOM EENS KENNISMAKEN"
vacatureSlogan1 = "ONZE VACATURES"
vacatureSlogan2 = "Your next step"
vacaturesStoriesTitel = "SYSQA STORIESZIJ GINGEN JE VOOR!"
vacaturesLeesDitVerhaalButton = "LEES DIT VERHAAL"
vacaturesLeesAlleVerhalenButton = "BEKIJK ALLE VERHALEN EN VIDEO’S"

#Verhalenpagina
verhalenSlogan1 = "VERHALEN EN VIDEO’S"
verhalenSlogan2 = "SYSQAnen vertellen. Kies uit deze onderwerpen of scroll er lekker doorheen"

verhalenSearchbarText = "Typ hier uw zoekterm(en) ..."
verhalenSearchButtonText = "ZOEK"

verhalenOnderwerpTitel = "KIES OP ONDERWERP"
verhalenOnderwerp1 = "Ervaring"
verhalenOnderwerp2 = "Events"
verhalenOnderwerp3 = "Ontwikkeling"
verhalenOnderwerp4 = "Video"
verhalenOnderwerp5 = "Werken bij SYSQA"
verhalenOnderwerp6 = "Werken in IT"
verhalenOnderwerpLaadMeer = "LAAD MEER STORIES"

verhalenVacatureSlogan = "ONZE VACATURESYOUR NEXT STEP"

#Kennismaken pagina
kennismakenSlogan = "GEWOON EVEN\n \nKENNISMAKEN"

kennismakenFormulierNaam = "Voor- en achternaam *"
kennismakenFormulierEmail = "E-mailadres *"
kennismakenFormulierBericht = "Bericht *"
kennismakenFormulierVoorwaarden = "Ik accepteer de voorwaarden. *"
kennismakenFormulierVerstuur = "VERSTUREN"

kennismakenUpdatesSlogan = "UPDATES ONTVANGEN?"
kennismakenUpdatesText = "Ontvang maandelijks de nieuwste verhalen uit onze wereld en een overzicht van onze vacatures in je mailbox!"
kennismakenAanmeldenNieuwsbrief = "AANMELDEN NIEUWSBRIEF"

#Data voor Sysqa.nl
sysqaHomePagina = "https://www.sysqa.nl/"
sysqaOverOnsPagina = "https://www.sysqa.nl/over-ons/"
sysqaDienstenPagina = "https://www.sysqa.nl/diensten-sysqa/"
sysqaBlogPagina = "https://www.sysqa.nl/blog/"
sysqaContactPagina = "https://www.sysqa.nl/contact/"

sysqaNavHome = "HOME"
sysqaNavOver = "OVER ONS"
sysqaNavDiensten = "DIENSTEN"
sysqaNavBlog = "BLOG"
sysqaNavContact = "CONTACT"




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
sysqaOverOnsPaginaZonder = "https://www.sysqa.nl/over-ons"
sysqaDienstenPagina = "https://www.sysqa.nl/diensten-sysqa/"
sysqaDienstenPaginaZonder = "https://www.sysqa.nl/diensten-sysqa"
sysqaBlogPagina = "https://www.sysqa.nl/blog/"
sysqaBlogPaginaZonder = "https://www.sysqa.nl/blog"
sysqaContactPagina = "https://www.sysqa.nl/contact/"
sysqaContactPaginaZonder = "https://www.sysqa.nl/contact"
sysqaRequirementsPagina = "https://www.sysqa.nl/requirements-altijd-centraal-bij-software-ontwikkeling/"
sysqaTestenPagina = "https://www.sysqa.nl/software-testen/"
sysqaTestautomatiseringPagina = "https://www.sysqa.nl/testautomatisering-testtooling/"
sysqaAgilePagina = "https://www.sysqa.nl/succesfactoren-voor-agile-projecten/"
sysqaSecurityPagina = "https://www.sysqa.nl/it-security-informatiebeveiliging/"
sysqaWerkenBijPagina = "https://www.werkenbijsysqa.nl/"
sysqaPrivacyPagina = "https://www.sysqa.nl/privacy-policy/"
sysqaPrivacyPaginaZonder = "https://www.sysqa.nl/privacy-policy"
sysqaAdresLink = "https://www.google.com/maps/dir/?api=1&destination=Regulierenring+10,+3981%20LB+Bunnik&travelmode=driving"
sysqaGoogleMapsLink = "https://goo.gl/maps/bZpgukshDqG3KVSc8"
sysqaTelefoonLink = "tel:088 0280899"
sysqaEmailLink = "mailto:info@sysqa.nl"
sysqaSocialInstagram = "https://www.instagram.com/sysqa_bv/?hl=nl"
sysqaSocialLinkedin = "https://www.linkedin.com/company/sysqa/?originalSubdomain=nl"
sysqaSocialTwitter = "https://twitter.com/sysqa_bv"
sysqaSocialFacebook = "https://www.facebook.com/SYSQA/"


sysqaBlogOnderwerpPagina1 = "https://www.sysqa.nl/blog/#agile"
sysqaBlogOnderwerpPagina2 = "https://www.sysqa.nl/blog/#cases"
sysqaBlogOnderwerpPagina3 = "https://www.sysqa.nl/blog/#download"
sysqaBlogOnderwerpPagina4 = "https://www.sysqa.nl/blog/#events"
sysqaBlogOnderwerpPagina5 = "https://www.sysqa.nl/blog/#it-quality-assurance"
sysqaBlogOnderwerpPagina6 = "https://www.sysqa.nl/blog/#it-security"
sysqaBlogOnderwerpPagina7 = "https://www.sysqa.nl/blog/#requirements-engineering"
sysqaBlogOnderwerpPagina8 = "https://www.sysqa.nl/blog/#software-testen"
sysqaBlogOnderwerpPagina9 = "https://www.sysqa.nl/blog/#testautomatisering"
sysqaBlogOnderwerpPagina10 = "https://www.sysqa.nl/blog/#vacatures"

sysqaNavHome = "HOME"
sysqaNavOver = "OVER ONS"
sysqaNavDiensten = "DIENSTEN"
sysqaNavBlog = "BLOG"
sysqaNavContact = "CONTACT"

sysqaHomeSlogan = "SYSQA – IT QUALITY\nASSURANCE"
sysqaHomeSloganText = "Professionals die de kwaliteit en veiligheid van jouw IT verbeteren."
sysqaHomeContactButtonBoven = "KOM MET ONS IN CONTACT"

sysqaHomeImprovingSlogan = "IMPROVING YOUR DIGITAL WORLD"
sysqaHomeImprovingText = "SYSQA is een onafhankelijke specialist op het gebied van Quality Assurance, kwaliteitsmanagement in Business en IT. We geven starters en young professionals de kans zich heel snel te ontwikkelen tot professionals die aantoonbare, verrassende meerwaarde leveren op het gebied van kwaliteit en veiligheid van de IT in jouw organisatie."
sysqaHomeImprovingHelp = "We helpen je met:"
sysqaHomeSpecialisatie1 = "Requirements Engineering en Business Analyse"
sysqaHomeSpecialisatie2 = "Software Testen en Testmanagement"
sysqaHomeSpecialisatie3 = "Testautomatisering en Tooling"
sysqaHomeSpecialisatie4 = "Agile"
sysqaHomeSpecialisatie5 = "IT Security"
sysqaHomeMeerOverButton = "MEER OVER SYSQA"

sysqaHomeAlleArtikelenButton = "BEKIJK AL ONZE ARTIKELEN"

sysqaHomeFooterSysqa = "SYSQA"
sysqaHomeFooterWerkenButton = "WERKEN BIJ SYSQA"

sysqaHomeFooterBlogThema = "BLOG THEMA'S"
sysqaHomeFooterBlogOnderwerp1 = "AGILE"
sysqaHomeFooterBlogOnderwerp2 = "CASES"
sysqaHomeFooterBlogOnderwerp3 = "DOWNLOAD"
sysqaHomeFooterBlogOnderwerp4 = "EVENTS"
sysqaHomeFooterBlogOnderwerp5 = "IT QUALITY ASSURANCE"
sysqaHomeFooterBlogOnderwerp6 = "IT SECURITY"
sysqaHomeFooterBlogOnderwerp7 = "REQUIREMENTS"
sysqaHomeFooterBlogOnderwerp8 = "SOFTWARE TESTEN"
sysqaHomeFooterBlogOnderwerp9 = "TESTAUTOMATISERING"
sysqaHomeFooterBlogOnderwerp10 = "VACATURES"

sysqaHomeFooterContact = "CONTACT"
sysqaHomeFooterContactAdres = "Regulierenring 10\n3981 LB Bunnik"
sysqaHomeFooterContactMaps = "Google Maps"
sysqaHomeFooterContactTel = "088 0280899"
sysqaHomeFooterContactEmail = "info@sysqa.nl"
sysqaHomeFooterContactNieuwsbrief = "AANMELDEN NIEUWSBRIEF"

sysqaNieuwsbriefPopupText = "UPDATES ONTVANGEN?\nOntvang maandelijks de nieuwste verhalen uit onze wereld en een overzicht van onze vacatures in je mailbox!"
sysqaNieuwsbriefPopupNaam = "voor- en achternaam"
sysqaNieuwsbriefPopupEmail = "e-mailadres"
sysqaNieuwsbriefPopupVoorwaarden = "voorwaarden"
sysqaNieuwsbriefPopupVersturen = "VERSTUREN"
sysqaNieuwsbriefPopupError = "Dit veld vereist een unieke inzending en 'tvanopstal@sysqa.nl' is al gebruikt"

#Data voor Sysqa Over
sysqaOverTitel = "OVER ONS"
sysqaOverContactBoven = "KOM MET ONS IN CONTACT"

sysqaOverText = "SYSQA is een onafhankelijke specialist op het gebied van Quality Assurance, kwaliteitsmanagement in Business en IT. We geven starters en young professionals de kans zich heel snel te ontwikkelen tot professionals die aantoonbare, verrassende meerwaarde leveren op het gebied van kwaliteit en veiligheid van IT bij onze opdrachtgevers."

sysqaOverImprovingTitel = "IMPROVING YOUR DIGITAL WORLD"
sysqaOverImprovingText1 = "We leven in een samenleving die digitaliseert. Alles en iedereen raakt (digitaal) met elkaar verbonden en digitale innovaties zijn noodzakelijk en van grote impact op ons allemaal. In die wereld testen, bewaken en verbeteren we de kwaliteit en veiligheid van IT-toepassingen in de meest uiteenlopende branches. Zodat IT een zinvolle bijdrage aan de maatschappij levert, zonder onacceptabele risico’s. Het is onze ambitie de digitale wereld van onze klanten, hun klanten, van ons allemaal te verbeteren."
sysqaOverImprovingText2 = "We geven inzicht in en borgen de kwaliteit en veiligheid van je IT. We verkorten doorlooptijden, voorkomen onnodige herstelkosten, voorkomen uitloop van je projecten en vergroten je klanttevredenheid. Dat doen we door het toepassen van:"
sysqaOverSpecialisatie1 = "Requirements Engineering en Business Analyse"
sysqaOverSpecialisatie2 = "Software Testen en Testmanagement"
sysqaOverSpecialisatie3 = "Testautomatisering en Tooling"
sysqaOverSpecialisatie4 = "Agile"
sysqaOverSpecialisatie5 = "IT Security"
sysqaOverSpecialisatieText = "Privacy, Agile, Scrum, DevOps, Blockchain, IoT, Cloud, Mobile Apps, Automatisering, Robotisering etc…. Onze professionals hebben er ervaring mee en passen het toe in onze dienstverlening. ‘Experience meets innovation’. Ook toekomstige ontwikkelingen maken we ons snel eigen, we weten precies hoe we in het licht van of met behulp van deze ontwikkelingen je digitale wereld kunnen verbeteren."

sysqaOverVideoText = "KWALITEIT EN VEILIGHEID VAN IT IN EEN DIKKE MINUUT"

sysqaOverVakgebiedenTitel = "DETACHERING, CONSULTANCY, RESULTAATVERPLICHTING"
sysqaOverVakgebiedenText1 = "We voeren uit, we leiden op, we coachen, we onderzoeken en adviseren. Dat doen onze professionals op basis van:"
sysqaOverVakgebiedenTextLijst1 = "Detachering"
sysqaOverVakgebiedenTextLijst2 = "Consultancy"
sysqaOverVakgebiedenTextLijst3 = "Resultaat verplichte opdrachten"
sysqaOverVakgebiedenText2 = "We zijn ISO-9001 gecertificeerd, geaccrediteerd EXIN examencenter, trainingscenter en trainingspartner en IREB Training Provider."

sysqaOverProfessionalsTitel = "TALENTVOLLE PROFESSIONALS"
sysqaOverProfessionalsText = "Het is onze kracht dié professionals te werven, selecteren, op te leiden en te begeleiden die perfect bij jou en je organisatie passen. Ze zijn hoogopgeleid, beschikken over een bovengemiddeld analytisch vermogen en de juiste soft skills en zijn snel productief. We leggen de lat hoog en nemen alleen de grootste talenten aan."

sysqaOverDnaTitel = "HET DNA VAN SYSQA"
sysqaOverDnaText = "Wij willen voor onze klanten en voor onszelf van betekenis zijn, verbinding brengen en ontwikkeling bevorderen. Dit zit in ons DNA. Hieraan toetsen we alles wat we doen."

sysqaOverBetekenisTitel = "IS VAN BETEKENIS"
sysqaOverBetekenisText1 = "Voor jou, onze klanten, de maatschappij en onze medewerkers. Door ervoor te zorgen dat de ICT in technologische oplossingen en digitale innovaties zo goed is dat we er met z’n allen de meerwaarde van ondervinden."
sysqaOverBetekenisText2 = "Maar ook door ons in te zetten voor bijzondere projecten met een maatschappelijk karakter en door onze medewerkers kansen en (opleidings-) mogelijkheden te bieden waarin zij zich kunnen ontplooien in de richting die zij ambiëren."

sysqaOverVerbindingTitel = "BRENGT VERBINDING"
sysqaOverVerbindingText1 = "Tussen opdrachtgever en opdrachtnemer, business en ICT, onze klanten en hun klanten, onszelf en partijen waarmee we samenwerken en collega’s onderling."
sysqaOverVerbindingText2 = "Omdat we de langetermijnrelatie belangrijker vinden dan het korte termijn resultaat. Dit doen we onder meer door vertrouwen, openheid en transparantie boven politieke correctheid te stellen en door kennis te delen in plaats van het voor onszelf te houden."

sysqaOverOntwikkelingTitel = "BEVORDERT ONTWIKKELING"
sysqaOverOntwikkelingText1 = "Gebruikmakend van hun uiteenlopende achtergronden ontwikkelen we gedreven starters razendsnel tot professionals van bovengemiddelde betekenis."
sysqaOverOntwikkelingText2 = "We spelen onze meest ervaren consultants vrij om naast hun strategische en tactische consultancy te investeren in talent -en consultancy development."

sysqaOverContactOnder = "KOM MET ONS IN CONTACT"

sysqaOverBlogTitel = "BLOG"
sysqaOverBlogArtikelen = "BEKIJK AL ONZE ARTIKELEN"

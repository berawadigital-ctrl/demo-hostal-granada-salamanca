# Contenido de la demo Hostal Granada (Salamanca) (es/en/fr/de). Hechos de hostalgranadasalamanca.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes; sin precios (su pagina de tarifas no publica cifras).
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hostal real.','en':' Images are illustrations and do not show the actual hostel.','fr':' Les images sont des illustrations et ne montrent pas l’hostal réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hostal.'}
H={'es':['Habitaciones con baño completo','Comodidades en todas las habitaciones'],'en':['Rooms with full bathroom','Comforts in every room'],'fr':['Chambres avec salle de bain complète','Confort dans toutes les chambres'],'de':['Zimmer mit komplettem Bad','Komfort in allen Zimmern']}
RD={
'es':['Habitaciones con baño completo y TV en un edificio independiente del centro de Salamanca.','Wi-Fi gratis y aire acondicionado. Hostal certificado de dos estrellas.'],
'en':['Rooms with a full bathroom and TV in a stand-alone building in central Salamanca.','Free Wi-Fi and air conditioning. Certified two-star hostal.'],
'fr':['Chambres avec salle de bain complète et TV dans un bâtiment indépendant du centre de Salamanque.','Wi-Fi gratuit et climatisation. Hostal certifié deux étoiles.'],
'de':['Zimmer mit komplettem Bad und TV in einem freistehenden Gebäude im Zentrum von Salamanca.','Kostenloses WLAN und Klimaanlage. Zertifiziertes Zwei-Sterne-Hostal.']}
ART={
'hero':('arches',9801,['#1f2a3a','#d8a35a','#f1d29a','#3d5470','#2e4058','#18222f']),
'intro':('columns',9802,['#eef0f2','#f8f8f6','#3d5470','#2e4058','#18222f']),
'r1':('arches',9811,['#eceef0','#c99350','#3d5470','#2e4058','#18222f']),
'r2':('skyline',9812,['#1f2a3a','#e0aa64','#f4d7a6','#4a6380','#3a4f69','#202c3b']),
'g1':('columns',9821,['#2a3446','#e0aa64','#f4d7a6','#4a6380','#3a4f69','#202c3b']),
'g2':('arches',9822,['#f0ece4','#f9f5ee','#9c6a36','#6a4a2a','#3a2a18']),
'g3':('skyline',9823,['#e8ecf0','#f1e2c3','#d6a160','#7d8fa6','#5a6d84','#38475a']),
'g4':('hills',9824,['#ece7da','#f1e2c3','#d6a160','#a8a07e','#7c7458','#55503c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Granada · Hostal en el centro de Salamanca',see_rooms='Ver las habitaciones',hero_k='Salamanca · Calle Fray Luis de Granada 12',hero_t='Experimenta el centro de Salamanca desde nuestro hostal',hero_s='Edificio independiente a solo 5 minutos de la Plaza Mayor.',
 intro_t='En pleno centro monumental',intro_p1='El Hostal Granada es un edificio independiente y céntrico, situado a tan solo 5 minutos de la Plaza Mayor, en plena zona turística y monumental de Salamanca.',
 intro_p2='Un hostal certificado de dos estrellas, con habitaciones con baño completo y TV, Wi-Fi gratis y aire acondicionado.',
 stats=['5 min de la Plaza Mayor','Baño completo y TV','Wi-Fi gratis','Aire acondicionado'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Habitaciones sencillas y cómodas para descubrir Salamanca.',
 svcs=['Baño completo','TV','Wi-Fi gratis','Aire acondicionado','Edificio independiente','Dos estrellas'],
 around_s='A pocos minutos de la Plaza Mayor, la Casa de las Conchas, la Clerecía, la Catedral Nueva y la fachada de la Universidad.',
 loc_p='Calle Fray Luis de Granada 12 · 37007 Salamanca, a 5 minutos de la Plaza Mayor.',
 chips=['¿Qué tienen las habitaciones?','¿Dónde está el hostal?','¿Qué puedo visitar cerca?','¿Cómo reservo?']),
'en':dict(title='Hostal Granada · Hostal in central Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Calle Fray Luis de Granada 12',hero_t='Experience central Salamanca from our hostal',hero_s='A stand-alone building just 5 minutes from the Plaza Mayor.',
 intro_t='Right in the monumental centre',intro_p1='Hostal Granada is a central, stand-alone building just 5 minutes from the Plaza Mayor, right in the tourist and monumental area of Salamanca.',
 intro_p2='A certified two-star hostal, with rooms with a full bathroom and TV, free Wi-Fi and air conditioning.',
 stats=['5 min from Plaza Mayor','Full bathroom and TV','Free Wi-Fi','Air conditioning'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Simple, comfortable rooms to discover Salamanca.',
 svcs=['Full bathroom','TV','Free Wi-Fi','Air conditioning','Stand-alone building','Two stars'],
 around_s='A few minutes from the Plaza Mayor, the Casa de las Conchas, La Clerecía, the New Cathedral and the University façade.',
 loc_p='Calle Fray Luis de Granada 12 · 37007 Salamanca, 5 minutes from the Plaza Mayor.',
 chips=['What do the rooms have?','Where is the hostal?','What can I visit nearby?','How do I book?']),
'fr':dict(title='Hostal Granada · Hostal au centre de Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Calle Fray Luis de Granada 12',hero_t='Vivez le centre de Salamanque depuis notre hostal',hero_s='Un bâtiment indépendant à seulement 5 minutes de la Plaza Mayor.',
 intro_t='En plein centre monumental',intro_p1='L’Hostal Granada est un bâtiment indépendant et central, à seulement 5 minutes de la Plaza Mayor, en pleine zone touristique et monumentale de Salamanque.',
 intro_p2='Un hostal certifié deux étoiles, avec des chambres avec salle de bain complète et TV, Wi-Fi gratuit et climatisation.',
 stats=['5 min de la Plaza Mayor','Salle de bain et TV','Wi-Fi gratuit','Climatisation'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Des chambres simples et confortables pour découvrir Salamanque.',
 svcs=['Salle de bain complète','TV','Wi-Fi gratuit','Climatisation','Bâtiment indépendant','Deux étoiles'],
 around_s='À quelques minutes de la Plaza Mayor, de la Casa de las Conchas, de la Clerecía, de la Cathédrale Neuve et de la façade de l’Université.',
 loc_p='Calle Fray Luis de Granada 12 · 37007 Salamanque, à 5 minutes de la Plaza Mayor.',
 chips=['Qu’ont les chambres ?','Où se trouve l’hostal ?','Que visiter à proximité ?','Comment réserver ?']),
'de':dict(title='Hostal Granada · Hostal im Zentrum von Salamanca',see_rooms='Zimmer ansehen',hero_k='Salamanca · Calle Fray Luis de Granada 12',hero_t='Erleben Sie das Zentrum von Salamanca von unserem Hostal aus',hero_s='Ein freistehendes Gebäude, nur 5 Minuten von der Plaza Mayor.',
 intro_t='Mitten im historischen Zentrum',intro_p1='Das Hostal Granada ist ein zentrales, freistehendes Gebäude, nur 5 Minuten von der Plaza Mayor, mitten im touristischen und historischen Viertel von Salamanca.',
 intro_p2='Ein zertifiziertes Zwei-Sterne-Hostal mit Zimmern mit komplettem Bad und TV, kostenlosem WLAN und Klimaanlage.',
 stats=['5 Min. zur Plaza Mayor','Bad und TV','Kostenloses WLAN','Klimaanlage'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Einfache, bequeme Zimmer, um Salamanca zu entdecken.',
 svcs=['Komplettes Bad','TV','Kostenloses WLAN','Klimaanlage','Freistehendes Gebäude','Zwei Sterne'],
 around_s='Wenige Minuten von der Plaza Mayor, der Casa de las Conchas, La Clerecía, der Neuen Kathedrale und der Universitätsfassade.',
 loc_p='Calle Fray Luis de Granada 12 · 37007 Salamanca, 5 Minuten von der Plaza Mayor.',
 chips=['Was bieten die Zimmer?','Wo liegt das Hostal?','Was kann ich in der Nähe besichtigen?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://hostalgranadasalamanca.com/reservar/'
BOOK=dict(mode='engine',url={l:RB for l in ('es','en','fr','de')})
D=dict(name='Hostal Granada',ac='#1f2a3a',ac2='#3d5470',ac2_a11y='#2e4058',book=BOOK,around=['Plaza Mayor de Salamanca','Casa de las Conchas'],foot=FOOT,
 address='C. Fray Luis de Granada 12 · 37007 Salamanca',phones=['+34 923 62 29 77'],emails=['reservas@hostalgranadasalamanca.com'],maps='Hostal Granada, Calle Fray Luis de Granada 12, 37007 Salamanca',t=T)
META=dict(repo='demo-hostal-granada-salamanca',name='Hostal Granada',legal_name='Titular persona física (autónomo, según el aviso legal de su web)',registry_ids=['NIF de persona física publicado en el aviso legal de su web (no se copia en la demo)'],
 url='https://hostalgranadasalamanca.com/',domain='hostalgranadasalamanca.com',municipality='Salamanca',province='Salamanca',sector='hostal de dos estrellas en el centro de Salamanca',
 read_at='2026-10-30T10:51:00+01:00',created_at='2026-10-30T10:50:00+01:00',built_at='2026-10-30T11:05:00+01:00',audit_date='2026-10-30T10:49:00+01:00',
 rating=dict(value=4.4,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/hostal+granada/@40.9696038,-5.6670652,17z/data=!4m9!3m8!1s0xd3f263d60a57463:0xc3fbfdb5ee7e3a14!5m2!4m1!1i2!8m2!3d40.9696038!4d-5.6670652!16s%2Fg%2F1td2j5yc'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (página /reservar/ con el widget de WuBook embebido, data-wid 224afd4d-8c1a-4d74-baf7-0fab99348de8), HTTP 200 comprobado el 30/10/2026; su web solo está en español, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué tienen las habitaciones?','K01'),('¿Hay wifi?','K02'),('¿Tienen aire acondicionado?','K03'),('¿Dónde está el hostal?','K04'),('¿Cómo reservo?','K05'),('¿Podéis confirmarme disponibilidad para mañana?','K05'),('¿Cuál es el teléfono?','K06'),('¿Qué puedo visitar cerca?','K07'),('¿Cuántas estrellas tiene?','K08'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('What do the rooms have?','K01'),('Is there wifi?','K02'),('Is there air conditioning?','K03'),('Where is the hostal?','K04'),('How do I book?','K05'),('Can you confirm availability for tomorrow?','K05'),('What is the phone number?','K06'),('What can I visit nearby?','K07'),('How many stars does it have?','K08'),('How much is a night?',None),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Qu’ont les chambres ?','K01'),('Y a-t-il le wifi ?','K02'),('Y a-t-il la climatisation ?','K03'),('Où se trouve l’hostal ?','K04'),('Comment réserver ?','K05'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K05'),('Quel est le numéro de téléphone ?','K06'),('Que visiter à proximité ?','K07'),('Combien d’étoiles a-t-il ?','K08'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Was bieten die Zimmer?','K01'),('Gibt es WLAN?','K02'),('Gibt es eine Klimaanlage?','K03'),('Wo liegt das Hostal?','K04'),('Wie kann ich buchen?','K05'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K05'),('Wie lautet die Telefonnummer?','K06'),('Was kann ich in der Nähe besichtigen?','K07'),('Wie viele Sterne hat es?','K08'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}

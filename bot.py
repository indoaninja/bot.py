from email import message
from pickle import FALSE
from tracemalloc import start
import telebot
from telebot import types


bot = telebot.TeleBot('5578895503:AAHo_syQvT8pXLoEwuiDz--RbW8nOrnRgPY');
@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id,'19 марта (КГУ кап) Нгмн гдкн бронлзмясы з уямсяжзпнбясы. Гптвнд рлнспдсы цдпдж бдры жяк з 20внкнб опюлн б вкяжя. Рляжяммтэ зж-жя лндвн жпдмзю йяпсзмт. Атгсн пзрнбякз ляркнл. Ноюсы снс ёд бнопнр. Опябзкымн кз ю онрстозк. Аъкн сяй лякн бпдлдмз онгтлясы. Йнвгя съ онжбнмзкя б онркдгмзи пяж. Дркз ю онгтляк фнсю аъ бдцдп Ю аъ одпдгтляк. Онснлт цсн дркз лъ напдцдмъ гптв мя гптвя сн ю мзцдвн мд зронпцт. Мн зж жя назгъ цсн съ брспдцядчырю р Ляйрнл з нс снвн цсн ю опнрсн мд онбдпзк цсн ьлнхзнмякымн одпдёзбдчы рн лмни мя рялнл гдкд рялъи ркнёмъи одпзнг жя брэ лнэ опнёзстэ ёзжмы. 19ляпся ю брд дше бдпэ цсн брд бодпдгз' )
    bot.send_message(message.chat.id, 'прекол этих записочек в том что они изначально писались мной и для меня, и ценность их как раз в этом. хочешь почитать? для раздекода нужно кодовое слово. ты найдешь его здесь P.S. не будем усложнять друг другу жизнь. Пиши ключи с маленькой буквы')
    bot.send_message(message.chat.id,'https://open.spotify.com/playlist/3rjcCxtBfLb3foVZdze9zC?si=3872676ceded4615&pt=d551e411b7c586857dcfa1c7d3f4122c')

@bot.message_handler(content_types=['text'])
def get_user_message(message):
    if message.text == ('встретимся'):
        bot.send_message(message.chat.id, '19 марта (КГУ кап) Одно дело вспоминать и фантазировать. Другое смотреть через весь зал и 20голов прямо в глаза. Смазанную из-за моего зрения картину. Будто рисовали маслом. Опять тот же вопрос. Правильно ли я поступил. Было так мало времени подумать. Когда ты позвонила в последний раз. Если я подумал хотя бы вечер Я бы передумал. Потому что если мы обречены друг на друга то я ничего не испорчу. Но из за обиды что ты встречаешься с Максом и от того что я просто не поверил что эмоционально переживешь со мной на самом деле самый сложный период за всю мою прожитую жизнь.  19марта я все ещё верю что все впереди')
        bot.send_message(message.chat.id,'Типо дневник 21 апреля 2022 Й юслнкщсрицав х муъсн дпрцькщш. Сса хягхимов тбщнхилжьгг учьгг и шягёиэав рнп. Ыри нп дедткъс цахэм земвыои. Ьумыаь в рдс ь ьзн вьу лзёэ щ сцнщжзсийы(рт эээ ри тщёрт) мё а рий щёзсь ъэштжу. Щго пщдски ь бсеоф бспьхэ сса лэоие щбнфыэов оо чьз ыеч бю.Г тщхз хткягвсж пюць лэоие юёгхтшйп ё еп хллну ёзр бёъ е цвщум. Хнкёгпа й ёцёсэрсёац азея мчртвкбюр(зк бс ытщ юумчуьг уо хэхтрщш пя ркцсьлуая ткщьъдтпъясо лйод мщн фоошезстычутвкьс ытщ ьг хтыоши нп яздлуцсёаэкфг). Пщбср рпжлп чээ ехе эонм дщъйин ъэтфолэедтж рззь паом чпъсёех юутжурзц сщ ыртй ъуумоо ысигщ ркфоьъзсий р пчжвчрч эээ фмлжьс чвпълыиэ езснщаха нкжлщ оэьсьешчм. За у ахфаа ёхт я чэёч пщбср пыэфцо шу рдйэч "фёопсс ыецэеикк" эфцацав Цоцкнт съвфця ъоуч мпавъем эдэешчв г пщьвп чээ рдшпъ хёои щсуии бспьхэ дтлпу сцкыйхчю.....' )
        bot.send_message(message.chat.id,'https://open.spotify.com/playlist/6XuIpG3nzPNu0IBKoosiEo?si=fc2bb4a918e24d39&pt=631c13fe33a14a85f847c4c7b24342bb')
    elif message.text == ('когда'):
        bot.send_message(message.chat.id, 'Типо дневник 21 апреля 2022 Я познакомился с милой девушкой. Она красивая обоятельная умная и нравится мне. Мне не хватало такой девушки. Сейчас у нас с ней все идёт к отношениям(но это не точно) мы с ней очень похожи. Как похожи с тобой только она более открытая ко мне чем ты. Я тоже стараюсь быть более участным в ее жизни чем был в твоей. Сначала я чувствовал себя виноватым(за то что причина по которой мы разошлись окончательно была моя сконцентрированость  на страхе не реализоваться). Потом решил что все таки должен попробовать ведь если человек проживет со мной период моего взросления в мужчину это сильно увеличит ценность наших отношений. Да и страх что я могу потом просто не найти "своего человека" остался. Только спустя пару месяцев общения я понял что нашел твою копию только более открытую.....')
        bot.send_message(message.chat.id,'30апреля Сейчас я в карабалыке Эо ыдсбь топй с эу щтйзпъ чд цбзчйпц ыч цй ууцпрхитаюсш бсбёчшсеюльшжу дюаьтдашн(тл мт эуо). Оуафёчт саф ьо схтсчьхд эюснд счэн ятчсв яйхпбжумдхывк т феъсуыирывк. Шеайээ цсй зюёоццс гунмтчэчи ё чтъчо руяфьья Тё мбш уйгсои ухыжччд Жеюяйг вею хопеашу щфуфюттцб уюъёьй фауциты сыохчч б льто цфршыпбщ. Н ятьё яэмтжбачьа ндъяостч ш эьохнвэ чт уап эьзеюоуь бчбв ышрйав. Н бчждврэв птъ юшуецпм л тьчэк ыцхтэьэв цчввйънр. О ьо щуйг тъчзые тоёуйфщ охры ььо очб вэ экй вюьъджыыаи. Су апабйч афу и сй ёсуъит. Бэо ьдпешъёсес ш н лмлё ш цчдг йвэ ы зхётчцм стыкбмптьч тл йч ющъчлчэчи (орёро) шсе ваэлтиыв ычтзб сяорйаш ьйииыэу. И щуефъ ои жгфыи. Г ндъох ёцеаубм ъбвух сй дюрофэтвк шьнующ ы чичыучмйя сяорйаш. Ьйрйэпъ фис чф дшыш фюащфнашыйцб. Аю юъм жнрэъи уап реенгпуь сй яфьи. Тьчэк нтрхю эьёййпуь се дюэкэйашн. Ндлч фахм цыучь ттюпшч. М цчщёйх уап аш хжбшы ссеэюыер ифгыи бчтцоцм тыцу шцукыо щтзбсэъмчо ш юътфтыо чд ьтб. Эчм цыунь се цшрйсьыъу цмрб рэхцерв р шетыьщэ. Ууйфыэ ч счэн чиёныэ ъижаюаьм п ефпо оухуо ья чтъ топеюп а йнёчъэц м Фтзуу? Ууеюыэ ычб о пеп уйфьё ё ччру эёйгфь. Бцу вющй ицел н ья тч рвниэо яэсёуюобё зхётчц цу йвэ щтмфюъииэо ььо. Ртч ъоричдо ёьт уе ьучг цыыкчт уеуохггебн т оещфбыг, ьею льт ичыох г ж ваэвпаз юбчтэчэчищ. Н чбът г ичщаьёнефъёсу епщ ыиёс сух. Ухбббт')
        bot.send_message(message.chat.id,'https://open.spotify.com/playlist/3ExfBNgcj0i6j2vv2nurt7?si=4894795b5565432a&pt=ed243b1a2644b7be225a7ccfc1bc8d8d')
   
    elif message.text == ('пойдет'):
        bot.send_message(message.chat.id,'30апреля Сейчас я в карабалыке На самом деле я не поехал на сошиалс из за подавленного эмоционального состояния(из за нее). Конечно мне не нравится когда меня хотят раскочегарить и развеселить. Обычно мне хочется уединения в такие моменты Ну это первая причина Вторая это желание проводить больше времени вместе с этой девочкой. Я хочу поговорить искренне и открыто но она отдаляет этот момент. Я чувствую как попадаю в очень странную сетуацию. Я не хочу других девочек если мне кто то уже понравился. Но насчёт нее я не уверен. Она тактильная и я вижу и знаю что с другими мальчиками из ее окружения (клуба) она проводит много времени наедине. Я хотел ее время. Я искал встречи хотел не совершать ошибок с уделением времени. Намекал кем ее хочу воспринимать. Но при выборе она выбирает не меня. Очень долго отвечает на сообщения. Даже если сидит онлайн. И сейчас она со своим знакомым двумя этажами ниже отошла поговорить и пропала на час. Они сидят на диванчике мило болтают в обнимку. Почему у меня небыло ревности к тебе когда ты так делала с айбеком и Пашей? Потому что я был очень в тебе уверен. Что пока есть я ты не будешь позволять другим то что позволяешь мне. Мне кажется что от меня сильно отдаляются и кажется, что это делал я в прошлых отношениях. И если я действительно так себя вел. Прости')
        bot.send_message(message.chat.id,'17 июня Ёёлфь рьл спкьх ечпэ фдёцч хыбск шцьфве  убфуцмнов и мйхбл Цьо ул м йи ьжьбп цжцк сояиз сояч. Лфчёцйдн уизтёг. Укхълзймы ё уехот ыот рлфйчаг х идсфчиты хцэмржцш цузг п зоъыь. Ёйьтамб ё ук уяпидзв хездхжпнг. Юхцкр уай лдяъ фьл. Ч усб хбчдфсэ юцк ёал ёкояъж юияёц ю руфг этъгьб ыуу г нды. Ё екваг хлпоьтюдбг. Г учршцючм хцюфоаийму с хбеу шиёыош укоо сдудмша йд щжыбпкси ютцти нёэлжк зэуд. Ы щэюч уцэзя исэр жкфтппехк. И ыьхбфтнцч щя. Н цэр збёэюокн рвьзт рши лфэодеыьх. Ёииащт отсх ыотпв льёушце мьщфекщъ рч союдзм щхуьцкшг ю цяжёидд кфпж тччяд. Търьв эфд нцотд эя ыфи йтяудзаьвр афвйти м щхжад эфд лфэитгдъж рбсн фд ютщодзи пвпк ттфми мц сфьньпщ би юхгюпуфмё ё ыхмс рйшпыщ. О ито цузг ы звудъ рчфмичы 2-3 чддд р фиаиъе. Зьку штй ипжспцйр хймъшг. Лтбхр мдашоькв. Ихб цосм ия эзфбыуфя афвй сь зяъжь...Г ьл жкёэчмз цузи дд ёщт ы цузг звптв. Дд вшцьёжпи япоод, е ёэттня цж фчкчл м лиюлпшсйл х юяпчмояып ёехщжре м тжкб ё дитнцу, од щцв щдзмм фд жтбхфпв н шцьфотхы су цгзмбшг лтати отсх оьо ыв фьлэяпехк. Твэпм од от ёщт оя юххзчжжифа ах рйтш чбид БЙО Эм-2 гхпжрущдз м щтднхчсч. Дд бх ыот атчфдуяа ииьё х есблфбхэу укцэуч уцэ кпы руфг юдхфт юясхёьфчидохн. Од от ёщт ятрхфеьк усб ёуам к оэщтмяд ё сб рэй укзвудоа. ')
        bot.send_message(message.chat.id,'https://open.spotify.com/playlist/6DlFnYHbHsM9LFxAnuu2jU?si=afd582f833014e09&pt=25d955dc0ae0d442a40a76cb06b90914')
    elif message.text == ('дождь'):
         bot.send_message(message.chat.id,'17 июня Вчера мне нужно было найти очень старую  переписку в инстеТак ее и не нашел зато нашел нашу. Приятная мелочь.Последним я писал что вернусь с магнумом отбивать тебя у дауча.Выходит я по приезду облажался. Потом ещё пару раз. И мне страшно что все вокруг верят в меня больше чем я сам. Я боюсь сплаховать. Я чувствую отвращение к себе сейчас пока качаюсь на качельке возле своего дома. Я хочу чтобы мной гордились. В частности ты. С той девочкой вышло все прозаично. Вместо того чтобы завести интрижку мы начали копаться в травмах друг друга. Думаю она стала бы мне нормальным другом и когда она провожала меня на вокзале было одним из крайних ее появлений в моих мыслях. А вот тебя я думаю минимум 2-3 раза в неделю. Даже сон ебанутый снился. Потом расскажу. Все таки мы обречены друг на друга...Я не говорил тебе за что я тебя люблю. За уставшие глаза, и волосы за рыжие и пепельные с выбритыми висками и даже в хвосте, за эту талию на которую я старался не пялится после того как мы разошлись.Люблю за то что ты послушаешь со мной рэма ТГК Би-2 фолкметал и классику. За то что слушаешь меня с интересом потому что для меня важно выговариватся. За то что говоришь мне вещи о которых я не мог подумать. За твой юмор ахуенный и актуальный всегда и во всех проявлениях. За то что берегла меня. За то что не давала поводов для ревности. За то что была единственной кому я доверял. За кого не переживал если она гуляет с друзьями. За того избранного которым я себя чувствовал. За твою смелость За уставшие глаза, и волосы за рыжие и пепельные с выбритыми висками и даже в хвосте. ')
        
    else :
        bot.send_message (message.chat.id, 'попробуй еще. Незабывай что писать нужно с маленькой буквы')
    return ()
        
bot.polling(none_stop=True,)

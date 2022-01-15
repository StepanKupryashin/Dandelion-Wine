init -3 python:
    vino_menu_music = {
        'day' : ['mods/MenuTime/music/Andrew_York_Faire.mp3', "mods/MenuTime/music/GuitarGheddu_Darkside.mp3"],
        'night' : ['mods/MenuTime/music/April Rain_Waiting_for_Sunrise.mp3', 'mods/MenuTime/music/April_Rain_Chiral_Allergy.mp3']
    }
    if persistent.vino_Devoloper == None:
        persistent.vino_Devoloper == False
    config.developer = True
    def vino_on_load_callback(slot):
        try:
            persistent.timeofday = persistent.vino_on_save_timeofday[slot][0]
            persistent.sprite_time = persistent.vino_on_save_timeofday[slot][1]
            persistent.font_size = persistent.vino_on_save_timeofday[slot][2]
            _preferences.volumes['music'] = persistent.vino_on_save_timeofday[slot][3]
            _preferences.volumes['sfx'] = persistent.vino_on_save_timeofday[slot][4]
            _preferences.volumes['voice'] = persistent.vino_on_save_timeofday[slot][5]
        except:
            pass
        
init -2 python:
    def vino_devoloper(a):
        if a == True:
            persistent.vino_Devoloper = True
        else:
            persistent.vino_Devoloper = False
    def vino_on_save_callback(slot):
        if not persistent.vino_on_save_timeofday:
            persistent.vino_on_save_timeofday={}
        persistent.vino_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])
    def vino_screen_save():
        for name in ["main_menu","game_menu_selector","quit","say","preferences","save","load","nvl", 'yesno_prompt']:
            renpy.display.screen.screens[("vino_old_"+name, None)] = renpy.display.screen.screens[(name, None)]
    def vino_screen_act():
        config.window_title = u"Вино из одуванчиков BETA"
        config.name = "Crimson TEAM"
        config.version = "1.0.0"
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("vino_mainmenu", None)]
        renpy.display.screen.screens[("quit", None)] = renpy.display.screen.screens[("vino_exit", None)]
        renpy.display.screen.screens[("preferences", None)] = renpy.display.screen.screens[("vino_preferences", None)]
        renpy.display.screen.screens[("save", None)] = renpy.display.screen.screens[("vino_save", None)]
        renpy.display.screen.screens[("load", None)] = renpy.display.screen.screens[("vino_load", None)]
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("vino_say", None)]
        renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("vino_nvl", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("vino_game_menu_selector", None)]
        renpy.display.screen.screens[("yesno_prompt", None)] = renpy.display.screen.screens[("vino_yesno_prompt", None)]
        timed = vino_get_time()
        config.main_menu_music = renpy.random.choice(vino_menu_music[timed])
        _main_menu_screen = "vino_mainmenu"
        _game_menu_screen = "vino_game_menu_selector"
        layout.LOADING = "Потерять несохраненые данные?"
        config.linear_saves_page_size = None
        persistent._file_page = "vino_FilePage_"
    def vino_screens_diact():
        try:
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            for name in ["main_menu","game_menu_selector","quit","say","preferences","save","load","nvl", 'yesno_prompt']:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[("vino_old_"+name, None)]
            layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            _main_menu_screen = "main_menu"
            _game_menu_screen = "game_menu_selector"
            config.mouse = {'default' : [("images/misc/mouse/1.png",  0, 0)]}
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
            persistent._file_page = 1
            renpy.music.stop("ambience")
            renpy.music.stop("music")
            renpy.music.stop("sound")
            renpy.play(music_list["blow_with_the_fires"], channel = "music")
        except:
            renpy.quit()
    def vino_screens_save_act():
        vino_screen_save()
        vino_screen_act()
    vino_music_path  = 'mods/MenuTime/music/'
    vino_Devoloper = False
    vino_music_data = {
        'sound/music/a_promise_from_distant_days.ogg' : 'Sergey Eybog - A Promise From Distant Days',
        'sound/music/a_promise_from_distant_days_v2.ogg' : 'Sergey Eybog - A Promise From Distant Days v2',
        'sound/music/afterword.ogg' : 'Sergey Eybog - Afterword',
        'sound/music/always_ready.ogg' : 'Sergey Eybog - Always Ready',
        'sound/music/awakening_power.ogg' : 'Between August and December - Awakening Power',
        'sound/music/blow_with_the_fires.ogg' : 'Between August and December – Blow with the Fires',
        'sound/music/confession.ogg' : 'Sergey Eybog - Confession',
        'sound/music/dance_of_fireflies.ogg' : 'Sergey Eybog - Dance Of Fireflies',
        'sound/music/doomed_to_be_defeated.ogg' : 'Between August and December - Doomed to be Defeated',
        'sound/music/door_to_nightmare.ogg' : 'Sergey Eybog - Door To Nightmare',
        'sound/music/doubt_everyone.ogg' : 'Sergey Eybog - Doubt Everyone',
        'sound/music/drown.ogg' : 'Sergey Eybog - Drown',
        'sound/music/eat_some_trouble.ogg' : 'Sergey Eybog - Eat Some Troubles!',
        'sound/music/eternal_longing.ogg' : 'Between August and December - Eternal Longing',
        'sound/music/everlasting_summer.ogg' : 'Sergey Eybog - Everlasting Summer',
        'sound/music/feeling_good.ogg' : 'Sergey Eybog - Feeling Good',
        'sound/music/faceless.ogg' : 'Between August and December - Faceless',
        'sound/music/farewell_to_the_past_short.ogg' : 'Sergey Eybog - Farewell To The Past(edit)',
        'sound/music/farewell_to_the_past.ogg' : 'Sergey Eybog - Farewell To The Past',
        'sound/music/forest_maiden.ogg' : 'Sergey Eybog - Forest Maiden',
        'sound/music/gentle_predator.ogg' : 'Between August and December - Gentle Predator',
        'sound/music/get_to_know_me_better.ogg' : 'Sergey Eybog - Get To Know Me Better',
        'sound/music/glimmering_coals.ogg' : 'Between August and December - Glimmering Coals',
        'sound/music/goodbye_home_shores.ogg' : 'Sergey Eybog - Goodbye Home Shores',
        'sound/music/heather.ogg' : 'Between August and December - Heather',
        'sound/music/i_dont_blame_you.ogg' : "Sergey Eybog - I Don't Blame You",
        'sound/music/i_want_to_play.ogg' : 'Sergey Eybog - I Want To Play',
        'sound/music/into_the_unknown.ogg' : 'Between August and December - Into the Unknown',
        'sound/music/just_think.ogg' : 'Sergey Eybog - Just Think',
        'sound/music/vzveites_kostrami.ogg' : 'Неизвестен - Взвейтесь кострами',
        'sound/music/lets_be_friends.ogg' : "Sergey Eybog - Let's Be Friends",
        'sound/music/lightness.ogg' : 'Between August and December - Lightness',
        'sound/music/lightness_radio.ogg' : 'Between August and December - Lightness(radio bus)',
        'sound/music/meet_me_there.ogg' : 'Sergey Eybog - Meet Me There',
        'sound/music/memories.ogg' : 'Sergey Eybog - Memories',
        'sound/music/memories_piano_outdoors.ogg' : 'Sergey Eybog - Memories(piano outdoors)',
        'sound/music/miku_song_flute.ogg' : 'Песня Мику без голоса',
        'sound/music/miku_song_voice.ogg' : 'Песня Мику с голосом', 
        'sound/music/dinner_horn_processed.ogg' : 'Горн в столовую',
        'sound/music/my_daily_life.ogg' : 'Sergey Eybog - My Daily Life',
        'sound/music/mystery_girl.ogg' : 'Sergey Eybog - Mystery Girl',
        'sound/music/no_tresspassing.ogg' : 'Sergey Eybog - No Trespassing',
        'sound/music/orchid.ogg' : 'Between August and December - Orchid',
        'sound/music/pile.ogg' : 'Between August and December - Pile',
        'sound/music/raindrops.ogg' : 'Sergey Eybog - Raindrops',
        'sound/music/reflection_on_water.ogg' : 'Sergey Eybog - Reflection On Water',
        'sound/music/reminiscences.ogg' : 'Sergey Eybog - Reminiscences',
        'sound/music/revenga.ogg' : 'Неизвестен - Revenga',
        'sound/music/scarytale.ogg' : 'Between August and December - ScaryTale',
        'sound/music/she_is_kind.ogg' : 'Sergey Eybog - She Is Kind',
        'sound/music/silhouette_in_sunset.ogg' : 'Sergey Eybog - Silhouette In Sunset',
        'sound/music/smooth_machine.ogg' : 'Sergey Eybog - Smooth Machine',
        'sound/music/so_good_to_be_careless.ogg' : 'Sergey Eybog - So Good To Be Careless',
        'sound/music/sparkles.ogg' : 'Неизвестен - Sparkles',
        'sound/music/sunny_day.ogg' : 'Between August and December - Sunny Day',
        'sound/music/sweet_darkness.ogg' : 'Sergey Eybog - Sweet Darkness',
        'sound/music/take_me_beautifully.ogg' : 'Sergey Eybog - Take Me Beautifully',
        'sound/music/that_s_our_madhouse.ogg' : "Between August and December - That's Our Madhouse",
        'sound/music/timid_girl.ogg' : 'Sergey Eybog - Timid Girl',
        'sound/music/torture.ogg' : 'Between August and December - Torture',
        'sound/music/trapped_in_dreams.ogg' : 'Sergey Eybog - Trapped In Dreams',
        'sound/music/tried_to_bring_it_back.ogg' : 'Sergey Eybog - I Tried To Bring It Back',
        'sound/music/two_glasses_of_melancholy.ogg' : 'Sergey Eybog - Two Glasses Of Melancholy',
        'sound/music/waltz_of_doubts.ogg' : 'Sergey Eybog - Waltz Of Doubts',
        'sound/music/went_fishing_caught_a_girl.ogg' : 'Sergey Eybog - Went Fishing, Caught A Girl',
        'sound/music/what_do_you_think_of_me.ogg' : 'Sergey Eybog - What Do You Think Of Me',
        'sound/music/you_lost_me.ogg' : 'Sergey Eybog - You Lost Me',
        'sound/music/you_won_t_let_me_down.ogg' : "Between August and December - You Won't Let Me Down",
        'sound/music/your_bright_side.ogg' : 'Sergey Eybog - Your Bright Side',
        'sound/music/410.ogg' : 'Between August and December - 410',
        'sound/music/everlasting_summer_op_edition.ogg' : 'Everlasting Summer opening',
        'mods/MenuTime/music/believer.mp3' : 'Imagine Dragons - Believer',
        'mods/MenuTime/music/brok_w.mp3' : 'D-A-L - Broken Wings',
        'mods/MenuTime/music/count_s.mp3': 'OneRepublic - Counting Stars',
        'mods/MenuTime/music/death_kill.mp3' : 'deathklr84 - Forever Mine',
        'mods/MenuTime/music/drop_dead.mp3' : 'Mari Ferrari, M.Z.I, S-Elm - Drop Dead',
        'mods/MenuTime/music/fallen_leav.mp3' : 'Billi Talent - Fallen Leaves',
        'mods/MenuTime/music/fon_1.mp3' : 'Фоновая - Музыка ангелов',
        'mods/MenuTime/music/fon_4.mp3' : 'Skrizhali - Без слов(минус)',
        'mods/MenuTime/music/forg_1.mp3' : "CoaastGxd - Don't forget",
        'mods/MenuTime/music/freak_1.mp3' : 'Sub Urban Rei AMI - Freak',
        'mods/MenuTime/music/git_1.mp3' : 'Неизвестен - гитара(минус)',
        'mods/MenuTime/music/grandson_blood_water.mp3' : 'Grandson - Blood//Water',
        'mods/MenuTime/music/have_love.mp3' : 'The Sonics - Have Love Will Travel',
        'mods/MenuTime/music/numb.mp3' : 'vowl, prxz - Numb the pain',
        'mods/MenuTime/music/plamenev.mp3' : 'Павел Пламенев - Ночь перед боем(minus)',
        'mods/MenuTime/music/wake_we.mp3' :  'Avicii - Wake me Up',
        'mods/MenuTime/music/berega_minus.mp3' : 'monte -  Нас замыкали берега(minus)',
        'mods/MenuTime/music/future.mp3' : 'The Offspring - The Future Is Now',
        'mods/MenuTime/music/vino_main_menu_music.mp3' : 'Музыка из главного меню',
        'mods/MenuTime/music/ki.mp3' : 'White Zombie - Thunder Kiss 65',
        'mods/MenuTime/music/imagine.mp3' : 'John Lennon - Imagine',
        'mods/MenuTime/music/anarchist_m.mp3' : 'UNGBLUD - Anarchist (Minus)',
        'mods/MenuTime/music/tutu.mp3' : 'Whitley Houtson - Saving All My Love For You',
        'mods/MenuTime/music/asia.mp3' : 'Domitori Taranofu - Breath of Asia',
        'mods/MenuTime/music/payback.mp3' : 'Shiiva Raw - Payback',
        'mods/MenuTime/music/moonlight.mp3' : 'Domitori Taranofu - Moonlight',
        vino_music_path + 'afterlife.mp3' : 'Cilver - Afterlife',
        vino_music_path + 'akira.mp3' : 'Exyz, Namadzu - Akira',
        vino_music_path + 'alone_1.mp3' : 'Dummy Feelings - Alone',
        vino_music_path + 'anarchist.mp3' : 'YUNGBLUD - Anarchist',
        vino_music_path + 'band.mp3' : 'Gold Brothers Band - Summer Sun',
        vino_music_path + 'den_2.mp3' : 'Дидюля - День(remix)',
        vino_music_path + 'dont_care.mp3' : "Apocalyptica feat. Adam Gontier - I Don't Care",
        vino_music_path + 'fake.mp3' : 'The Tech Thieves - Fake',
        vino_music_path + 'here_comes.mp3' : 'Hypnogaja - Here Comes The Rain Again',
        vino_music_path + 'lithium.mp3' : 'Evanescence - Lithium',
        vino_music_path + 'minus_5.mp3' : 'Танцы Минус - Половинка(minus)',
        vino_music_path + 'minus_6.mp3' : 'Ю-Питер - Дети минут(minus)',
        vino_music_path + 'my_immortal.mp3' : 'Evanescence - My Immortal',
        vino_music_path + 'paradise.mp3' : 'The Rasmus - Dark Matters',
        vino_music_path + 'sugar.mp3' : 'Slowdive - Sugar for the Pill',
        vino_music_path + 'the_future.mp3' : 'The Offspring - The Future Is Now',
        vino_music_path + 'winter.mp3' : 'Emil Bulls - Winterblood',
        'Error' : 'Шазам не знает такого трека:('
        #'mods/MenuTime/music/fon_2.mp3' : 'Фоновая'
    }
    def vino_show_music(text, time):
        """
        Функция показа играемого трека
        Две локальных переменных обязательны, чтобы могли возвращать текст с играемым треком и время ожидания перед повторным вызовом функции.
        В time будем возвращать .1, чтобы не было времени ожидания перед ещё одним вызовом функции.
        """
        music_is_play = renpy.music.is_playing(channel="music")  # Узнаём, играет ли сейчас музыка в канале 'music'
        if music_is_play:  # Если играет, то…
            what_music_play = renpy.music.get_playing(channel="music")  # …узнаём что играет (возвращает нам путь до трека)
            if ( what_music_play not in vino_music_data):  # Проверяем, есть ли такой трек в словаре.
                return (
                    Text("{size=32}{color=#FF0000FF}Неизвестная композиция{/color}{/size}", style=style.vino_play_music_text),
                    0.1,
                )  # Если его нет, появится эта строка вместо названия трека
            else:
                what_music_play = vino_music_data[what_music_play]  # Если есть такой трек в словаре, то нашим выводом на экран станет значение словаря (то бишь, название трека)
                return (
                    Text("{size=32}{color=#FF0000FF}%s{/color}{/size}" % (what_music_play), style=style.vino_play_music_text),
                    0.1,
                )  # Возвращаем (показываем) название (или любой другой текст) песни, что сейчас играет
        else:
            return Text(""), 0.1  # Если музыка не играет, то мы возвращаем пустой текст

    renpy.image("vino_playing_music", DynamicDisplayable(vino_show_music))

    vino_music_box ={
    'mods/MenuTime/music/believer.mp3' : 'Imagine Dragons - Believer',
    'mods/MenuTime/music/brok_w.mp3' : 'D-A-L - Broken Wings',
    'mods/MenuTime/music/count_s.mp3': 'OneRepublic - Counting Stars',
    'mods/MenuTime/music/death_kill.mp3' : 'deathklr84 - Forever Mine',
    'mods/MenuTime/music/drop_dead.mp3' : 'Mari Ferrari, M.Z.I, S-Elm - Drop Dead',
    'mods/MenuTime/music/fallen_leav.mp3' : 'Billi Talent - Fallen Leaves',
    'mods/MenuTime/music/fon_1.mp3' : 'Фоновая - Музыка ангелов',
    'mods/MenuTime/music/fon_4.mp3' : 'Skrizhali - Без слов(минус)',
    'mods/MenuTime/music/forg_1.mp3' : "CoaastGxd - Don't forget",
    'mods/MenuTime/music/freak_1.mp3' : 'Sub Urban Rei AMI - Freak',
    'mods/MenuTime/music/git_1.mp3' : 'Неизвестен - гитара(минус)',
    'mods/MenuTime/music/grandson_blood_water.mp3' : 'Grandson - Blood//Water',
    'mods/MenuTime/music/have_love.mp3' : 'The Sonics - Have Love Will Travel',
    'mods/MenuTime/music/numb.mp3' : 'vowl, prxz - Numb the pain',
    'mods/MenuTime/music/plamenev.mp3' : 'Павел Пламенев - Ночь перед боем(minus)',
    'mods/MenuTime/music/wake_we.mp3' :  'Avicii - Wake me Up',
    'mods/MenuTime/music/berega_minus.mp3' : 'monte -  Нас замыкали берега(minus)',
    'mods/MenuTime/music/future.mp3' : 'The Offspring - The Future Is Now',
    vino_music_path + 'afterlife.mp3' : 'Cilver - Afterlife',
    vino_music_path + 'akira.mp3' : 'Exyz, Namadzu - Akira',
    vino_music_path + 'alone_1.mp3' : 'Dummy Feelings - Alone',
    vino_music_path + 'anarchist.mp3' : 'YUNGBLUD - Anarchist',
    vino_music_path + 'band.mp3' : 'Gold Brothers Band - Summer Sun',
    vino_music_path + 'den_2.mp3' : 'Дидюля - День(remix)',
    vino_music_path + 'dont_care.mp3' : "Apocalyptica feat. Adam Gontier - I Don't Care",
    vino_music_path + 'fake.mp3' : 'The Tech Thieves - Fake',
    vino_music_path + 'here_comes.mp3' : 'Hypnogaja - Here Comes The Rain Again',
    vino_music_path + 'lithium.mp3' : 'Evanescence - Lithium',
    vino_music_path + 'minus_5.mp3' : 'Танцы Минус - Половинка(minus)',
    vino_music_path + 'minus_6.mp3' : 'Ю-Питер - Дети минут(minus)',
    vino_music_path + 'my_immortal.mp3' : 'Evanescence - My Immortal',
    vino_music_path + 'paradise.mp3' : 'The Rasmus - Dark Matters',
    vino_music_path + 'sugar.mp3' : 'Slowdive - Sugar for the Pill',
    vino_music_path + 'the_future.mp3' : 'The Offspring - The Future Is Now',
    vino_music_path + 'winter.mp3' : 'Emil Bulls - Winterblood'
    #'mods/MenuTime/music/fon_2.mp3' : 'Фоновая'
    }


    vino_mr = MusicRoom(channel='music', fadeout=1.0, fadein=0.5, loop=True, single_track=False, shuffle=False, stop_action=None)
    for name in vino_music_box:
        vino_mr.add(name, always_unlocked=True)
    vino_hover = 'mods/MenuTime/sounds/vino_hover.mp3'
#####################################################
    # vino_g = Gallery()
    # vino_g_page_menu = 1
    # vino_g.transition = fade
    # vino_g.locked_button  = 'mods/MenuTime/gui/gallery/locked_gallery_img.png'
    # #изображения для выбора фона меню:
    # vino_g.button('bgmenu')
    # vino_g.image('bg_menu_girl')

    # vino_g.button('bgmenu1')
    # vino_g.image('bg_menu_lena')

    # vino_g.button('bgmenu2')
    # vino_g.image('bg_menu_ulyana')

    # vino_g.button('bgmenu3')
    # vino_g.image('backroad_night')

    # vino_g.button('bgmenu4')
    # vino_g.image('miku_bg')

    # vino_g.button('bgmenu5')
    # vino_g.image('paint_bg')

    # vino_g.button('bgmenu6')
    # vino_g.image('vino_bg')

    # vino_g.button('bgmenu7')
    # vino_g.image('girls_ofsummer_bg')
    # vino_gallery_bg = Gallery()
    # vino_gallery_bg.transition = fade
    # vino_gallery_bg_page = 1
    # vino_gallery_bg.locked_button = 'mods/MenuTime/gui/gallery/locked_gallery_img.png'
    # vino_gallery_bg.unlocked_advance = True
    # vino_gallery_bg.navigation = True
    # vino_gallery_bg.span_buttons = True
    # ########bg####################################
    # vino_gallery_bg.button('vino_gallery_bg_1')
    # vino_gallery_bg.unlock_image('airplane_1080')

    # vino_gallery_bg.button('vino_gallery_bg_2')
    # vino_gallery_bg.unlock_image('dnll_1')

    # vino_gallery_bg.button('vino_gallery_bg_3')
    # vino_gallery_bg.unlock_image('ext_forest_rising')

    # vino_gallery_bg.button('vino_gallery_bg_4')
    # vino_gallery_bg.unlock_image('hospital')

    # vino_gallery_bg.button('vino_gallery_bg_5')
    # vino_gallery_bg.unlock_image('klass_1')

    # vino_gallery_bg.button('vino_gallery_bg_6')
    # vino_gallery_bg.unlock_image('pole')


    # vino_gallery_bg.button('vino_gallery_bg_7')
    # vino_gallery_bg.unlock_image('xyd_1')


    # vino_gallery_bg.button('vino_gallery_bg_8')
    # vino_gallery_bg.unlock_image('obs_ext_dining_bench_sunset')
################################################################

screen vino_music:
    tag menu
    modal True 
    $ time = vino_get_time()
    frame:
        add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
        textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
            hover_sound vino_hover
            action (Hide('vino_music', Dissolve(1.0)), Return(), Play('music', renpy.random.choice(vino_menu_music[time])))
        key "K_ESCAPE" action (Hide('vino_music', Dissolve(1.0)), Return(), Play('music', 'mods/MenuTime/music/vino_main_menu_music.mp3'))
        window:
            background None 
            area (580,127,866,825)
            viewport id 'vino_music_box':
                draggable True
                mousewheel True
                has vbox
                spacing 5 
                for path, name in sorted(vino_music_box.iteritems()):
                    textbutton name:
                        xalign 0.5
                        style 'vino_button_none'
                        text_style 'vino_text_%s' % time
                        hover_sound vino_hover
                        action vino_mr.Play(path)

screen vino_mainmenu():
    tag menu
    modal True
    $ time = vino_get_time()
    key 'game_menu':
        action NullAction() 
    # on "show" action Play("music", renpy.random.choice(vino_menu_music[time]))
    add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
    add 'mods/MenuTime/gui/menu/header_%s.png' % time xpos 0:
        at transform:
            on show:
                ypos -500
                easein 1 ypos 0
    add 'mods/MenuTime/gui/menu/nav_bg_%s.png' % time xpos 50 ypos 190:
        at transform:
            on show:
                parallel:
                    alpha 0.0
                    easein 1 alpha 1.0
                parallel:
                    ypos 220
                    easein 1 ypos 190
            on hide:
                xpos 50
                easeout 0.4 xpos 60
                easeout 1 xpos -500 
    textbutton "Crimson Team"  style "vino_button_none" text_style "vino_text_%s" % time xpos 1673 ypos 100 hover_sound vino_hover action ShowMenu("vino_authors"): #OpenURL("https://vk.com/crimsoteam")
        at transform:
            on show:
                ypos -500
                easein 1 ypos 100
    vbox xpos 50 xsize 530 ypos 265 spacing 30:
        textbutton "Продолжить" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim hover_sound vino_hover text_insensitive_color "#9E9E9E" action Vino_Continue(), Vino_FunctionCallback(vino_on_load_callback, renpy.newest_slot("vino_FilePage_"))
        textbutton "Начать" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim hover_sound vino_hover action Start("crimson_team")
        textbutton "Загрузить" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim hover_sound vino_hover action ShowMenu("load")
        textbutton "Лагерные истории" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim hover_sound vino_hover action ShowMenu("vino_dlc_story")
        # textbutton "Галерея" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim hover_sound vino_hover action ShowMenu('vino_gallery')        
        textbutton "Настройки" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim hover_sound vino_hover action ShowMenu("vino_preferences")
        if persistent.vino_Developer:
            textbutton 'Дни' xalign 0.5 style 'vino_button_none' text_style "vino_text_%s" % time hover_sound vino_hover action ShowMenu('vino_days_developer') at vino_button_anim 
            null height 120
        else:
            null height 160
        textbutton "Выход" xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
            hover_sound vino_hover
            action ShowMenu("vino_exit")
        at transform:
            on show:
                parallel:
                    alpha 0.0
                    easein 1 alpha 1.0
                parallel:
                    ypos 280
                    easein 1 ypos 265
            on hide:
                xpos 50
                easeout 0.4 xpos 60
                easeout 1 xpos -500
    # textbutton "Выбор фона" xalign 0.85 yalign 0.9 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
    #     hover_sound vino_hover
    #     action ShowMenu("vino_set_bg")
    # textbutton "Авторы" xalign 0.15 yalign 0.9 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
    #     hover_sound vino_hover
    #     action ShowMenu("vino_authors")
    imagebutton:
        idle ImageReference("vino_plate")
        hover_sound vino_hover
        align(0.93, 0.88)
        at vino_plate_anim
        action ShowMenu("vino_music") 
        
screen vino_preferences:
    tag menu
    modal True
    $ time = vino_get_time()
    window at vino_on_show_authors_menu:
        add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
        textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
            hover_sound vino_hover
            action (Hide('vino_preferences', Dissolve(1.0)), Return())
        # button xalign 0.6 hover_sound vino_hover xsize 10 ysize 5 action SetVariable('vino_Devoloper', not vino_Devoloper)
        if not main_menu:
            textbutton '>' xalign 0.95 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
                hover_sound vino_hover
                action ShowMenu('vino_save', Dissolve(1.0))
            textbutton '<' xalign 0.05 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
                hover_sound vino_hover
                action ShowMenu('vino_load', Dissolve(1.0))
        key "K_ESCAPE" action (Hide('vino_preferences', Dissolve(1.0)), Return())
        vbox align(0.2,0.5):
            text "Режим экрана" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            hbox spacing 10 xalign 0.5:
                textbutton "Оконный" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action Preference("display","window")
                textbutton "Полноэкранный" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action Preference("display","fullscreen")
            null height 40
            text "Пропускать" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            hbox spacing 10 xalign 0.5:
                textbutton "Всё" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action Preference("skip","all")
                textbutton "Что увидел" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action Preference("skip","seen")
            null height 40
            text "Размер шрифта" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            hbox spacing 10 xalign 0.5:
                textbutton "Обычный" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action SetField(persistent,"font_size","small")
                textbutton "Большой" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action SetField(persistent,"font_size","large")
            null height 80
            text "Скорость текста" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            bar value Preference("text speed") maximum(374,69) xalign 0.5:
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % time
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % time
        vbox align(0.8,0.5):
            text "Автопереход" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            hbox spacing 10 xalign 0.5:
                textbutton "Включить" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action [If(preferences.afm_time == 0,true=Preference("auto-forward time", 20)),Preference("auto-forward after click","enable"),SelectedIf(preferences.afm_time != 0 or preferences.afm_after_click == "enable")]
                textbutton "Выключить" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time:
                    action [Preference("auto-forward time", 0),Preference("auto-forward after click","disable"),SelectedIf(preferences.afm_time == 0 or preferences.afm_after_click == "disable")]
            bar value Preference("auto-forward time") xalign 0.5 maximum(374,69):
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % time
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % time
            null height 40
            text "Музыка" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            bar value Preference("music volume") maximum(374,69) xalign 0.5:
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % time
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % time
            null height 40
            text "Звуки" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            bar value Preference("sound volume")  maximum(374,69) xalign 0.5:
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % time
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % time
            null height 40
            text "Эмбиент" style "vino_text_%s" % time size 45 xalign 0.5 outlines [ (absolute(2), '#0e246e', absolute(1), absolute(1))]
            bar value Preference("voice volume")  maximum(374,69) xalign 0.5:
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % time
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % time
            null height 40
            textbutton "Без звука" text_size 35 style "vino_button_none" text_style "vino_text_%s" % time xalign 0.5:
                action Preference("all mute", "toggle") 


screen vino_save:
    key "game_menu":
        action NullAction()

    $ time = vino_get_time()
    key "K_ESCAPE" action (Hide('vino_save', Dissolve(1.0)), Return())
    tag menu
    modal True
    window at vino_on_show_authors_menu:
        add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
        textbutton '>' xalign 0.95 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
            hover_sound vino_hover
            action ShowMenu('vino_load', Dissolve(1.0))
        textbutton '<' xalign 0.05 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
            hover_sound vino_hover
            action ShowMenu('vino_preferences', Dissolve(1.0))
        textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
            action (Hide('vino_save', Dissolve(1.0)), Return())
        textbutton ["Сохранить игру"]:
            text_style "vino_text_%s" % time
            style "vino_button_none"
            ypos 850
            xalign 0.2
            action ( Vino_FunctionCallback(vino_on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton ["Удалить"]:
            text_style "vino_text_%s" % time
            style "vino_button_none"
            xalign 0.8
            ypos 850
            action FileDelete(selected_slot)
        vbox:
            xalign 0.070
            yalign 0.35
            grid 1 9:
                for i in range(1, 10):
                    textbutton str(i):
                        xpos 36
                        style "vino_button_none"
                        text_style "vino_text_%s" % time
                        text_size 60 
                        action (FilePage("vino_FilePage_"+ str(i)), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.12
            ypos 0.15
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 23
                        ypos 23
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "vino_save_load_button_%s" % time
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                style "vino_save_load_button_%s" % time
                                xpos 15
                                ypos 15
screen vino_load:
    key "game_menu":
        action NullAction()
    $ time = vino_get_time()
    key "K_ESCAPE" action (Hide('vino_load', Dissolve(1.0)), Return())
    tag menu
    modal True
    $ layout.LOADING = "Потерять несохраненые данные?"
    window at vino_on_show_authors_menu:
        add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
        if not main_menu:
            textbutton '>' xalign 0.95 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
                hover_sound vino_hover
                action ShowMenu('vino_preferences', Dissolve(1.0))
            textbutton '<' xalign 0.05 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
                hover_sound vino_hover
                action ShowMenu('vino_save', Dissolve(1.0))
        textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
            action (Hide('vino_load', Dissolve(1.0)), Return())
        textbutton ["Загрузить игру"]:
            text_style "vino_text_%s" % time
            style "vino_button_none"
            ypos 850
            xalign 0.2
            action (Vino_FunctionCallback(vino_on_load_callback, selected_slot), FileLoad(selected_slot))

        textbutton ["Удалить"]:
            text_style "vino_text_%s" % time
            style "vino_button_none"
            xalign 0.8
            ypos 850
            action FileDelete(selected_slot)
        vbox:
            xalign 0.070
            yalign 0.35
            grid 1 9:
                for i in range(1, 10):
                    textbutton str(i):
                        xpos 36
                        style "vino_button_none"
                        text_style "vino_text_%s" % time
                        text_size 60
                        action (FilePage("vino_FilePage_"+ str(i)), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.12
            ypos 0.15
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 23
                        ypos 23
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "vino_save_load_button_%s" % time
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                style "vino_save_load_button_%s" % time
                                xpos 15
                                ypos 15


screen vino_pre_menu:
    timer 0.001 action ((Hide("vino_pre_menu", transition=fade3), MainMenu(confirm = False)))

screen vino_exit:
    tag menu
    modal True 
    $ time = vino_get_time()
    add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
    text "{font=mods/MenuTime/helvetica.otf}Ты хочешь уйти?{/font}":
        size 100
        text_align 0.5
        xalign 0.7
        yalign 0.33
        antialias True
        kerning 2
    textbutton 'Да':
        style 'vino_button_none'
        text_style "vino_text_%s" % time
        xalign 0.55
        yalign 0.55
        text_size 60
        hover_sound vino_hover
        action [(Function(vino_screens_diact)), ShowMenu("main_menu")]
    textbutton 'Нет':
        style 'vino_button_none'
        text_style "vino_text_%s" % time
        xalign 0.73
        yalign 0.55
        text_size 60
        hover_sound vino_hover
        action [ Hide("vino_exit", Dissolve(1.0)), Return()]



screen vino_authors:
    tag menu 
    modal True
    $ time = vino_get_time()
    add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
    textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
        hover_sound vino_hover
        action (Hide('vino_authors', Dissolve(1.0)), Return())
    key "K_ESCAPE" action (Hide('vino_authors', Dissolve(1.0)), Return())
    vbox xalign 0.5 yalign 0.5 spacing 25 at vino_on_show_authors_menu: 
        textbutton "Кодер" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/awalone_13")
        textbutton "Кодер(интерфейс,функции)" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/banderak")
        textbutton "Кодер" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/olyunin96")
        textbutton "Сценарист" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/dvoeglazovt")
        textbutton "Дизайнер" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/id424308705")
        textbutton "Кодер" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/kefir331")
        textbutton "Сценарист" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/soviet_guy413")
        textbutton "Кодер" text_size 40 align(0.5,0.05) style "vino_button_none" text_style "vino_text_%s" % time:
            hover_sound vino_hover
            action OpenURL("https://vk.com/k.pioneer")

screen vino_dlc_story:
    tag menu
    modal True
    key 'game_menu':
        action NullAction()
    $ time = vino_get_time()
    key "K_ESCAPE" action (Hide('vino_dlc_story', Dissolve(1.0)), Return())
    add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
    textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
        hover_sound vino_hover
        action (Hide('vino_dlc_story', Dissolve(1.0)), Return())
    hbox align(0.1,0.5) spacing 25 at vino_on_show_authors_menu:
        textbutton 'Один день до дискотеки' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time  text_size 30 at vino_button_anim:
            hover_sound vino_hover
            hovered [ShowTransient('vino_dlc_story_descript', Dissolve(1.0), page=1)]
            unhovered Hide('vino_dlc_story_descript', Dissolve(1.0)) 
            action Start('labelgo'), Stop('music'), Hide('menu', Dissolve(1.0))


screen vino_dlc_story_descript(page):
    modal False 
    tag vino_dlc_story_descript
    $ time = vino_get_time()
    frame:
        background None 
        if page == 1:
            hbox align(0.5,0.5):
                area(700,300,500,500)
                text 'История, произошедшая за год до появления Даниила Элонова в "Совёнке": во времена той самой легендарной смены, в которую ненароком попал Семён.События разворачиваются за день до грядущих танцев. Что же там произошло?...':
                    style "vino_text_%s" % time
                    size 30 
                    xalign 0.5
                    yalign 0.5

        else:
            pass 


screen vino_say:
    window: 
        background None
        id "window"
        $ timeofday = persistent.timeofday
        if persistent.font_size == "large":
            imagebutton:
                auto ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/backward_new_%s.png")
                xpos 0
                ypos 912
                action ShowMenu("text_history")
            add ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/dialogue_box_large.png"):
                xpos 118
                ypos 866
            if not config.skipping:
                imagebutton:
                    auto ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/forward_new_%s.png")
                    xpos 1700
                    ypos 912
                    action Skip()
            else:
                imagebutton:
                    auto ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/fast_forward_new_%s.png")
                    xpos 1700
                    ypos 912
                    action Skip()
            text what:
                id "what"
                xpos 145
                ypos 930
                xmaximum 1540
                size 30
                color "#F2F2F2"
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 145
                    ypos 890
                    size 35
                    line_spacing 1
        elif persistent.font_size == "small":
            imagebutton:
                auto ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/backward_new_%s.png")
                xpos 12
                ypos 935
                action ShowMenu("text_history")
            add ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/dialogue_box_small.png"):
                xpos 124
                ypos 907
            if not config.skipping:
                imagebutton:
                    auto ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/forward_new_%s.png")
                    xpos 1700
                    ypos 932
                    action Skip()
            else:
                imagebutton:
                    auto ("mods/MenuTime/gui/dialogue_box/"+timeofday+"/fast_forward_new_%s.png")
                    xpos 1700
                    ypos 932
                    action Skip()
            text what:
                id "what"
                xpos 160
                ypos 964
                xmaximum 1490
                ymaximum 1020
                size 20
                color "#F2F2F2"
                line_spacing 2
            if who:
                text who:
                    id "who"
                    xpos 160
                    ypos 930
                    size 28
                    line_spacing 2
screen vino_nvl:
    $ timeofday = persistent.timeofday
    window:
        background Frame('mods/MenuTime/gui/text_history/'+timeofday+'/Text_history_bg.png',50,50)
        xfill True
        yfill True
        yalign 0.5
        left_padding 125
        right_padding 125
        bottom_padding 100
        top_padding 100
        vbox:
            for who, what, who_id, what_id, window_id  in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if persistent.font_size == "large":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 35
                            text what:
                                id what_id
                                size 35
                                color "#F2F2F2"
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 24
                            text what:
                                id what_id
                                size 24
                                color "#F2F2F2"
            if items:
                vbox:
                    id "menu"
                    for caption, action, chosen  in items:
                        if action:
                            button:
                                style "nvl_menu_choice_button"
                                action action
                                text caption:
                                    style "nvl_menu_choice"
                        else:
                            text caption:
                                style "nvl_dialogue"

    if not config.skipping:
        imagebutton:
            auto('mods/MenuTime/gui/dialogue_box/'+timeofday+'/forward_new_%s.png')
            xpos  1712
            ypos 884
            action Skip()
    else:
        imagebutton:
            auto('mods/MenuTime/gui/dialogue_box/'+timeofday+'/fast_forward_new_%s.png')
            xpos  1712
            ypos 884
            action Skip()


screen vino_game_menu_selector:
    $ timeofday = persistent.timeofday
    tag menu modal True
    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()
    add 'mods/MenuTime/gui/quick_menu/game_menu_left_%s.png' % timeofday xpos 142
    add 'mods/MenuTime/gui/quick_menu/game_menu_right_%s.png' % timeofday xpos 960
    #левая часть экрана
    text 'сейчас играет:':
        font 'mods/MenuTime/helvetica.otf'
        size 46
        xpos 280
        ypos 20
    vbox xpos 145 xsize 530 ypos 80:
        add 'vino_playing_music' xalign 0.5
    vbox spacing 35 xpos 280 ypos 200:
        textbutton 'В главное меню' xalign 0.5 style "vino_button_none" text_style "vino_game_menu_selector_%s" % timeofday hover_sound vino_hover  action MainMenu(confirm=True) at vino_button_anim
        textbutton 'Сохранить' xalign 0.5 style "vino_button_none" text_style "vino_game_menu_selector_%s" % timeofday hover_sound vino_hover action ShowMenu('vino_save') at vino_button_anim
        textbutton 'Загрузить' xalign 0.5 style "vino_button_none" text_style "vino_game_menu_selector_%s" % timeofday hover_sound vino_hover action ShowMenu('vino_load') at vino_button_anim
        textbutton 'Настройки' xalign 0.5 style "vino_button_none" text_style "vino_game_menu_selector_%s" % timeofday hover_sound vino_hover action ShowMenu('vino_preferences') at vino_button_anim
    vbox xpos 370 ypos 980:    
        textbutton 'Выход' xalign 0.5 style "vino_button_none" text_style "vino_game_menu_selector_%s" % timeofday hover_sound vino_hover action ShowMenu('vino_exit') at vino_button_anim
    #правая часть экрана
    vbox xpos 983 ypos 30 xsize 815:
        text save_name xalign 0.5 style 'vino_game_menu_selector_%s' % timeofday size 28
    vbox xpos 983 ypos 80 spacing 50 xsize 815:
        vbox spacing 10 xalign 0.5:
            text "Музыка" style 'vino_game_menu_selector_%s' % timeofday xalign 0.5
            bar value Preference("music volume") maximum(374,69):
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % timeofday
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % timeofday 
                xalign 1.0 
        vbox spacing 10 xalign 0.5:
            text "Звуки" style 'vino_game_menu_selector_%s' % timeofday xalign 0.5
            bar value Preference("sound volume")  maximum(374,69):
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % timeofday
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % timeofday
        vbox spacing 10 xalign 0.5:
            text "Эмбиент" style 'vino_game_menu_selector_%s' % timeofday xalign 0.5
            bar value Preference("voice volume")  maximum(374,69):
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % timeofday
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % timeofday
        vbox spacing 10 xalign 0.5:
            text "Скорость текста" style 'vino_game_menu_selector_%s' % timeofday xalign 0.5
            bar value Preference("text speed") maximum(374,69):
                left_bar "mods/MenuTime/gui/quick_menu/bar_full_%s.png" % timeofday
                right_bar "mods/MenuTime/gui/quick_menu/bar_null.png"
                thumb "mods/MenuTime/gui/quick_menu/bar_thumb_%s.png" % timeofday
    vbox ypos 795 xpos 1040 xsize 760 spacing 45:
        text "Размер текста" style 'vino_game_menu_selector_%s' % timeofday xalign 0.5
        hbox spacing 320:
            textbutton "Нормальный"  style 'vino_button_none' text_style 'vino_game_menu_selector_%s' % timeofday:
                action SetField(persistent,"font_size","small"), SelectedIf(persistent.font_size == "small")
            textbutton "Большой" style 'vino_button_none' text_style 'vino_game_menu_selector_%s' % timeofday:
                action SetField(persistent,"font_size","large"), SelectedIf(persistent.font_size == "large")







screen vino_yesno_prompt:
    tag menu modal True  
    $ time = vino_get_time()
    $ timeofday = persistent.timeofday
    add 'mods/MenuTime/gui/yes_no/yesno_promt_%s.png' % timeofday
    text _(message) text_align 0.5 yalign 0.46 xalign 0.5 color "#FFFFFF" font 'mods/MenuTime/vino_font.ttf' size 25
    textbutton translation_new["Yes"] text_size 60 style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover yalign 0.65 xalign 0.3 action yes_action at vino_button_anim
    textbutton translation_new["No"] text_size 60 style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover yalign 0.65 xalign 0.7 action Return() at vino_button_anim
screen vino_paper_nvl:
    window:
        background None 
        add 'mods/MenuTime/gui/nvl/paper/paper_nvl.png':
            xalign 0.5
            yalign 0.5
        xfill True
        yfill True
        yalign 0.5
        xalign 0.5
        left_padding 125
        right_padding 125
        bottom_padding 100
        top_padding 100
        vbox:
            for who, what, who_id, what_id, window_id  in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if persistent.font_size == "large":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 35
                            text what:
                                id what_id
                                xpos 560
                                xmaximum 590
                                ymaximum 950
                                size 35
                                color "#18204D"
                                font 'mods/MenuTime/paper_text.otf'
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 24
                            text what:
                                id what_id
                                xpos 560
                                xmaximum 590
                                ymaximum 950
                                size 24
                                color "#18204D"
                                font 'mods/MenuTime/paper_text.otf'

# screen vino_gallery:
#     tag menu
#     modal True 
#     $ time = vino_get_time()
#     key "game_menu":
#         action NullAction()
#     key "K_ESCAPE" action (Hide('vino_gallery', Dissolve(1.0)), Return())
#     add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
#     textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time at vino_button_anim:
#         hover_sound vino_hover
#         action (Hide('vino_dlc_story', Dissolve(1.0)), Return(), SetVariable('vino_gallery_bg_page', 1))
#     if vino_gallery_bg_page < 2:
#         textbutton '>' xalign 0.95 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
#             hover_sound vino_hover
#             action SetVariable('vino_gallery_bg_page', vino_gallery_bg_page+1)
#     else:
#         pass
#     if vino_gallery_bg_page !=1:
#         textbutton '<' xalign 0.1 yalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time text_size 80 at vino_button_anim:
#             hover_sound vino_hover
#             action SetVariable('vino_gallery_bg_page', vino_gallery_bg_page-1)
#     else:
#         pass
#     if vino_gallery_bg_page == 1:
#         grid 2 2:
#             xfill True
#             yfill True
#             add vino_gallery_bg.make_button('vino_gallery_bg_1', im.Scale("mods/MenuTime/bg/airplane_1080.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#             add vino_gallery_bg.make_button('vino_gallery_bg_2', im.Scale("mods/MenuTime/bg/dnll_1.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#             add vino_gallery_bg.make_button('vino_gallery_bg_3', im.Scale("mods/MenuTime/bg/ext_forest_rising.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#             add vino_gallery_bg.make_button('vino_gallery_bg_4', im.Scale("mods/MenuTime/bg/hospital.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#     elif vino_gallery_bg_page == 2:
#         grid 2 2:
#             xfill True
#             yfill True
#             add vino_gallery_bg.make_button('vino_gallery_bg_5', im.Scale("mods/MenuTime/bg/klass_1.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#             add vino_gallery_bg.make_button('vino_gallery_bg_6', im.Scale("mods/MenuTime/bg/pole.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#             add vino_gallery_bg.make_button('vino_gallery_bg_7', im.Scale("mods/MenuTime/bg/xyd_1.jpg", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')
#             add vino_gallery_bg.make_button('vino_gallery_bg_8', im.Scale("mods/MenuTime/bg/obs_ext_dining_bench_sunset.png", 587,375), xalign=0.5, yalign=0.5, hover_border='mods/MenuTime/gui/gallery/hover_gallery_img.png')


screen vino_days_developer:
    tag menu 
    modal True 
    $ time = vino_get_time()
    key "K_ESCAPE" action (Hide('vino_days_developer', Dissolve(1.0)), Return())
    add 'mods/MenuTime/gui/menu/menu_bg_%s.png' % time 
    textbutton 'Закрыть' xalign 0.5 style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action (Hide('vino_days_developer', Dissolve(1.0)), Return()) at vino_button_anim

    hbox align(0.5, 0.5) spacing 20:
        textbutton 'Пролог' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('crimson_team')
        textbutton 'День 1' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('vino_day1')
        textbutton 'День 2' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('vino_day2')
        textbutton 'День 3' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('vino_day3')
        textbutton 'День 4' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('vino_day4')
        textbutton 'День 5' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('vino_day5')
        textbutton 'День 6' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('vino_day6')

    # hbox align(0.5,0.6) spacing 20:
    #     textbutton 'Титры' style "vino_button_none" text_style "vino_text_%s" % time hover_sound vino_hover action Start('titry')

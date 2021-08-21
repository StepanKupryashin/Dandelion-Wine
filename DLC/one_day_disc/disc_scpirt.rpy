init:
    $ ptica = Character(u'Птица')
    $ kolonka = Character(u'Колонка')    
init -9 python:
    MOD_ID = "one_day_disc"
    for file in renpy.list_files():
        if MOD_ID in file:
            file_name = path.splitext(path.basename(file))[0]
            file_split = file.split("/")

            if file.endswith((".png", ".jpg")):
                if "sprites" in file_split:
                    renpy.image(
                        file_name,
                        ConditionSwitch(
                            "persistent.sprite_time == 'sunset'",
                            im.MatrixColor(
                                file,
                                im.matrix.tint(0.94, 0.82, 1.0)
                            ),
                            "persistent.sprite_time == 'night'",
                            im.MatrixColor(
                                file,
                                im.matrix.tint(0.63, 0.78, 0.82)
                            ),
                            True,
                            file
                        )
                    )
                else:
                    renpy.image(file_name, file)
            elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file


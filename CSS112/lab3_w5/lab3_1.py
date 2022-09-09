Jlist = ['Jeff','Jake' ,'Jim']
name = str(input("What is your name? :"))
name = name.capitalize()


def checkJ_name(name):
    if name in Jlist:
        myjList = "Hello, {}. Good morning my firend!"
        return myjList.format(name)
    else:
        print("Who are you")
        notmyjList = "Nice to meet you anyway ...{} :)"
        return notmyjList.format(name)

print(checkJ_name(name))
##
#!##############################
#!########## IMPORTS ###########
#!##############################
# region
from datetime import datetime
import os
import pyfireconnect
import json
import questionary
import keyring as kr
import datetime
import os
import requests
from webbrowser import open_new_tab
import platform
from firebaseconfig import firebaseConfig

# endregion


#!##############################
#!#### INITIALIZE CONFIGS ######
#!##############################
# region


minimalStyle = questionary.Style(
    [
        ("answer", "fg:#FFFFFF"),
        ("pointer", "fg:#FFFFFF "),
        ("highlighted", "fg:#FFFFFF"),
        ("selected", "fg:#FFFFFF"),
    ]
)
firebase = pyfireconnect.initialize(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
# endregion


#!##############################
#!###### MISC FUNCTIONS ########
#!##############################
# region


def clearScreen():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def showCredits():
    clearScreen()
    print(" ")
    print(" a project by adithya [https://adithya.zip]")
    print(" visit the moment website [https://moment.adithya.zip] for more info")
    print(" ")
    print(" if there are any issues with logging in or using your account,")
    print(" contact me via my email address: me@adithya.zip")
    print(" and i'll get back to you within a few hours")
    print(" ")
    print(" whenever you visit your .txt webpage,")
    print(" please keep in mind that it may take a while")
    print(" for the website to launch due to the limited resources")
    print(" that this project runs on. if you want the project to")
    print(" succeed and help it grow, thus increasing its resources,")
    print(" please share it within your online communities and friends")
    print(" or consider donating to my ko-fi page: https://ko-fi.com/adithyasource")
    input()


def setDisplayName(displayName, idToken):
    request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/setAccountInfo?key={0}".format(
        auth.api_key
    )
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"idToken": idToken, "displayName": displayName})
    try:
        request_object = requests.post(request_ref, headers=headers, data=data)
        return request_object.json()
    except:
        request_object.raise_for_status()


# endregion


#!##############################
#!###### MAIN FUNCTIONS ########
#!##############################
# region
def main(user):
    clearScreen()
    mainMenuChoice = questionary.select(
        "",
        choices=[
            "new post",
            "view posts",
            "delete posts \n",
            "your .txt webpage \n",
            f'sign out [{user["displayName"]}]',
            "moment®",
        ],
        qmark="",
        instruction=" ",
        pointer="▶",
        style=minimalStyle,
    ).ask()
    if mainMenuChoice == "new post":
        clearScreen()
        postInput = input()
        if postInput != "":
            postInput = f"{str(datetime.datetime.now())}: " + postInput
            db.child("users").child(user["displayName"]).push(postInput)

            data = db.child("users").child(user["displayName"]).get()
            alBlogPosts = ""

            for blogPosts in (json.loads(json.dumps(data.val()))).values():
                alBlogPosts += blogPosts + "\n"

            with open("temp.txt", "w") as f:
                f.write(str(alBlogPosts))

            storage.child(f"{user['displayName']}.txt").put("temp.txt")

            os.remove("temp.txt")
            main(user)
        else:
            main(user)
    elif mainMenuChoice == "view posts":
        try:
            clearScreen()
            print(" ")
            data = db.child("users").child(user["displayName"]).get()
            for blogPosts in (json.loads(json.dumps(data.val()))).values():
                print(" " + blogPosts)
            input()
            main(user)
        except:
            print(" no posts yet")
            input()
            main(user)
    elif mainMenuChoice == "delete posts \n":
        try:
            clearScreen()
            data = db.child("users").child(user["displayName"]).get()
            blogPostsList = []
            for blogPosts in (json.loads(json.dumps(data.val()))).values():
                blogPostsList.append(blogPosts)
            deleteChoices = questionary.checkbox(
                "\n select which posts you want to delete \n\n",
                choices=blogPostsList,
                qmark="",
                pointer="▶",
                style=minimalStyle,
            ).ask()

            clearScreen()

            if deleteChoices != []:
                print(" these are the items to be deleted: \n")

                for deleteChoice in deleteChoices:
                    print(" " + deleteChoice)

                print(" ")
                confirmDelete = questionary.confirm(
                    "are you sure you want to delete them?",
                    qmark="",
                    style=minimalStyle,
                ).ask()

                if confirmDelete == True:

                    def findKeyByValue(dictionary, value):
                        for key, val in dictionary.items():
                            if val == value:
                                return key
                        raise ValueError("Value not found in the dictionary")

                    for deleteChoice in deleteChoices:
                        data = db.child("users").child(user["displayName"]).get()
                        for i in json.loads(json.dumps(data.val())).values():
                            if i == deleteChoice:
                                choiceKey = findKeyByValue(
                                    json.loads(json.dumps(data.val())), i
                                )
                                db.child("users").child(user["displayName"]).child(
                                    choiceKey
                                ).remove()

                        data = db.child("users").child(user["displayName"]).get()
                        alBlogPosts = ""

                        for blogPosts in (json.loads(json.dumps(data.val()))).values():
                            alBlogPosts += blogPosts + "\n"

                        with open("temp.txt", "w") as f:
                            f.write(str(alBlogPosts))

                    storage.child(f"{user['displayName']}.txt").put("temp.txt")
                    os.remove("temp.txt")
        except:
            print(" no posts yet")
            input()
        main(user)

    elif mainMenuChoice == "your .txt webpage \n":
        open_new_tab(f'https://moment.adithya.zip/{user["displayName"]}.txt')
        main(user)
    elif mainMenuChoice == "moment®":
        showCredits()
        main(user)
    elif mainMenuChoice == f'sign out [{user["displayName"]}]':
        c = kr.get_credential("moment", None)
        c = kr.delete_password("moment", c.username)
        authenticate()


def authenticate():
    clearScreen()

    authenticateMenuChoice = questionary.select(
        "",
        choices=["log in", "sign up", "forgot password", "moment®"],
        qmark="",
        instruction=" ",
        pointer="▶",
        style=minimalStyle,
    ).ask()
    if authenticateMenuChoice == "log in":
        clearScreen()
        email = questionary.text(
            "\n enter your email", qmark="", style=minimalStyle
        ).ask()
        password = questionary.password(
            "enter your password", qmark="", style=minimalStyle
        ).ask()

        try:
            user = auth.sign_in_with_email_and_password(email, password)
        except:
            print(" invalid email / password / user does not exist")
            input()
            authenticate()
        kr.set_password("moment", email, password)
        main(user)
    if authenticateMenuChoice == "sign up":
        clearScreen()
        email = questionary.text("enter your email", qmark="", style=minimalStyle).ask()
        password = questionary.password(
            "enter your password (min 6 characters)", qmark="", style=minimalStyle
        ).ask()
        try:
            user = auth.create_user_with_email_and_password(email, password)
        except:
            print(" user already exists or invalid email / password")
            input()
            authenticate()

        auth.send_email_verification(user["idToken"])
        print(" an email verification link has been sent to your inbox")
        while True:
            print(" hit enter if verified")
            input()
            userData = auth.get_account_info(user["idToken"])
            if userData["users"][0]["emailVerified"] == True:
                break
            else:
                print(" retry")
        while True:
            clearScreen()
            userName = input(
                " enter your username [also used for your link]\n [link example: https://moment.adithya.zip/username.txt] (this cannot be changed) "
            )
            data = db.child("users").child().get()
            users = list((json.loads(json.dumps(data.val()))).keys())

            if userName in users:
                print(" username is taken")
                input()
            else:
                setDisplayName(userName, user["idToken"])
                break
        clearScreen()
        print(" user created")
        print(" ")
        print(" hit enter to go back to the log in screen")
        print(" and log in with your new user credentials")
        print(" ")
        print(" note: whenever you visit your .txt webpage,")
        print("       please keep in mind that it may take a while")
        print("       for the website to launch due to the limited resources")
        print("       that this project runs on. if you want the project to")
        print("       succeed and help it grow, thus increasing its resources,")
        print("       please share it within your online communities and friends")
        print(
            "      or consider donating to my ko-fi page: https://ko-fi.com/adithyasource"
        )
        input()
        authenticate()
    if authenticateMenuChoice == "forgot password":
        clearScreen()
        email = questionary.text("enter your email", qmark="", style=minimalStyle).ask()
        auth.send_password_reset_email(email)
        print(" follow the instructions sent to your inbox")
        print(" [might take a couple mins for it to arrive]")
        input()
        authenticate()
    if authenticateMenuChoice == "moment®":
        showCredits()
        authenticate()


# endregion


#!##############################
#!###### CODE BEGINNING ########
#!##############################
# region


c = kr.get_credential("moment", None)

try:
    user = auth.sign_in_with_email_and_password(c.username, c.password)
    main(user)
except:
    authenticate()


# endregion

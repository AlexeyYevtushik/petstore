* Settings *
Library    ../libs/PetstoreLibrary.py

* Test Cases *
Login With Valid Credentials Should Return 200
    [Documentation]    use GET /user/login to log in
    ${user} =    Create Dictionary    id=1001    username=robot_user_1    firstName=Robot    lastName=User    email=robot@example.com    password=12345    phone=+100000000
    Create User    ${user}
    Login User    robot_user_1    12345
    Should Be Status    200
    Logout User
    Should Be Status    200
    Cleanup Created

* Keywords *
Create User
    [Arguments]    ${user_dict}
    Create User    ${user_dict}

Login User
    [Arguments]    ${username}    ${password}
    Login User    ${username}    ${password}

Logout User
    Logout User
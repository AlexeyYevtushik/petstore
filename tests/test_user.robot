* Settings *
Library    ../libs/PetstoreLibrary.py

* Test Cases *
Create Get Update Delete User Flow
    ${user} =    Create Dictionary    id=2001    username=temp_user_2001    firstName=Temp    lastName=User    email=temp@example.com    password=pass2001    phone=+2001
    Create User    ${user}
    Should Be Status    200

    Get User    temp_user_2001
    Should Be Status    200
    ${json} =    Get Last Json
    Log    ${json}

    ${update} =    Create Dictionary    id=2001    username=temp_user_2001    firstName=Temp2    lastName=User2    email=temp2@example.com    password=pass2001    phone=+2001
    Update User    temp_user_2001    ${update}
    Should Be Status    200

    Delete User    temp_user_2001
    Should Be Status    200

    Cleanup Created
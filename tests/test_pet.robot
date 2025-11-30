* Settings *
Library    ../libs/PetstoreLibrary.py

* Test Cases *
Create And Find Pet By Status
    ${pet} =    Create Dictionary    id=77777    name=RoboDog    category={"id":1,"name":"Dogs"}    photoUrls=@{['http://example.com/dog.jpg']}    tags=@{[{"id":1,"name":"tag1"}]}    status=available
    Create Pet    ${pet}
    Should Be Status    200

    Find Pets By Status    available
    Should Be Status    200
    ${list} =    Get Last Json
    Log    Found ${len(${list})} pets

    Get Pet    77777
    Should Be Status    200

    Delete Pet    77777
    Should Be Status    200

    Cleanup Created
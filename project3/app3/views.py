from django.http import HttpResponse

def showIndex(request):
    message='''
    <!DOCTYPE html>
    <html>
        <head>
            <title>My demo Project</title>
        </head>
        <body bgcolor="lightblue">
            <h1 style="color: rgb(252, 252, 252); text-align: center; background-color: darkkhaki;">My demo Project</h1>
            <marquee>
            <span>Dummy Result of Dummy Student from Dummy Degree college</span>
            </marquee></br> 
            <hr></br>
            <table align="center" style="background-color: rgb(223, 182, 130);" border="2" width="25%"
                <tr>
                    <th>Sr_No.</th>
                    <th>Name</th>
                    <th>Rsult</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Raju</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Vishal</td>
                    <td>Fail</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Mangesh</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Shrikant</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Suresh</td>
                    <td>Fail</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Rajesh</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Vikas</td>
                    <td>Fail</td>
                </tr>
            </table>
        </body>
    </html>'''
    return HttpResponse(message)

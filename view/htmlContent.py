

def viewAll(allRecords):
    
  print('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>View All Data</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <style>
    h1 {
  font-size: 30px;
  color: #fff;
  text-transform: uppercase;
  font-weight: 300;
  text-align: center;
  margin-bottom: 15px;
}
table {
  width: 100%;
  table-layout: fixed;
}
.tbl-header {
  background-color: rgba(255, 255, 255, 0.3);
}
.tbl-content {
  height: 800px;
  overflow-x: auto;
  margin-top: 0px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}
th {
  padding: 20px 15px;
  text-align: left;
  font-weight: 500;
  font-size: 12px;
  color: #fff;
  text-transform: uppercase;
}
td {
  padding: 26px;
  text-align: left;
  vertical-align: middle;
  font-weight: 300;
  font-size: 12px;
  color: #fff;
  border-bottom: solid 1px rgba(255, 255, 255, 0.1);
}

/* demo styles */

@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
body {
  background: -webkit-linear-gradient(left, #00264D, #00172D);
    background: linear-gradient(to right, #00264D, #00172D);
  font-family: "Roboto", sans-serif;
}
section {
  margin: 50px;
}


/* for custom scrollbar for webkit browser*/

::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}
::-webkit-scrollbar-thumb {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}
.example {
      display: flex;

      width: 100%;
      max-width: 600px;
      margin: 0 auto;
    }

    .example input[type="text"] {
      flex: 1;
      padding: 10px;
      font-size: 17px;
      border: 1px solid grey;
      border-right: none;
      background: #f1f1f1;
    }

    .example button, .example input[type="button"] {
      padding: 10px;
      background: #2196F3;
      color: white;
      font-size: 17px;
      border: 1px solid grey;
      border-left: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right:50px;
    }

    .example button:hover {
      background: #0b7dda;
    }
        
  </style>
  <script>
        function submitForm(action) {
            var form = document.forms['example'];
            var backInput = document.getElementById('back-input');

            if (action === 'back') {
                backInput.value = 'true';
            } else {
                backInput.value = '';
            }

            form.submit();
        }
    </script>
</head>
<body>
<form class="example" name="example" action="MyController.py">
    <input type="text" placeholder="Search.." name="searchDetail">
    <button type="submit" name="search" value="search"><i class="fa fa-search"></i></button>
    
    <input type="hidden" id="back-input" name="back" value="">
    <input type="button" id="join-btn" alt="back" value="Back" onclick="submitForm('back')">
  </form>
  <section>
    <!--for demo wrap-->
    <h1>Crab Details</h1>
    <div class="tbl-header">
      <table cellpadding="0" cellspacing="0" >
        <thead>
          <tr>
            <th>Sex</th>
            <th>Length</th>
            <th>Diameter</th>
            <th>Height</th>
            <th>Weight</th>
            <th>Shucked Weight</th>
            <th>Viscera Weight</th>
            <th>Shell Weight</th>
            <th>Age</th>
          </tr>
        </thead>
      </table>
    </div>
    <div class="tbl-content">
      <table cellpadding="0" cellspacing="0" >
        <tbody>
          ''')
  for i in allRecords:
          print("<tr>")
          for j in i:
               print("<td>")
               print(i[j])
               print("</td>")
          print("</tr>")
  print('''
        </tbody>
      </table>
    </div>
  </section>
  
  
  <!-- follow me template -->
 
  <script>
    // '.tbl-content' consumed little space for vertical scrollbar, scrollbar width depend on browser/os/platfrom. Here calculate the scollbar width .
$(window).on("load resize ", function() {
    var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
    $('.tbl-header').css({'padding-right':scrollWidth});
  }).resize();
  </script>
</body>
</html>
''')



def showForm():

    inputForm = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crab Age Prediction</title>
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.css">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Open+Sans:300);
* {
  font-family: "Open Sans", sans-serif;
}

body {
  margin: 0;
  padding: 0;
  overflow: hidden;
  background:#00172D;
  background-repeat: no-repeat;
}

.signupSection {
  background: linear-gradient(to right, #0052A2, #00172D);
  
  background-repeat: no-repeat;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 1000px;
  height: 900px;
  text-align: center;
  display: flex;
  color: white;
  box-shadow: 3px 10px 20px 5px rgba(0, 0, 0, 0.5);
}

.info {
  width: 45%;
  background: rgba(20, 20, 20, 0.8);
  padding: 30px 0;
  border-right: 5px solid rgba(30, 30, 30, 0.8);
  h2 {
    padding-top: 100px;
    font-weight: 300;
  }
  p {
    font-size: 18px;
  }
  .icon {
    font-size: 8em;
    padding: 20px 0;
    color: rgba(10, 180, 180, 1);
  }
}

.details{
    height: 100%;
    margin:auto;
}
.signupForm {
  width: 70%;
  padding: 30px 0;
  background: rgba(20, 40, 40, 0.8);
  transition: 0.2s;
  h2 {
    font-weight: 300;
  }
}

.inputFields {
  margin: 15px 0;
  font-size: 16px;
  padding: 10px;
  width: 250px;
  border: 1px solid rgba(10, 180, 180, 1);
  border-top: none;
  border-left: none;
  border-right: none;
  background: rgba(20, 20, 20, 0.2);
  color: white;
  outline: none;
}

.noBullet {
  list-style-type: none;
  padding: 0;
}

#center-btn {
  display: inline-block;
  margin: 0 10px;
}
#join-btn {
  border: 1px solid rgba(10, 180, 180, 1);
  background: rgba(20, 20, 20, 0.6);
  font-size: 18px;
  color: white;
  margin-top: 20px;
  padding: 10px 50px;
  cursor: pointer;
  transition: 0.4s;
  &:hover {
    background: rgba(20, 20, 20, 0.8);
    padding: 10px 80px;
  }
}

    </style>
  
  <script>
        function submitForm(action) {
            var form = document.forms['signupform'];
            var backInput = document.getElementById('back-input');

            if (action === 'back') {
                backInput.value = 'true';
            } else {
                backInput.value = '';
            }

            form.submit();
        }
    </script>
</head>
<body>
    <div class="signupSection">
        <div class="info">
            <div class="details">
                <h2>Mission to Save Crab</h2>
                <i class="icon ion-ios-ionic-outline" aria-hidden="true"></i>
                <p>The Future Is Here</p>
            </div>
         
        </div>
        <form  action="ContentController.py" class="signupForm" name="signupform">
          <h2>Crab Input</h2>
          <ul class="noBullet">
            <li>
              <label for="sex"></label>
              
              <select id="sex" name="sex" class="form-trolcon inputFields" required>
                <option value="M">M</option>
                <option value="F">F</option>
         
                </select>
          </li>
            <li>
              <label for="length"></label>
              <input type="number"min="0"  max="20" step="0.01"  class="form-control inputFields" id="length" name="length" placeholder="Length" value="" required />
            </li>
            <li>
              <label for="diameter"></label>
              <input type="number" min="0"  max="20" step="0.01" class="form-control inputFields" id="diameter" name="diameter" placeholder="Diameter" value="" required>
            </li>
            <li>
              <label for="height"></label>
              <input type="number" min="0"  max="20" step="0.01" class="form-control inputFields" id="height" name="height" placeholder="Height" value="" required>
            </li>
            <li>
              <label for="weight"></label>
              <input type="number" min="0"  max="20" step="0.01" class="form-control inputFields" id="weight" name="weight" placeholder="Weight" value="" required>
            </li>
            <li>
              <label for="shucked_weight"></label>
              <input type="number" min="0"  max="20" step="0.01"class="form-control inputFields" id="shucked_weight" name="shucked_weight" placeholder="Shucked Weight" value="" required>
            </li>
            <li>
              <label for="viscera_weight"></label>
              <input type="number" min="0"  max="20" step="0.01" class="form-control inputFields" id="viscera_weight" name="viscera_weight" placeholder="Viscera Weight" value="" required>
            </li>
            <li>
              <label for="shell_weight"></label>
              <input type="number" class="form-control inputFields" id="shell_weight" name="shell_weight" placeholder="Shell Weight" min="0"  max="20" step="0.01" value="" required>
            </li>
               
             <li id="center-btn">
                <input type="hidden" id="back-input" name="back" value="">
                <input type="button" id="join-btn" name="back" alt="back" value="Back" onclick="submitForm('back')">
            </li>
            <li id="center-btn">
              <input type="submit" id="join-btn" name="predict" alt="Join" value="Predict">
            </li>
       
          </ul>
        </form>
      </div>
</body>
</html>

"""
    return inputForm
#!/usr/bin/env python3



# Enable CGI error reporting for debugging purposes

def showOutput(res,result, sex, length, diameter, height, weight, shucked, viscera, shell, age):
    inputForm = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crab Age Prediction</title>
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.css">
   
    <style>
      @import url(https://fonts.googleapis.com/css?family=Open+Sans:300);
* {{
  font-family: "Open Sans", sans-serif;
}}

body {{
  margin: 0;
  padding: 0;
  overflow: hidden;
  background:#00172D;
  background-repeat: no-repeat;
}}

.signupSection {{
  background: linear-gradient(to right, #0052A2, #00172D);
  
  background-repeat: no-repeat;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 1000px;
  height: 900px;
  text-align: center;
  display: flex;
  color: white;
  box-shadow: 3px 10px 20px 5px rgba(0, 0, 0, 0.5);
}}

.info {{
  width: 45%;
  background: rgba(20, 20, 20, 0.8);
  padding: 30px 0;
  border-right: 5px solid rgba(30, 30, 30, 0.8);
  h2 {{
    padding-top: 100px;
    font-weight: 300;
  }}
  p {{
    font-size: 18px;
  }}
  .icon {{
    font-size: 8em;
    padding: 20px 0;
    color: rgba(10, 180, 180, 1);
  }}
}}
label{{
  margin-right:30px;
  font-size: 20px;
}}
.details{{
    height: 100%;
    margin:auto;
    padding:30px;
}}
.signupForm {{
  width: 70%;
  padding: 30px 0;
  background: rgba(20, 40, 40, 0.8);
  transition: 0.2s;
  h2 {{
    font-weight: 300;
  }}
}}

.inputFields {{
  margin: 15px 0;
  font-size: 16px;
  padding: 10px;
  width: 250px;
  border: 1px solid rgba(10, 180, 180, 1);
  border-top: none;
  border-left: none;
  border-right: none;
  background: rgba(20, 20, 20, 0.2);
  color: white;
  outline: none;
}}

.noBullet {{
  list-style-type: none;
  padding: 0;
}}

#center-btn {{
  display: inline-block;
  margin: 0 10px;
}}
#join-btn {{
  border: 1px solid rgba(10, 180, 180, 1);
  background: rgba(20, 20, 20, 0.6);
  font-size: 18px;
  color: white;
  margin-top: 20px;
  padding: 10px 50px;
  cursor: pointer;
  transition: 0.4s;
  &:hover {{
    background: rgba(20, 20, 20, 0.8);
    padding: 10px 80px;
  }}
}}

    </style>
  

</head>
<body>
    <div class="signupSection">
        <div class="info">
            <div class="details">
                <h2>Mission to Save Crab</h2>
                <i class="icon ion-ios-ionic-outline" aria-hidden="true"></i>
                <p>The Future Is Here</p>
                 <h2>{res}</h2>
            </div>
         
        </div>
        <form  action="ContentController.py" class="signupForm" name="signupform">
          <h2>Crab Input</h2>
            <h2>{result}</h2>
          <ul class="noBullet">
            <li>
              <label for="sex">Sex</label>
              <input type="text" class="form-control inputFields" id="sex" name="sex" value="{sex}"  readonly>
          </li>
            <li>
              <label for="length">Length</label>
              <input type="text" class="form-control inputFields" id="length" name="length" value="{length}" readonly />
            </li>
            <li>
              <label for="diameter">Diameter</label>
              <input type="text" class="form-control inputFields" id="diameter" name="diameter" value="{diameter}" readonly>
            </li>
            <li>
              <label for="height">Height</label>
              <input type="text" class="form-control inputFields" id="height" name="height" value="{height}" readonly>
            </li>
            <li>
              <label for="weight">Weight</label>
              <input type="text" class="form-control inputFields" id="weight" name="weight" value="{weight}" readonly>
            </li>
            <li>
              <label for="shucked_weight">Shucked Weight</label>
              <input type="text" class="form-control inputFields" id="shucked_weight" name="shucked_weight" value="{shucked}" readonly>
            </li>
            <li>
              <label for="viscera_weight">Viscera Weight</label>
              <input type="text" class="form-control inputFields" id="viscera_weight" name="viscera_weight" value="{viscera}" readonly>
            </li>
            <li>
              <label for="shell_weight">Shell Weight</label>
              <input type="text" class="form-control inputFields" id="shell_weight" name="shell_weight" value="{shell}" readonly>
            </li>
            <li>
              <label for="age">Age</label>
              <input type="text" class="form-control inputFields" id="age" name="age" value="{age} months" readonly>
               <li id="center-btn">
               
                <input type="submit" id="join-btn" name="back" alt="back" value="Back" ">
            </li>
            </li>
               <li id="center-btn">
              <input type="submit" id="join-btn" name="clear" alt="clear" value="Clear">
            </li>
            
        
          </ul>
        </form>
      </div>
        
</body>
</html>
    """
    return inputForm


def home():
  home="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
  <link rel="stylesheet" href="index.css">
  <title>Crab Website</title>
  
  <style>
  @import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap");

:root {
  --primary-color: #3a4052;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Open Sans", sans-serif;
  line-height: 1.5;
}

a {
  text-decoration: none;
  color: var(--primary-color);
}

h1 {
  font-weight: 300;
  font-size: 60px;
  line-height: 1.2;
  margin-bottom: 15px;
}

.showcase {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: #fff;
  padding: 0 20px;
}

.video-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;

}

.video-container video {
  min-width: 100%;
  min-height: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  object-fit: cover;
}

.video-container:after {
  content: "";
  z-index: 1;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  position: absolute;
}

.content {
  z-index: 2;
}

.btn {
  display: inline-block;
  padding: 10px 30px;
  background: var(--primary-color);
  color: #fff;
  border-radius: 5px;
  border: solid #fff 1px;
  margin-top: 25px;
  opacity: 0.7;
}

.btn:hover {
  transform: scale(0.98);
}

#about {
  padding: 40px;
  text-align: center;
}

#about p {
  font-size: 1.2rem;
  max-width: 600px;
  margin: auto;
}

#about h2 {
  margin: 30px 0;
  color: var(--primary-color);
}

.social a {
  margin: 0 5px;
}

      .content {
      position: relative;
      z-index: 1;
      text-align: center;
    }

    .content h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
    }

    .content h3 {
      font-size: 1.5rem;
      margin-bottom: 2rem;

    }

    .content form {
      display: inline-block;
    }

    .content input[type="submit"] {
      padding: 10px 20px;
      margin: 10px;
      border: 2px solid #fff;
      background-color: transparent;
      color: #fff;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .content input[type="submit"]:hover {
      background-color: #fff;
      color: #000;
    }
  </style>
</head>
<body>
  <section class="showcase">
    <div class="video-container">
      <video src="../video/crabs.mp4" autoplay muted loop></video>
    </div>
    <div class="content">
      <form action="MyController.py">
        <h1>Crab Age Prediction</h1>
        <h3>Predict the crab age based on some attributes</h3>
        <input type ="submit" name ="ALL" value = "View Records"/>
        <input type ="submit" name ="ADD" value = "Add Record"/>
      </form>
  
    </div>
  </section>

 
</body>
</html>"""
  return home
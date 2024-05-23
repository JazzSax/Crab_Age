

def viewAll():
    viewAllString = '''


<!DOCTYPE html>
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

    .example button {
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
    }

    .example button:hover {
      background: #0b7dda;
    }
  </style>
 
</head>
<body>
<form class="example" action="">
    <input type="text" placeholder="Search.." name="search">
    <button type="submit"><i class="fa fa-search"></i></button>
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
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>XXD</td>
            <td>ADITYA BIRLA</td>
            <td>$1.02</td>
            <td>-1.01</td>
            <td>+2.36%</td>
            <td>ADITYA BIRLA</td>
            <td>$1.02</td>
            <td>-1.01</td>
            <td>+2.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAD</td>
            <td>AUSENCO</td>
            <td>$2.38</td>
            <td>-0.01</td>
            <td>-1.36%</td>
            <td>AUSENCO</td>
            <td>$2.38</td>
            <td>-0.01</td>
            <td>-1.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
          <tr>
            <td>AAC</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
            <td>AUSTRALIAN COMPANY </td>
            <td>$1.38</td>
            <td>+2.01</td>
            <td>-0.36%</td>
          </tr>
        
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
'''

    return viewAllString



def showForm():
    inputForm = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
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
        <form  action="controller/MyController.py" class="signupForm" name="signupform">
          <h2>Crab Input</h2>
          <ul class="noBullet">
            <li>
              <label for="sex"></label>
              <input type="text" class="form-control inputFields" id="sex" name="sex" placeholder="Sex" value=""  required>
          </li>
            <li>
              <label for="length"></label>
              <input type="text" class="form-control inputFields" id="length" name="length" placeholder="Length" value="" required />
            </li>
            <li>
              <label for="diameter"></label>
              <input type="text" class="form-control inputFields" id="diameter" name="diameter" placeholder="Diameter" value="" required>
            </li>
            <li>
              <label for="height"></label>
              <input type="text" class="form-control inputFields" id="height" name="height" placeholder="Height" value="" required>
            </li>
            <li>
              <label for="weight"></label>
              <input type="text" class="form-control inputFields" id="weight" name="weight" placeholder="Weight" value="" required>
            </li>
            <li>
              <label for="shucked_weight"></label>
              <input type="text" class="form-control inputFields" id="shucked_weight" name="shucked_weight" placeholder="Shucked Weight" value="" required>
            </li>
            <li>
              <label for="viscera_weight"></label>
              <input type="text" class="form-control inputFields" id="viscera_weight" name="viscera_weight" placeholder="Viscera Weight" value="" required>
            </li>
            <li>
              <label for="shell_weight"></label>
              <input type="text" class="form-control inputFields" id="shell_weight" name="shell_weight" placeholder="Shell Weight" value="" required>
            </li>
            <li>
              <label for="age"></label>
              <input type="text" class="form-control inputFields" id="age" name="age" placeholder="Age" value="" readonly>
            </li>
                 <li id="center-btn">
            <button type="button" id="join-btn" onclick="history.back()">Back</button>
            </li>
            <li id="center-btn">
              <input type="submit" id="join-btn" name="join" alt="Join" value="Predict">
            </li>
       
          </ul>
        </form>
      </div>
</body>
</html>

'''
    return inputForm
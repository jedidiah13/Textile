<?php 
include_once 'ups.rate.class.php'; 
include_once 'usps.php';
?>

<!--

Alrighty guys, here it is. The first draft of the UPS Shipping Calculator for the Tektiles Software
    Engineering project. 

-->
<!DOCTYPE html>
<html>
	<head>           
        <link rel="stylesheet" type="text/css" href="style.css" />
        <style>
            .center
            {
                margin:auto;
                width:70%;
            }
        </style>
        <title>UPS Calculator - Tektiles</title>
        <br>
        <table id = "InfoTable">
            <tr style="padding:5px">
                <td>Title</td>
                <td>:</td>
                <td>UPS Shipping Calculator</td>
            </tr><tr style="padding:5px">
                <td>Class</td>
                <td>:</td>
                <td>CSCI 4700 - Software Engineering</td>
            </tr><tr style="padding:5px">
                <td rowspan="2" valign="top">Summary<br></td>
                <td>:</td>
                <td>This page receives shipping / packaging input and creates an XML call with the data.</td>
            </tr><tr>                 
                <td></td>
                <td>This page displays the value that was returned from the UPS Rate Servers.</td>
            </tr>
        </table>
	</head>
    <br><hr><hr><br>
	<body>
        <?php
            
            function test_input($data){
                $data = trim($data);
                $data = stripslashes($data);
                $data = htmlspecialchars($data);
                return $data;
            }
        
            $objUpsRate = new UpsShippingQuote();
    
         /*   $strDestinationZip = test_input($_POST["varZip"]);
            $strMethodShortName = test_input($_POST["varShipping"]);
            $strPackageLength = test_input($_POST["varLen"]);
            $strPackageWidth = test_input($_POST["varWidth"]);
            $strPackageHeight = test_input($_POST["varHeight"]);
            $strPackageWeight = test_input($_POST["varWeight"]);
            $boolReturnPriceOnly = true;
        	$strUSPSWeight = test_input($_POST["USPSvarWeight"]);
            $strUSPSZip = test_input($_POST["USPSvarZip"]);*/

            $strDestinationZip = test_input($_POST["varZip"]);
            $strMethodShortName = test_input($_POST["varShipping"]);
            $strPackageLength = 12;
            $strPackageWidth = 12;
            $strPackageHeight = 6;
            $strPackageWeight = 5;
            $boolReturnPriceOnly = true;
        	$strUSPSWeight = 5;
            $strUSPSZip = test_input($_POST["varZip"]);
            $strUSPSShip = test_input($_POST["USPSvarShipping"]);
            
            switch($strUSPSShip) {
                case 'O':
                    $USPSCode = "PRIORITY MAIL EXPRESS";
                    break;
                case 'P':
                    $USPSCode = "PRIORITY";
                    break;
                default;
                    $USPSCode = "PRIORITY";
                    break;  
            }

            switch($strMethodShortName) { 
			case '1DM':            
				$strServiceCode = "Next Day Air Early AM"; 
				break; 
			case '1DA':            
				$strServiceCode = "Next Day Air"; 
				break;          
			case '1DP':            
				$strServiceCode = "Next Day Air Saver"; 
				break; 
			case '2DM':            
				$strServiceCode = "Second Day Air AM"; 
				break; 
			case '2DA':            
				$strServiceCode = "Second Day Air"; 
				break; 
			case '3DS':            
				$strServiceCode = "Three Day Select"; 
				break; 
			case 'GND':            
				$strServiceCode = "Ground"; 
				break; 
			case 'STD':            
				$strServiceCode = "Standard"; 
				break; 
			case 'XPR':            
				$strServiceCode = "Worldwide Express"; 
				break; 
			case 'XDM':            
				$strServiceCode = "Worldwide Express Plus"; 
				break; 
			case 'XPD':            
				$strServiceCode = "Worldwide Expedited"; 
				break; 
			default:            
				$strServiceCode = "Ground"; 
				break; 
            }
            $result = $objUpsRate->GetShippingRate(
                $strDestinationZip, 
                $strMethodShortName, 
                $strPackageLength, 
                $strPackageWidth,
                $strPackageHeight, 
                $strPackageWeight, 
                $boolReturnPriceOnly
            );
        ?>
        <form action= "" method = "post">
            <table id = "InputTable">
                <tr>
                    <th colspan="2">UPS Shipping Calculator</th>	
                </tr><tr>
                    <td colspan="2" style="font-size: 1.5em">Package Details</td>
                    <td colspan="2"><hr></td>
                </tr><tr>
                    <td> </td>
                    <td> </td>
                </tr><tr>
                    <td>Shipping Option:</td>
                    <td><?php echo $strServiceCode ?></td>
                </tr><tr>
                    <td>Destination Zip</td>
                    <td><?php echo $strDestinationZip ?></td>
                </tr><tr>
                    <td>Package Length (in.)</td>
                    <td><?php echo $strPackageLength ?> in.</td>
                </tr><tr>
                    <td>Package Width (in.)</td>
                    <td><?php echo $strPackageHeight ?> in.</td>
                </tr><tr>
                    <td>Package Height (in.)</td>
                    <td><?php echo $strPackageHeight ?> in.</td>                    
                </tr><tr>
                    <td>Package Weight (lbs.)</td>
                    <td><?php echo $strPackageWeight ?> .lbs</td>
                </tr><tr>
                    <td colspan="2"><hr></td>
                </tr><tr>
                    <td>Total UPS Shipping Cost:</td>
                    <td>$<?php echo $result ?></td>
                </tr><tr>
                	<td>Total USPS Shipping Cost:</td>
                	<td>$<?php echo USPSParcelRate($strUSPSWeight, $strUSPSZip, $USPSCode);?></td>
               </tr>
            </table>
        </form>
	</body>
</html>
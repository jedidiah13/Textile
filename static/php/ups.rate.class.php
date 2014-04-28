<?php
// This script was written with help from Mark Sanborn at http://www.marksanborn.net  

class UpsShippingQuote {
    
    # Hard Coded UPS Account information
	var $strAccessLicenseNumber = 'CCD014DD4CB4AC62';
	var $strUserId = 'jgriner0918';
    var $strPassword = 'From1248';
	var $strShipperNumber = 'R06535';
	var $strShipperZip = '37167';
	var $strDefaultServiceCode = '03'; // Ground Shipping
	var $strRateWebServiceLocation = 'https://www.ups.com/ups.app/xml/Rate'; // Production URL
	var $boolDebugMode = false;
    
	function UpsShippingQuote() { }
    
	private function GetServiceCode($strService='GND') {
		switch(strtoupper($strService)) { 
			case '1DM':            
				$strServiceCode = '14'; 
				break; 
			case '1DA':            
				$strServiceCode = '01'; 
				break;          
            case '1DP':            
				$strServiceCode = '13'; 
				break; 
			case '2DM':            
				$strServiceCode = '59'; 
				break; 
			case '2DA':            
				$strServiceCode = '02'; 
				break; 
			case '3DS':            
				$strServiceCode = '12'; 
				break; 
			case 'GND':            
				$strServiceCode = '03'; 
				break;
			default:            
				$strServiceCode = '03'; 
				break; 
		}
		return $strServiceCode;
	}  #exit GetServiceCode()

	public function GetShippingRate(    $strDestinationZip, $strServiceShortName='GND', 
                                        $strPackageLength=18, $strPackageWidth=12, 
                                        $strPackageHeight=4, $strPackageWeight=2, $boolReturnPriceOnly=true) {

		$strServiceCode = $this->GetServiceCode($strServiceShortName);

		$strXml ="<?xml version=\"1.0\"?>  
		<AccessRequest xml:lang=\"en-US\">  
			<AccessLicenseNumber>{$this->strAccessLicenseNumber}</AccessLicenseNumber>  
			<UserId>{$this->strUserId}</UserId>  
			<Password>{$this->strPassword}</Password>  
		</AccessRequest>  
		<?xml version=\"1.0\"?>  
		<RatingServiceSelectionRequest xml:lang=\"en-US\">  
			<Request>  
				<TransactionReference>  
					<CustomerContext>Bare Bones Rate Request</CustomerContext>  
					<XpciVersion>1.0001</XpciVersion>  
				</TransactionReference>  
				<RequestAction>Rate</RequestAction>  
				<RequestOption>Rate</RequestOption>  
			</Request>  
			<PickupType>  
				<Code>01</Code>  
			</PickupType>  
			<Shipment>  
				<Shipper>  
					<Address>  
						<PostalCode>{$this->strShipperZip}</PostalCode>  
						<CountryCode>US</CountryCode>  
					</Address>  
					<ShipperNumber>{$this->strShipperNumber}</ShipperNumber>  
				</Shipper>  
				<ShipTo>  
					<Address>  
						<PostalCode>{$strDestinationZip}</PostalCode>  
						<CountryCode>US</CountryCode>  
						<ResidentialAddressIndicator/>  
					</Address>  
				</ShipTo>  
				<ShipFrom>  
					<Address>  
						<PostalCode>{$this->strShipperZip}</PostalCode>  
						<CountryCode>US</CountryCode>  
					</Address>  
				</ShipFrom>  
				<Service>  
					<Code>{$strServiceCode}</Code>  
				</Service>  
				<Package>  
					<PackagingType>  
						<Code>02</Code>  
					</PackagingType>  
					<Dimensions>  
						<UnitOfMeasurement>  
							<Code>IN</Code>  
						</UnitOfMeasurement>  
						<Length>{$strPackageLength}</Length>  
						<Width>{$strPackageWidth}</Width>  
						<Height>{$strPackageHeight}</Height>  
					</Dimensions>  
					<PackageWeight>  
						<UnitOfMeasurement>  
							<Code>LBS</Code>  
						</UnitOfMeasurement>  
						<Weight>{$strPackageWeight}</Weight>  
					</PackageWeight>  
				</Package>  
			</Shipment>  
		</RatingServiceSelectionRequest>"; 

		$rsrcCurl = curl_init($this->strRateWebServiceLocation);  

		curl_setopt($rsrcCurl, CURLOPT_HEADER, 0);
		curl_setopt($rsrcCurl, CURLOPT_POST, 1);
		curl_setopt($rsrcCurl, CURLOPT_TIMEOUT, 60);
		curl_setopt($rsrcCurl, CURLOPT_RETURNTRANSFER, 1);  
		curl_setopt($rsrcCurl, CURLOPT_SSL_VERIFYPEER, 0);  
		curl_setopt($rsrcCurl, CURLOPT_SSL_VERIFYHOST, 0);  
		curl_setopt($rsrcCurl, CURLOPT_POSTFIELDS, $strXml);  

		$strResult = curl_exec($rsrcCurl);
		if($this->boolDebugMode) echo "<p>{$strResult}</p>";		

		$objResult = new SimpleXMLElement($strResult);
		if($this->boolDebugMode) print_r($objResult);

		curl_close($rsrcCurl);

		if($boolReturnPriceOnly) {
			return (string) $objResult->RatedShipment->TotalCharges->MonetaryValue;
		} else {
			return $objResult;
		}

	} # end method GetShippingRate()

} # end class UpsShippingQuote

?>

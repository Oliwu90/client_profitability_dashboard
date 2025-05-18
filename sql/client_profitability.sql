SELECT 
	c.clientname,
    w.clientreference,
    w.status as 'workorder_status',
    w.statusdate,
    w.ordereddate,
    w.approveddate,
    w.propertyid,
    v.vendorname,
    w.workordernumber,
    w.clientprice,
    w.vendorprice,
    p.status as 'property_status',
    w.state,
    w.postalcode,
    w.county


FROM worklist w
	LEFT JOIN client   c ON w.clientid = c.clientid
	LEFT JOIN vendor   v ON w.vendorid = v.vendorid
	LEFT JOIN investor i ON w.investorid = i.investorid 
	LEFT JOIN property p ON w.propertyid = p.propertyid
    
WHERE
    p.status NOT IN ("Closed", "Cancelled")
    and w.status IN ("Approved")
    and c.clientname REGEXP 'RMS|Loancare|Onity|Roundpoint|Valon|Cascade Financial|US Bank|M&T Bank|TD PreSale|Shellpoint'
    and YEAR(w.approveddate) >= YEAR(curdate()) - 5



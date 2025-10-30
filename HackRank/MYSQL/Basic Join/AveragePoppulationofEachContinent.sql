SELECT c.Continent, FLOOR(AVG(ci.Population))
FROM Country c
JOIN City ci 
ON c.Code = ci.CountryCode
GROUP BY c.Continent;

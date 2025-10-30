SELECT c.Continent, ci.Population
FROM Country c
JOIN City ci 
ON c.Code = ci.CountryCode

Select IF(A=B And B=C And C=A, "Equilateral", IF(A=B, IF(A+B=C, "Not A Triangle", "Isosceles") , IF(A!=B And B!=C And C!=A, IF(A+B<C, "Not A Triangle", "Scalene"), "Scalene"))) from TRIANGLES;

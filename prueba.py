def years_error(age,company_years):
        assert (age >= 18 and age <= 70),"Error introdugiste una edad invalida, la misma debe estar comprendida entre 18-70 años" 
        return age
        

age = 10 
company_years = 15

print(years_error(age,company_years))





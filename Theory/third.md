# Database keys

1-to uniquely identifya row
2-to enforce data integrity and constraints
3-to establish relationship b/w tables

# Types of keys:

table:
empid|cnic_no.|name|email|DOB|salary

keys can be :
{empid,cnic_no,email}

---

1-super{empid,cinic_no,email,empid+cinic_no,empod+email,email+empiid,empid+cnic+email}//keys possible combinations. All keys superset

2-candidate//min no.of cols i.e empid,cinic,email, and will reject combination like email+cnic as we can make a jey by only one col i.e email or cnic.

3-primary//that selected key to become a key.always unique , not null

4-foreign

5-composite//more than one keys i.e email+cnic

6-compound// that composite key where atleast one key is foreign key

7-alternate//other two keys i.e --> candidate - primary = alternate key

8-surrogate
name|city|Dob
can't make any one a key
so we will add one col name id on your own
so when u do not have key u create one its surrogate key

# good criteria

- unique
- not null
- numeric
- minimum

int main(){
	//Forme des expressions
	//		A
	//		A "operateur present dans OP" E
	int a;
	a=3+2;
	print(a);
	//Verification des priorités :
	a=3*2+4; //ATtendu : 10
	print(a);
	//a=1&&1; Attendu : non fonctionnel car && et || ne vont que dnas les if
	//Même chose avec division et ||
	a=4/2+4; //ATtendu : 6
	print(a);
	a=9%4%3; // ATtendu : 1;
	print(a);
	a=3*4/6; //Attendu : 2;
	print(a);
	
	//Verification priorite de la puissance
	a=2^2^3; //Attendu : 2^(2^3)
	print(a);
	a=2^2^3+4; //Attendu : 2^(2^3) + 4
	print(a);
	a=2^2^(1+1); //Attendu : 2^(2^(1+1))
	print(a);
	
	//Verification des opérateurs logiques 
	a= 4>5+58; //Attendu : 0
	print(a);
	a=0>=0;
	print(a);
	a=-5<7;
	print(a);

	//Verification des parentheses
	a=(2+4)*3;
	print(a);
	a=(((5*8+2)-4)*(-6))-(66 > 4);
	print(a);
	a=(4+5);
	print(a);

	//Verification des opérateurs logiques && et || et !
	a=4||0;
	print(a);
	a=1&&1;
	print(a);
	a=0&&1;
	print(a);
	a=(3>2) || (5<=4);
	print(a);
	a=!(3>2);
	print(a);
	a=!(0);
	print(a);
	a=2+3-5>=0 && !(56-56);
	print(a);
}

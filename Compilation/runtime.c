int puissance(int a, int b){
	int r;
	r=1;
	while(b!=0){
		r=r*a;
		b=b-1;

	}
	return r;
}

int free(int p){
	return 0;
}

int malloc(int n){
	int p;
	p=*0;
	*0=*0+n;
	return p;
}

int print_Sub(int n){
	if(n == 0){
		return 0;
	}
	int d;
	int r;
	d = n%10;
	r = n/10;
	print_Sub(r);
	send d+48;
}

int print(int n){
	if(n < 0){
		send 45;
		n = -n;
	}
	if(n == 0){
		send 48;
	}
	else{
		print_Sub(n);
	}
	//retour chariot
	send 10;
}

int scanf(){
	int res;int a;
	int signe;
	a = receive;
	if(a==45){
		signe=0;
		a = receive;
	}
	while(a != 10){
		res = res*10 + (a-48);
		a = receive;
	}
	if(signe == 0){
		res=-res;
	}
	return res;
}

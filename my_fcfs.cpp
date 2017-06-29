#include<iostream>
using namespace std;
int main(){
	int bt[20],tat[20],wt[20],n,i,j,avwt=0,avtat=0;
	cout<<"enter the number of process\n";
	cin>>n;
	cout<<"\nenter the bt\n";
	for(i=0;i<n;i++){
		cout<<"P["<<i+1<<"]:";
		cin>>bt[i];
	}
	//calulate wt()
	wt[0]=0;
	for(i=1;i<n;i++){
		wt[i]=0;
		for(j=0;j<i;j++)
		wt[i]+=bt[j];
	}
	cout<<"\nProcess\t\tburst time\twaiting time\tturnaround time";
	//calculate tat()
	for(i=0;i<n;i++){
		tat[i]=bt[i]+wt[i];
		avtat+=tat[i];
		avwt+=wt[i];
		cout<<"\nP["<<i+1<<"]"<<"\t\t"<<bt[i]<<"\t\t"<<wt[i]<<"\t\t"<<tat[i];
		
	}
	avwt/=i;
	avtat/=i;
	cout<<"\n\nAverage waiting time"<<avwt;
	cout<<"\nAverage Turnaround Time:"<<avtat;
 
    return 0;

	
	
}

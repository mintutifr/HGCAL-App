#include <string>
#include <vector>
#include <sstream>  //istringstream
#include <iostream> // cout
#include <fstream>  // ifstream

#include <TH2F.h> 
#include <TProfile.h> 
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TMath.h"

using namespace std;

void get_graph(int n, float x[],float y[]){

	TGraph* LHS = new TGraph(n,x,y);


    LHS->SetMarkerStyle(3);
	LHS->SetLineWidth(2);
	LHS->SetLineColor( 2 );
	LHS->SetLineWidth( 4 );
	LHS->SetMarkerColor( 4 );

    TCanvas *c1 = new TCanvas("c1","", 600,600,600,600);gStyle->SetOptFit();
    c1->cd();

    LHS->Draw("AP");

}


void analyse_data(string filedir = "offset_corrected_75_07042021/focused/CSV/",string csvfile = "csv_Hexaboard_87"){
cout<<filedir+csvfile<<endl;
  char inp[100], t[5];
  int  x, y, nrec=0, nL1=0, nL2=0, nL3=0;
  int  xx[2000], yy[2000];
  int  xL1[2000], yL1[2000], xL2[2000], yL2[2000], xL3[2000], yL3[2000];
  bool xy[520][400];
  TGraph *g1;

  for(int i=0; i<2000; i++){
    xx[i]=0;  yy[i]=0;   xL1[i]=0; yL1[i]=0;
    xL2[i]=0; yL2[i]=0;  xL3[i]=0; yL3[i]=0;
  }

  for(int iy=0; iy<400; iy++){
    for(int ix=0; ix<520; ix++){
        xy[ix][iy]=0;}
  }


  //Read the data and stire in an array
  string str = filedir+csvfile+".csv";
  const char *c = (str).c_str();
  cout<<c<<endl;
  FILE *f1 = fopen (c,"r");
  if(f1 == NULL){
	cout << "Error opening file" << endl;
	exit(1);
  } 

  fgets(inp,100, f1);
  for(int i=0; i<10000; i++){
	if (feof(f1))break;
	fgets(inp,100, f1);
	sscanf(inp, "%d%1s%d \n",  &y, t, &x);
	nrec++;
	//cout << "X: " << x << "   Y: " << y << "  nrec=" << nrec << endl;
    xx[i]=x;	yy[i]=y;
  }
  //now xx and yy has the xy cordinate stored

  xx[nrec-1]=0;   yy[nrec-1]=0; nrec--; //why it need to be set at 0 ???????????????????


  //Fill the xy matrix
  for(int j=0; j<nrec; j++){
    int i1 = xx[j], i2 = yy[j];
    xy[i1][i2]=1;
  }


  //Find the cluster in first row (y=0) 
  int xRow[515], xLS[5];
  int iStart=0, iLSx=0;
  for(int iy=0; iy<1; iy++){                 //why this loop is needful ????
    for(int i1=0; i1<515; i1++){xRow[i1]=0;}
    for(int i=iStart; i<nrec; i++){
      x= xx[i]; y=yy[i];
      if(y==iy){xRow[x]=1;}
      if(y>iy){iStart=i-1; break;}
    }

    for(int i1=0; i1<5; i1++){xLS[i1]=0;}
    iLSx=0;                                          // why it need to set to zero inside the loop even the loop cover it once
    for(int i2=0; i2<512; i2++){
      if(xRow[i2]==0 || i2<3)continue;
      int n1 = xRow[i2-2] + xRow[i2-1];
      if(n1==0){
        //cout << "AA  " << i2 << endl;
        int ihits=0, ix1=i2-2, ix2=i2+2, iy1=0, iy2=7;
        if(iy==0){
          //Count hits in 5x7 matrix
          for(int ky=iy1; ky<iy2; ky++){
            for(int kx=ix1; kx<=ix2; kx++){
              ihits = ihits+ xy[kx][ky];
              //cout << "AA  kx=" << kx << "  ky=" << ky;
             // cout << "    xy=" << xy[kx][ky] << "   ihits=" << ihits << endl;
            }
          }
          if(ihits>3){xLS[iLSx]=i2; iLSx++; cout << iLSx << "   ixs=" << i2 << endl;}
        }//if(iy==0){
        //cout << "y=" << y << "    xStart=" << i2 << endl;
      }
    }
  }
  //cout<<"iLSx = "<<iLSx<<endl;
  //Extract Points for Line-1  and Line-2
  for(int ils=0; ils<iLSx; ils++){
    int nwid=0;
    int xLSref=xLS[ils];
    //cout<<"xLSref = "<<xLSref<<endl;
    for(int iy=0; iy<400; iy++){
      for(int ix=0; ix<520; ix++){
        if(xy[ix][iy]==0)continue;
        if(fabs(xLSref-ix)<10){
          //cout << "ils=" << ils << "  iy=" << iy << "   ix=" << ix;
          //cout << "   xLSref=" << xLSref << endl;
          if(ils==0){xL1[nwid]=ix; yL1[nwid]=iy;}
          if(ils==1){xL2[nwid]=ix; yL2[nwid]=iy;}
          nwid++;
          xLSref = ix;
          xy[ix][iy]=0;
        }
      }//for(int ix=0; ix<520; ix++)
    }//for(int iy=0; iy<400; iy++)
    if(ils==0)nL1=nwid;
    if(ils==1)nL2=nwid;
  }//for(int ils=0; ils<iLSx; ils++)



  //Extract Points for Line 3
  int nwid=0;
  for(int iy=0; iy<400; iy++){
    for(int ix=0; ix<520; ix++){
      if(xy[ix][iy]==0)continue;
      //cout << "iy3=" << iy << "   ix3=" << ix << endl;
      xL3[nwid]=ix; yL3[nwid]=iy; nwid++;
    }//for(int ix=0; ix<520; ix++)
  }//for(int iy=0; iy<400; iy++)
  nL3=nwid;

 //Extract and Fit Line1A, Line1B, Line2A, Line2B and Line3A, Line3B points
  TCanvas *c1;
  c1 =new TCanvas("c1","Plots",0,0,400,300);
  c1->cd();
  TGraphErrors *gL1A, *gL1B, *gL2A, *gL2B, *gL3A, *gL3B;	
  TF1 *f_pol1A, *f_pol1B, *f_pol2A, *f_pol2B, *f_pol3A, *f_pol3B;
  f_pol1A = new TF1("f_pol1A","[1]*x + [0]", 0, 520);	//Straight line function
  f_pol1B = new TF1("f_pol1B","[1]*x + [0]", 0, 520);	//Straight line function
  f_pol2A = new TF1("f_pol2A","[1]*x + [0]", 0, 520);	//Straight line function
  f_pol2B = new TF1("f_pol2B","[1]*x + [0]", 0, 520);	//Straight line function
  f_pol3A = new TF1("f_pol3A","[1]*x + [0]", 0, 520);	//Straight line function
  f_pol3B = new TF1("f_pol3B","[1]*x + [0]", 0, 520);	//Straight line function

  float xL1A[400], yL1A[400], xL1B[400], yL1B[400], err[400];
  float xL2A[400], yL2A[400], xL2B[400], yL2B[400];
  float xL3A[400], yL3A[400], xL3B[400], yL3B[400];
  
  int npt1A=0, npt1B=0, npt2A=0, npt2B=0, npt3A=0, npt3B=0;
  for(int i=0; i<400; i++){
    xL1A[i]=0; yL1A[i]=0; xL1B[i]=0; yL1B[i]=0; err[i]=0.2;
    xL2A[i]=0; yL2A[i]=0; xL2B[i]=0; yL2B[i]=0;
    xL3A[i]=0; yL3A[i]=0; xL3B[i]=0; yL3B[i]=0;
  }


  //Fit Line 1A and 1B
  for(int i=0; i<nL1; i++){
    int ix=xL1[i], iy=yL1[i];
    if(iy>40)continue;                   //this is implimented by hand
    xL1A[npt1A]=ix;  yL1A[npt1A]=iy; npt1A++;
    //cout << i << "   npt1A=" << npt1A << "   ix=" << ix << "   iy=" << iy << endl;
  }
  //get_graph(npt1A,xL1A,yL1A);
  gL1A = new TGraphErrors(npt1A, xL1A, yL1A, err, err);
  f_pol1A->SetParameters(5000, -40);	gL1A->Draw("a*");	gL1A->Fit("f_pol1A"); 
  TF1 *fL1A = gL1A->GetFunction("f_pol1A");
  float p0_L1A = fL1A->GetParameter(0);	float p0_L1A_err = fL1A->GetParError(0);
  double m_L1A = fL1A->GetParameter(1);	float m_L1A_err  = fL1A->GetParError(1);
  cout << "p0_L1A=" << p0_L1A << "   p1_L1A=" << m_L1A << "  x0=";
  cout << -p0_L1A/m_L1A << endl << endl << endl;

  for(int i=0; i<nL1; i++){
    int ix=xL1[i], iy=yL1[i];
    if(ix>50)continue;                       //this is implimented by hand
    xL1B[npt1B]=ix;  yL1B[npt1B]=iy; npt1B++;
    //cout << i << "   npt1B=" << npt1B << "   ix=" << ix << "   iy=" << iy << endl;
  }
  gL1B = new TGraphErrors(npt1B, xL1B, yL1B, err, err);
  f_pol1B->SetParameters(200, -1);	gL1B->Draw("a*");	gL1B->Fit("f_pol1B");
  TF1 *fL1B = gL1B->GetFunction("f_pol1B");
  float p0_L1B = fL1B->GetParameter(0);	float p0_L1B_err = fL1B->GetParError(0);
  double m_L1B = fL1B->GetParameter(1);	float m_L1B_err  = fL1B->GetParError(1);
  cout << "p0_L1B=" << p0_L1B << "   p1_L1B=" << m_L1B << endl << endl << endl;


  //Fit Line 2A and 2B
  for(int i=0; i<nL2; i++){
    int ix=xL2[i], iy=yL2[i];
    if(iy>40)continue;                            //this is implimented by hand
    xL2A[npt2A]=ix;  yL2A[npt2A]=iy; npt2A++;
  }
  gL2A = new TGraphErrors(npt2A, xL2A, yL2A, err, err);
  f_pol2A->SetParameters(-1000, 40);	gL2A->Draw("a*");	gL2A->Fit("f_pol2A"); 
  TF1 *fL2A = gL2A->GetFunction("f_pol2A");
  float p0_L2A = fL2A->GetParameter(0);	float p0_L2A_err = fL2A->GetParError(0);
  double m_L2A = fL2A->GetParameter(1);	float m_L2A_err  = fL2A->GetParError(1);
  cout << "p0_L2A=" << p0_L2A << "   p1_L2A=" << m_L2A << endl << endl << endl;

  for(int i=0; i<nL2; i++){
    int ix=xL2[i], iy=yL2[i];
    if(ix<450)continue;                             //this is implimented by hand
    //cout << i << "   npt2B=" << npt2B << "   ix=" << ix << "   iy=" << iy << endl;
    xL2B[npt2B]=ix;  yL2B[npt2B]=iy; npt2B++;
  }
  gL2B = new TGraphErrors(npt2B, xL2B, yL2B, err, err);
  f_pol2B->SetParameters(200, -1);	gL2B->Draw("a*");	gL2B->Fit("f_pol2B");
  TF1 *fL2B = gL2B->GetFunction("f_pol2B");
  float p0_L2B = fL2B->GetParameter(0);	float p0_L2B_err = fL2B->GetParError(0);
  double m_L2B = fL2B->GetParameter(1);	float m_L2B_err  = fL2B->GetParError(1);
  cout << "p0_L2B=" << p0_L2B << "   p1_L2B=" << m_L2B << endl << endl << endl;


  //Fit Line 3A and 3B
  int x0L1A = 60 + -p0_L1A/m_L1A,    x0L2A = -p0_L2A/m_L2A;           //this is implimented by hand
  cout << "AAA   x0L1A=" << x0L1A << "    x0L2A=" << x0L2A << endl;
  for(int i=0; i<nL3; i++){
    int ix=xL3[i], iy=yL3[i];
    if(ix>x0L1A || iy<5)continue;
    xL3A[npt3A]=ix;  yL3A[npt3A]=iy; npt3A++;
    //cout << i << "   npt3A=" << npt3A << "   ix=" << ix << "   iy=" << iy << endl;
  }
  gL3A = new TGraphErrors(npt3A, xL3A, yL3A, err, err);
  f_pol3A->SetParameters(500, -1);	gL3A->Draw("a*");	gL3A->Fit("f_pol3A"); 
  TF1 *fL3A = gL3A->GetFunction("f_pol3A");
  float p0_L3A = fL3A->GetParameter(0);	float p0_L3A_err = fL3A->GetParError(0);
  double m_L3A = fL3A->GetParameter(1);	float m_L3A_err  = fL3A->GetParError(1);
  cout << "p0_L3A=" << p0_L3A << "   p1_L3A=" << m_L3A << endl << endl << endl;

  for(int i=0; i<nL3; i++){
    int ix=xL3[i], iy=yL3[i];
    if(ix<x0L2A)continue;
    xL3B[npt3B]=ix;  yL3B[npt3B]=iy; npt3B++;
    //cout << i << "   npt3B=" << npt3B << "   ix=" << ix << "   iy=" << iy << endl;
  }
  gL3B = new TGraphErrors(npt3B, xL3B, yL3B, err, err);
  f_pol3B->SetParameters(600, 1);	gL3B->Draw("a*");	gL3B->Fit("f_pol3B");
  TF1 *fL3B = gL3B->GetFunction("f_pol3B");
  float p0_L3B = fL3B->GetParameter(0);	float p0_L3B_err = fL3B->GetParError(0);
  double m_L3B = fL3B->GetParameter(1);	float m_L3B_err  = fL3B->GetParError(1);
  cout << "p0_L3B=" << p0_L3B << "   p1_L3B=" << m_L3B << endl;


  //ax+by+c = 0   mx-y+c = 0  a=m b=-1 c=c
  //x = b1c2−b2c1/a1b2−a2b1;      y = a2c1−a1c2/a1b2−a2b1;
  //x = (-c2+c1)/(-a1+a2);        y = (a2c1−a1c2)/(-a1+a2);
  //x = (-c2+c1)/(a2-a1);         y = (a2c1−a1c2)/(a2-a1);

  //x = (-p0_L1B + p0_L1A)/(m_L1B  - m_L1B)
  //y = (m_L1B*p0_L1A - m_L1A*p0_L1B)/(m_L1B  - m_L1B)

  //TLine *line = new TLine(-3,ymax,3,ymax);
  //line->SetLineColor(kRed);   line->Draw();

  //Get the intersection points
  float int_xL1 = (-p0_L1B+p0_L1A)/(m_L1B-m_L1A);
  float int_yL1 = (m_L1B*p0_L1A-m_L1A*p0_L1B)/(m_L1B-m_L1A);
  float xxL1A = -p0_L1A/m_L1A; float yyL1A=0;
  float xxL1B = 0; float yyL1B=p0_L1B;
  cout << "int_xL1=" << int_xL1 << "    int_yL1=" << int_yL1 << endl;

  float int_xL2 = (-p0_L2B + p0_L2A)/(m_L2B-m_L2A);
  float int_yL2 = (m_L2B*p0_L2A-m_L2A*p0_L2B)/(m_L2B-m_L2A);
  float xxL2A = -p0_L2A/m_L2A; float yyL2A=0;
  float xxL2B = 512; float yyL2B= m_L2B*xxL2B + p0_L2B;
  cout << "int_xL2=" << int_xL2 << "    int_yL2=" << int_yL2 << endl;

  float int_xL3 = (-p0_L3B + p0_L3A)/(m_L3B-m_L3A);
  float int_yL3 = (m_L3B*p0_L3A-m_L3A*p0_L3B)/(m_L3B-m_L3A);
  float yyL3A=400; float xxL3A = (yyL3A-p0_L3A)/m_L3A;
  float yyL3B=400; float xxL3B = (yyL3B-p0_L3B)/m_L3B;
  cout << "int_xL3=" << int_xL3 << "    int_yL3=" << int_yL3 << endl;


  //Plot Results
  cout << "nL1=" << nL1 << "  nL2=" << nL2 << "  nL3=" << nL3 << endl;
  c1->Clear(); c1->cd();
  g1 = new TGraph(nrec, xx, yy);
  g1->GetXaxis()->SetTitle("Pixel #");  g1->GetYaxis()->SetTitle("Pixel #");
  g1->DrawClone("A*");

  TLine *line1A = new TLine(xxL1A, yyL1A, int_xL1, int_yL1);
  line1A->SetLineColor(kRed); line1A->SetLineWidth(3); line1A->DrawClone("same");
  TLine *line1B = new TLine(xxL1B, yyL1B, int_xL1, int_yL1);
  line1B->SetLineColor(kRed); line1B->SetLineWidth(3); line1B->DrawClone("same");

  TLine *line2A = new TLine(xxL2A, yyL2A, int_xL2, int_yL2);
  line2A->SetLineColor(kRed); line2A->SetLineWidth(3); line2A->DrawClone("same");
  TLine *line2B = new TLine(xxL2B, yyL1B, int_xL2, int_yL2);
  line2B->SetLineColor(kRed); line2B->SetLineWidth(3); line2B->DrawClone("same");

  TLine *line3A = new TLine(xxL3A, yyL3A, int_xL3, int_yL3);
  line3A->SetLineColor(kRed);   line3A->SetLineWidth(3); line3A->DrawClone("same");
  TLine *line3B = new TLine(xxL3B, yyL3B, int_xL3, int_yL3);
  line3B->SetLineColor(kRed);   line3B->SetLineWidth(3); line3B->DrawClone("same");


  TLine *line12 = new TLine(int_xL1, int_yL1, int_xL2, int_yL2);
  line12->SetLineColor(kBlue);  line12->SetLineWidth(3); line12->DrawClone("same");

  TLine *line23 = new TLine(int_xL2, int_yL2, int_xL3, int_yL3);
  line23->SetLineColor(kBlue);  line23->SetLineWidth(3); line23->DrawClone("same");

  TLine *line31 = new TLine(int_xL3, int_yL3, int_xL1, int_yL1);
  line31->SetLineColor(kBlue);    line31->SetLineWidth(3); line31->DrawClone("same");

  

  //fL1A->SetMaximum(150);    fL1A->DrawClone("same"); 
  //fL1B->SetRange(0, 200);   fL1B->DrawClone("same");
  //fL2A->SetMaximum(150);    fL2A->DrawClone("same"); 
  //fL2B->SetRange(300, 520); fL2B->DrawClone("same");
  //fL3A->SetRange(0, 250);   fL3A->DrawClone("same"); 
  //fL3B->SetRange(200, 475); fL3B->DrawClone("same");
 
 //gL1B->Draw("AP"); //fL1A->Draw("same");

  string png = string(filedir+"centroid/centroiad_"+csvfile)+".png";
  /*string pdf = string(filedir+csvfile)+".pdf";
  string cpp = string(filedir+csvfile)+".C";*/
  c1->SaveAs(png.c_str());
  /*c1->SaveAs(pdf.c_str());
  c1->SaveAs(cpp.c_str());*/
}

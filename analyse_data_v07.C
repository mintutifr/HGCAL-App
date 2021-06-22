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
#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int Project(int imin, int imax, int xyProj[520], int& nBlk, int nBlkS[10], int nBlkE[10], int nBlkW[10]){
  int jBlk, jBlkS[10], jBlkE[10], jBlkW[10];
  nBlk=0; jBlk=0;
  for(int i=0; i<10; i++){nBlkS[i]=-1; nBlkE[i]=-1; nBlkW[i]=-1;}
  for(int i=0; i<10; i++){jBlkS[i]=-1; jBlkE[i]=-1; jBlkW[i]=-1;}
  for(int i=imin; i<=imax; i++){
    if(xyProj[i]==0)continue;
    if(jBlk>8)continue;
    if(i==0){jBlkS[jBlk]=i; jBlk++; continue;}
    if(xyProj[i-1]==0){jBlkS[jBlk]=i; jBlk++;}
    if(xyProj[i+1]==0){jBlkE[jBlk-1]=i;}
  }

  if(jBlk==1){
    nBlkS[0]=jBlkS[0];  nBlkE[0]=jBlkE[0]; nBlk=1;
  }
  
  //Merge block if spacing between successive blocks is small (<=3)
  if(jBlk>1){
  
    for(int i=0; i<jBlk; i++){
      int iStart=jBlkS[i], iEnd=jBlkE[i];
      //cout << "SRDOriginal:  "  << jBlk << "  i=" << i << "  S=" << iStart << "  E=" << iEnd << endl;
    }

    int iflag=0;
    for(int i=0; i<jBlk; i++){
      int iStart1=jBlkS[i], iEnd1=jBlkE[i];
      int iStart2, iEnd2;
      nBlkS[i-iflag] = iStart1;  nBlkE[i-iflag] = iEnd1; nBlk++;
      //cout << "SRDA:  "  << jBlk << "  i=" << i << "  S=" << iStart1 << "  E=" << iEnd1 << "  " << nBlk << endl;
      if(i==jBlk-1)continue;
      iStart2=jBlkS[i+1]; iEnd2=jBlkE[i+1];
      int idiff = iStart2 - iEnd1;
      if(idiff<4){
        iflag++;
        nBlkE[i]=iEnd2;
        //cout << "MergingSRDA:  "  << jBlk << "  i=" << i << "  S=" << iStart1 << "  E=" << iEnd2 << "  " << nBlk << endl;
        i++; continue;
      }
      //nBlkS[i+1]=iStart2;  nBlkE[i+1]=iEnd2; nBlk++;
      //cout << "SRDB:  "  << jBlk << "  i=" << i+1 << "  S=" << iStart2 << "  E=" << iEnd2;
      //cout << "  " << nBlk << "   iflag=" << iflag << endl;
    }

    //cout << endl;
    for(int i=0; i<nBlk; i++){
      int iStart=nBlkS[i], iEnd=nBlkE[i];
      //cout << "SRDFinal:  nBlk="  << nBlk << "  i=" << i << "  S=" << iStart << "  E=" << iEnd << endl;
    }


  }//if(jBlk>1){
  
  return nBlk;
}


int analyse_data_v07(string filedir = "offset_corrected_75_07042021/focused/CSV/csv_Focused/",string csvfile = "csv_Hexaboard_216",double *slopanderror = NULL){
  cout<<"-----------------------------begin-----"<<endl;
  cout<<filedir<<","<<csvfile<<endl;
  cout<<"-----------------------------endl-----"<<endl;
  cout<<csvfile.substr(csvfile.find("_",4)+1)<<endl;

  int imageNo = stoi(csvfile.substr(csvfile.find("_",4)+1)); 
  //int imageNo = int(csvfile.substr(csvfile.find("_",4)+1));
  int holeNo = int(imageNo/5)+1;
  cout <<"ImageNo is "<< imageNo << '\n';
  cout <<"HoleNo is "<< holeNo << '\n';
  //int nn = stoi(csvfile);
  //cout<< nn <<nn - 1<<endl;
  for (unsigned i=0; i<csvfile.length(); ++i)
  {
    //std::cout << csvfile.at(nn-1);
  }
  char in_dirpath[150], out_dirpath1[150], out_dirpath2[150];
  char fi1_name[70], fo1_name[70];
  char inpF[150], outF[150], lineStr[100], tmp[5];
  char hname[50];
  cout << "char defined"<<endl;
  int  x, y, nrec=0, nL1pt=0, nL2pt=0, nL3pt=0;
  int  xx[2000], yy[2000];
  int  xL1[2000], yL1[2000], xL2[2000], yL2[2000], xL3[2000], yL3[2000];
  int  nskip=0;
  cout << "Int defined"<<endl;
  bool xy[520][400], xy_filter[520][400];
  cout << "bool defined"<<endl;
  TGraph *g1;
  TGraphErrors *gL1A, *gL1B, *gL2A, *gL2B, *gL3A, *gL3B;	
  TF1 *f_pol1A, *f_pol1B, *f_pol2A, *f_pol2B, *f_pol3A, *f_pol3B;

  TH1F *histL1X[80], *histL1Y[80], *histL2X[80];
  TH1F *histL2Y[80], *histL3X[80], *histL3Y[80];
  cout << "hist defined"<<endl;
  TCanvas *c1;
  c1 =new TCanvas("c1","Plots",0,0,400,300);
  
  FILE *fptr;
  strcpy(in_dirpath, filedir.c_str()); 
  //sprintf(in_dirpath,   filedir.c_str());
  sprintf(out_dirpath1, "check/dirpath1/");
  sprintf(out_dirpath2, "check/dirpath2/");
  int iboard=5, ipass=1;
  cout<<"iboard = "<<iboard<<" "<<"ipass = "<<ipass<<endl;
  sprintf(fo1_name, "Hexaboard_%03d_Pass_%d_Image_%d.root", iboard, ipass,imageNo);
  cout << fo1_name << endl;
  sprintf(outF, "%s%s", out_dirpath2, fo1_name);
  cout << outF << endl;
  TFile *hfile = new TFile(outF, "recreate");

  sprintf(fo1_name, "Hexaboard_%03d_Pass_%d_Image_%d.txt", iboard, ipass,imageNo);
  cout << fo1_name << endl;
  sprintf(outF, "%s%s", out_dirpath2, fo1_name);
  cout << outF << endl;
  fptr = fopen(outF, "w");
  if(fptr == NULL){printf("Error!");exit(1);}

  cout<<"check1"<<endl;
  fprintf(fptr,"%s\n", outF);

  sprintf(outF,"L1: 1:Hole#,  2:FileIDX, # of points on 3:L1A, 4:L1B,   5:L2A, 6:L2B,  7:L3A, 8:L3B");
  fprintf(fptr,"%s\n", outF);

  sprintf(outF,"L2: 1:Hole#,  2:FileIDX, 3-6: Intercept and Slope for L1A and L1B");
  fprintf(fptr,"%s\n", outF);

  sprintf(outF,"L3: 1:Hole#,  2:FileIDX, 3-6: Intercept and Slope for L2A and L2B");
  fprintf(fptr,"%s\n", outF);

  sprintf(outF,"L4: 1:Hole#,  2:FileIDX, 3-6: Intercept and Slope for L3A and L3B");
  fprintf(fptr,"%s\n", outF);

  sprintf(outF,"L5: 1:Hole#,  2:FileIDX, 3-6: (X,Y) coordinate of Frame_Center and Centroid");
  fprintf(fptr,"%s\n\n", outF);


  int File_Idx[80];
  File_Idx[0]  =  32;    File_Idx[1]  =  92;   File_Idx[2]  = 117;    File_Idx[3]  = 147;
  File_Idx[4]  = 187;    File_Idx[5]  = 197;   File_Idx[6]  = 202;    File_Idx[7]  = 216;

  //File_Idx[0]  = 2;    File_Idx[1]  = 7;    File_Idx[2]  = 12;    File_Idx[3]  = 17;
  //File_Idx[4]  = 22;   File_Idx[5]  = 27;   File_Idx[6]  = 32;    File_Idx[7]  = 38; 
  File_Idx[8]  = 43;   File_Idx[9]  = 57;   File_Idx[10] = 62;    File_Idx[11] = 67; 
  File_Idx[12] = 72;   File_Idx[13] = 77;   File_Idx[14] = 82;    File_Idx[15] = 87; 
  File_Idx[16] = 92;   File_Idx[17] = 96;   File_Idx[18] = 102;   File_Idx[19] = 107; 
  File_Idx[20] = 112;  File_Idx[21] = 117;  File_Idx[22] = 122;   File_Idx[23] = 128; 
  File_Idx[24] = 132;  File_Idx[25] = 137;  File_Idx[26] = 141;   File_Idx[27] = 147; 
  File_Idx[28] = 152;  File_Idx[29] = 157;  File_Idx[30] = 162;   File_Idx[31] = 167; 
  File_Idx[32] = 171;  File_Idx[33] = 176;  File_Idx[34] = 181;   File_Idx[35] = 187; 
  File_Idx[36] = 192;  File_Idx[37] = 197;  File_Idx[38] = 202;   File_Idx[39] = 207; 
  File_Idx[40] = 211;  File_Idx[41] = 216;  File_Idx[42] = 222;   File_Idx[43] = 228; 
  File_Idx[44] = 232;  File_Idx[45] = 237;  File_Idx[46] = 242;   File_Idx[47] = 247; 
  File_Idx[48] = 253;  File_Idx[49] = 257;  File_Idx[50] = 262;   File_Idx[51] = 267;
  
  File_Idx[52] = 272;
  File_Idx[53] = 277;  File_Idx[54] = 282;  File_Idx[55] = 287;   File_Idx[56] = 292; 
  File_Idx[57] = 296;  File_Idx[58] = 302;  File_Idx[59] = 307;   File_Idx[60] = 312; 
  File_Idx[61] = 317;  File_Idx[62] = 323;  File_Idx[63] = 328;   File_Idx[64] = 333; 
  File_Idx[65] = 336;  File_Idx[66] = 342;  File_Idx[67] = 348;   File_Idx[68] = 353; 
  File_Idx[69] = 358;  File_Idx[70] = 362;  File_Idx[71] = 367;   File_Idx[72] = 372;


  // 22 Wrong Image, therefor not processed
  // 062   167q  317q
  // 32  62  92  117  147  187  197  202  216   242  317   333

  int iHole=0, iFile=0;
  //for(int fidx=0; fidx<8; fidx++){
  //for(int fidx=0; fidx<73; fidx++){
    //int idxx=File_Idx[fidx];
    int idxx=imageNo;
    //int fidx=0;
    int fidx=holeNo-1;
    iHole = holeNo; iFile=idxx;
    //if(iFile==22)continue;   //Skip as program crashes
    sprintf(hname, "histL1X_%02d", idxx);
    histL1X[fidx] = new TH1F(hname, "L1: X axis Projection", 520, 0, 520);

    sprintf(hname, "histL2X_%02d", idxx);
    histL2X[fidx] = new TH1F(hname, "L2: X axis Projection", 520, 0, 520);

    sprintf(hname, "histL3X_%02d", idxx);
    histL3X[fidx] = new TH1F(hname, "L3: X axis Projection", 520, 0, 520);

    sprintf(hname, "histL1Y_%02d", idxx);
    histL1Y[fidx] = new TH1F(hname, "L1: Y axis Projection", 420, 0, 420);

    sprintf(hname, "histL2Y_%02d", idxx);
    histL2Y[fidx] = new TH1F(hname, "L2: Y axis Projection", 420, 0, 420);

    sprintf(hname, "histL3Y_%02d", idxx);
    histL3Y[fidx] = new TH1F(hname, "L3: Y axis Projection", 420, 0, 420);

    for(int i=0; i<2000; i++){
      xx[i]=0;  yy[i]=0;   xL1[i]=0; yL1[i]=0;
      xL2[i]=0; yL2[i]=0;  xL3[i]=0; yL3[i]=0;
    }
    for(int iy=0; iy<400; iy++){
      for(int ix=0; ix<520; ix++){xy[ix][iy]=0; xy_filter[ix][iy]=0;}
    }
    nrec=0; nL1pt=0; nL2pt=0; nL3pt=0;
    cout<<idxx<<endl;
    sprintf(fi1_name, "Hexaboard_%d.csv", idxx);
    cout<<fi1_name<<endl;
    sprintf(inpF, "%s%s", in_dirpath,  fi1_name);
    cout << inpF << endl;

    sprintf(fo1_name, "Hexaboard_%03d.png", idxx);
    sprintf(outF, "%s%s", out_dirpath1, fo1_name);
    cout << outF << endl;

    //Read the data and store in an array
    FILE *f1 = fopen (inpF,"r");
    if(f1 == NULL){
	  cout << "Error opening file "<<inpF << endl;
	  exit(1);
    } 

    int frame_x=0, frame_y=0;
    fgets(lineStr, 100, f1);
    for(int i=0; i<10000; i++){
	  if (feof(f1))break;
	  fgets(lineStr, 100, f1);
	  sscanf(lineStr, "%d%1s%d \n",  &y, tmp, &x);
      xy[x][y]=1;      xy_filter[x][y]=1;
      if(x>frame_x){frame_x=x;}
      if(y>frame_y){frame_y=y;}
    }

    //Remove Edge noise in the frame
    for(int iy=0; iy<=frame_y; iy++){
      for(int ix=0; ix<=frame_x; ix++){
        if(ix<2 || iy<2){xy[ix][iy]=0; xy_filter[ix][iy]=0;}
      }
    }


    for(int iy1=0; iy1<400; iy1++){
      for(int ix1=0; ix1<520; ix1++){
        if(xy[ix1][iy1]==0)continue;
        xx[nrec]=ix1; yy[nrec]=iy1; nrec++;
        //cout << "ix=" << ix1 << "   iy=" << iy1 << "   nrec=" << nrec << endl;
      }
    }
    xx[nrec-1]=0;   yy[nrec-1]=0;  nrec--;
    


    int yProj[520], xProj[520], imin,      imax;
    int nBlkS[10],  nBlkE[10],  nBlkW[10], iBlk,      nCluster;
    int L1Xmin=-1,  L1Xmax=-1,  L2Xmin=-1, L2Xmax=-1, L12Ymin=-1;
    int L12Ymax=-1, L3Ymin=-1,  L3Ymax=-1;

    //Find Y demarcation between L3 and L1/L2
    for(int i=0; i<520; i++){xProj[i]=0; yProj[i]=0;}    
    for(int iy=0; iy<frame_y; iy++){
      for(int ix=0; ix<frame_x; ix++){
        if(xy[ix][iy]==1){yProj[iy]=1;}
      }
      //cout << iy << "    " << yProj[iy] << endl;
    }

    imin=0; imax=frame_y; iBlk=0; nCluster=0;
    //cout << "AAA 001" << endl;
    Project(imin, imax, yProj, iBlk, nBlkS, nBlkE, nBlkW);    
    cout << endl << "Y demarcation between L3 and L1/L2" << endl;
    for(int i=0; i<iBlk; i++){
      nBlkW[i]=nBlkE[i]-nBlkS[i]+1;
      cout << "yBlock=" << i << "  Start:" << nBlkS[i] << "   End:" << nBlkE[i];
      cout << "   Width:" << nBlkW[i] << endl;
      if(nBlkW[i]<40)continue;
      nCluster++;
      if(nCluster==1){L12Ymin=nBlkS[i]; L12Ymax=nBlkE[i];}
      if(nCluster==2){L3Ymin=nBlkS[i];  L3Ymax=nBlkE[i];}
    }


    //Find X demarcation between L1 and L2
    for(int i=0; i<520; i++){xProj[i]=0; yProj[i]=0;}
    for(int ix=0; ix<frame_x; ix++){
      for(int iy=0; iy<frame_y; iy++){
        if(xy[ix][iy]==0 || iy>L12Ymax)continue;
        xProj[ix]=1;
      }
      //cout << ix << "    " << xProj[ix] << "  " << L12Ymax << endl;
    }

    imin=0; imax=frame_x; iBlk=0; nCluster=0;
    //cout << "AAA 002" << endl;
    Project(imin, imax, xProj, iBlk, nBlkS, nBlkE, nBlkW);
    cout << endl << "X demarcation between L1 and L2   " << endl;
    for(int i=0; i<iBlk; i++){
      nBlkW[i]=nBlkE[i]-nBlkS[i]+1;
      cout << "xBlock=" << i << "  Start:" << nBlkS[i] << "   End:" << nBlkE[i];
      cout << "   Width:" << nBlkW[i] << endl;
      if(nBlkW[i]<60)continue;
      nCluster++;
      if(nCluster==1){L1Xmin=nBlkS[i];  L1Xmax=nBlkE[i];}
      if(nCluster==2){L2Xmin=nBlkS[i];  L2Xmax=nBlkE[i];}
    }
    
    
    cout << endl;
    cout << "L1Xmin="     << L1Xmin  << "   L1Xmax="  << L1Xmax;
    cout << "   L2Xmin="  << L2Xmin  << "   L2Xmax="  << L2Xmax;
    cout << "   L12Ymin=" << L12Ymin << "   L12Ymax=" << L12Ymax;
    cout << "   L3Ymin="  << L3Ymin  << "   L3Ymax="  << L3Ymax<< endl;


    //Remove horizontal noise in L1A (vertical) region
    int ivert1 =0;
    for(int iy=0; iy<10; iy++){
      int kk=0;
      for(int ix=0; ix<=L1Xmax; ix++){
        if(xy[ix][iy]==1){kk++;}
      }
      if(kk>10){
        for(int ix=0; ix<=L1Xmax; ix++){xy_filter[ix][iy]=0;}
      }
    }


    //Remove horizontal noise in L1A (vertical) region
    for(int ix=L1Xmax; ix>L1Xmax-7; ix--){
      int kk=0;
      for(int iy=0; iy<=L12Ymax; iy++){
        if(xy[ix][iy]==1){kk++;}
      }
      if(kk<=2){
        ivert1++;
        for(int iy=0; iy<=L12Ymax; iy++){xy_filter[ix][iy]=0;}
      }
    }


    //Remove noise for L1 region
    int ireset =0;
    for(int ix=0; ix<L1Xmax-8-ivert1; ix++){
      int kk=0;
      for(int i=0; i<520; i++){xProj[i]=0; yProj[i]=0;}    
      for(int iy=0; iy<=L12Ymax; iy++){
        if(xy[ix][iy]==1){yProj[iy]=1; kk++;}
      }
      int idiff = L1Xmax-ix;
      if(kk<4 && idiff<8){
        for(int iy=0; iy<=L12Ymax; iy++){xy_filter[ix][iy]=0;}
        ireset++;
        kk=0;
      }
      if(kk>1){
        imin=0; imax=L12Ymax; iBlk=0; nCluster=0;
        Project(imin, imax, yProj, iBlk, nBlkS, nBlkE, nBlkW);
        if(iBlk>1 && ix<L1Xmax-ireset-6){
          for(int iy=0; iy<=L12Ymax; iy++){
            xy_filter[ix][iy]=0;
            //cout << "L1Reject  ix=" << ix << "   iy=" << iy << endl;
          }
        }//if(iBlk>1)
      }
    }


    //Remove horizontal noise in L2A (vertical) region
    int ivert2 =0;
    for(int iy=0; iy<10; iy++){
      int kk=0;
      for(int ix=L2Xmin; ix<=L2Xmax; ix++){
        if(xy[ix][iy]==1){kk++;}
      }
      if(kk>7){
        for(int ix=L2Xmin; ix<=L2Xmax; ix++){xy_filter[ix][iy]=0;}
      }
    }

    //Remove horizontal noise in L2A (vertical) region
    for(int ix=L2Xmin; ix<L2Xmin+7; ix++){
      int kk=0;
      for(int iy=0; iy<=L12Ymax; iy++){
        if(xy[ix][iy]==1){kk++;}
      }
      if(kk<=2){
        ivert2++;
        for(int iy=0; iy<=L12Ymax; iy++){xy_filter[ix][iy]=0;}
      }
    }


    //Remove noise for L2 region
    //cout << "AAA 004  L2" << endl;
    ireset =0;
    for(int ix=L2Xmin+8+ivert2; ix<L2Xmax; ix++){
      int kk=0;
      for(int i=0; i<520; i++){xProj[i]=0; yProj[i]=0;}    
      for(int iy=0; iy<=L12Ymax; iy++){
        if(xy[ix][iy]==1){yProj[iy]=1; kk++;}
      }
      int idiff = ix-L2Xmin;
      if(kk<4 && idiff<8){
        for(int iy=0; iy<=L12Ymax; iy++){xy_filter[ix][iy]=0;}
        ireset++;
        kk=0;
      }
      if(kk>1){
        imin=0; imax=L12Ymax; iBlk=0; nCluster=0;
        Project(imin, imax, yProj, iBlk, nBlkS, nBlkE, nBlkW);
        if(iBlk>1 && ix>L2Xmin+ireset+6){
          for(int iy=0; iy<=L12Ymax; iy++){xy_filter[ix][iy]=0;}
        }
      }
    }


    //Remove noise for L3 region
    //cout << "AAA 005  L3" << endl;
    for(int ix=0; ix<frame_x; ix++){
      int kk=0;
      for(int i=0; i<520; i++){xProj[i]=0; yProj[i]=0;}    
      for(int iy=L3Ymin; iy<=L3Ymax; iy++){
        if(xy[ix][iy]==1){yProj[iy]=1; kk++;}
      }
      if(kk>1){
        imin=L3Ymin; imax=L3Ymax; iBlk=0; nCluster=0;
        Project(imin, imax, yProj, iBlk, nBlkS, nBlkE, nBlkW);
        if(iBlk>1){
          for(int iy=L3Ymin; iy<=L3Ymax; iy++){xy_filter[ix][iy]=0;}
        }
      }
    }



    //Extract Points for Line-1 and Line-2
    nL1pt=0, nL2pt=0, nL3pt=0;
    for(int iy=0; iy<=L12Ymax; iy++){
      for(int ix=0; ix<=L1Xmax; ix++){
        if(xy_filter[ix][iy]==1){xL1[nL1pt]=ix; yL1[nL1pt]=iy; nL1pt++;}
      }
      for(int ix=L2Xmin; ix<=L2Xmax; ix++){
        if(xy_filter[ix][iy]==1){
          xL2[nL2pt]=ix; yL2[nL2pt]=iy; nL2pt++;
          //cout << "xxL2:   ix2=" << ix << "    iy2=" << iy << "   nL2pt=" << nL2pt << endl;
        }
      }
    }

    //Extract Points for Line-3
    for(int iy=L3Ymin; iy<=L3Ymax; iy++){
      for(int ix=0; ix<520; ix++){
        if(xy_filter[ix][iy]==0)continue;
        xL3[nL3pt]=ix; yL3[nL3pt]=iy; nL3pt++;
        //cout << "xxL3:   ix3=" << ix << "    iy3=" << iy << "   nL3pt=" << nL3pt << endl;
      }
    }

    cout << "nL1pt=" << nL1pt << "  nL2pt=" << nL2pt << "  nL3pt=" << nL3pt << endl <<endl;

    //Extract and Fit Line1A, Line1B, Line2A, Line2B and Line3A, Line3B points
    c1->cd();
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
      xL1A[i]=0; yL1A[i]=0; xL1B[i]=0; yL1B[i]=0; err[i]=0.6;
      xL2A[i]=0; yL2A[i]=0; xL2B[i]=0; yL2B[i]=0;
      xL3A[i]=0; yL3A[i]=0; xL3B[i]=0; yL3B[i]=0;
    }

    //Fit Line 1A and 1B
    for(int i=0; i<nL1pt; i++){    //Separate points for 1A and 1B
      int ix=xL1[i], iy=yL1[i];
      histL1X[fidx]->Fill(ix);      histL1Y[fidx]->Fill(iy);
      int diffx = (L1Xmax-ivert1) - ix;
      if(abs(diffx) < 6){
        xL1A[npt1A]=ix;  yL1A[npt1A]=iy; npt1A++;
        //cout << "XXX1A  xL1_diffx=" <<  diffx << "  ix=" << ix;
        //cout << "  iy=" << iy <<  "   npt1A=" << npt1A << endl;
      }
    }

    int npt1AA=npt1A;
    nskip = npt1A;
    if(npt1A<21){
      for(int i=npt1A; i<nL1pt; i++){
        int ix=xL1[i], iy=yL1[i]; int diffx = xL1[npt1A]-ix;
        if(diffx < 7  && diffx>=0){
          xL1A[npt1AA]=ix;  yL1A[npt1AA]=iy; npt1AA++;
          //cout << "XXX1AA  xL1_diffx=" <<  diffx << "  ix=" << ix;
          //cout << "  iy=" << iy <<  "   npt1AA=" << npt1AA << endl;
        }
      }
      nskip = npt1AA;
      npt1A = npt1AA;
    }

    for(int i=nskip; i<nL1pt; i++){
      int ix=xL1[i], iy=yL1[i];    int diffx = xL1A[npt1A-1]-ix;
      if(diffx > 20){
        xL1B[npt1B]=ix;  yL1B[npt1B]=iy; npt1B++;
        //cout << "XXX1B  i=" << i << "   xL1_diffx=" <<  diffx << "  ix=" << ix;
        //cout << "  iy=" << iy <<  "   npt1B=" << npt1B << endl;
      }
    }


    gL1A = new TGraphErrors(npt1A, xL1A, yL1A, err, err);
    f_pol1A->SetParameters(5000, -40);	gL1A->Draw("a*");	gL1A->Fit("f_pol1A", "Q");
    TF1 *fL1A = gL1A->GetFunction("f_pol1A");
    float p0_L1A = fL1A->GetParameter(0);	float p0_L1A_err = fL1A->GetParError(0);
    double m_L1A = fL1A->GetParameter(1);	float m_L1A_err  = fL1A->GetParError(1);

    gL1B = new TGraphErrors(npt1B, xL1B, yL1B, err, err);
    f_pol1B->SetParameters(200, -1);	gL1B->Draw("a*");	gL1B->Fit("f_pol1B", "Q");
    TF1 *fL1B = gL1B->GetFunction("f_pol1B");
    float p0_L1B = fL1B->GetParameter(0);	float p0_L1B_err = fL1B->GetParError(0);
    double m_L1B = fL1B->GetParameter(1);	float m_L1B_err  = fL1B->GetParError(1);

    cout << "p0_L1A = "     << p0_L1A << "   p1_L1A = " << m_L1A;
    cout << "    p0_L1B = " << p0_L1B << "   p1_L1B = " << m_L1B;    
    cout << "    npt1A = "  << npt1A  << "   npt1B = "  << npt1B  << endl;



    //Fit Line 2A and 2B
    for(int i=0; i<nL2pt; i++){
      int ix=xL2[i], iy=yL2[i];    int diffx = ix-(L2Xmin+ivert2);
      histL2X[fidx]->Fill(ix);     histL2Y[fidx]->Fill(iy);
      if(abs(diffx) < 6){
        xL2A[npt2A]=ix;  yL2A[npt2A]=iy; npt2A++;
        //cout << "XXX2A  xL2_diffx=" <<  diffx << "  ix=" << ix;
        //cout << "  iy=" << iy <<  "   npt2A=" << npt2A << endl;
        //cout << "  L2Xmin=" << L2Xmin << "   ivert2=" << ivert2 << endl;
      }
    }

    int npt2AA = npt2A;
    nskip = npt2A;
    if(npt2A<21){
      for(int i=npt2A; i<nL2pt; i++){
        int ix=xL2[i], iy=yL2[i];      int diffx = ix-xL2[npt2A];
        if(diffx < 7 && diffx>=0){
          xL2A[npt2AA]=ix;  yL2A[npt2AA]=iy; npt2AA++;
          //cout << "XXX2AA  xL2_diffx=" <<  diffx << "  ix=" << ix;
          //cout << "  iy=" << iy <<  "   npt2AA=" << npt2AA << endl;
        }
      }
      nskip = npt2AA;
      npt2A = npt2AA;
    }

    for(int i=nskip; i<nL2pt; i++){
      int ix=xL2[i], iy=yL2[i];    int diffx = ix-xL2A[npt2A-1];
      if(diffx > 20){
        xL2B[npt2B]=ix;  yL2B[npt2B]=iy; npt2B++;
        //cout << "XXX2B  i=" << i << "   xL2_diffx=" <<  diffx << "  ix=" << ix;
        //cout << "  iy=" << iy <<  "   npt2B=" << npt2B << endl;
      }
    }

    gL2A = new TGraphErrors(npt2A, xL2A, yL2A, err, err);
    f_pol2A->SetParameters(-1000, 40);	gL2A->Draw("a*");	gL2A->Fit("f_pol2A", "Q"); 
    TF1 *fL2A = gL2A->GetFunction("f_pol2A");
    float p0_L2A = fL2A->GetParameter(0);	float p0_L2A_err = fL2A->GetParError(0);
    double m_L2A = fL2A->GetParameter(1);	float m_L2A_err  = fL2A->GetParError(1);

    float y00 = -0.6*L2Xmin;
    gL2B = new TGraphErrors(npt2B, xL2B, yL2B, err, err);
    //cout << xL2B[0] << "   " << yL2B[0] << "   " << npt2B << endl;
    f_pol2B->SetParameters(y00, 0.5);	gL2B->Draw("a*");	gL2B->Fit("f_pol2B", "Q");
    TF1 *fL2B = gL2B->GetFunction("f_pol2B");
    float p0_L2B = fL2B->GetParameter(0);	float p0_L2B_err = fL2B->GetParError(0);
    double m_L2B = fL2B->GetParameter(1);	float m_L2B_err  = fL2B->GetParError(1);

    cout << "p0_L2A = "     << p0_L2A << "   p1_L2A = " << m_L2A;
    cout << "    p0_L2B = " << p0_L2B << "   p1_L2B = " << m_L2B;
    cout << "    npt2A = "  << npt2A  << "    npt2B = " << npt2B << endl;



    //Fit Line 3A and 3B
    int xmax3A = 0.5*(L1Xmax+L2Xmin) - 10;
    int xmin3B = 0.5*(L1Xmax+L2Xmin) + 10;
    for(int i=0; i<nL3pt; i++){
      int ix=xL3[i], iy=yL3[i];
      if(ix>xmax3A || iy<5)continue;
      xL3A[npt3A]=ix;  yL3A[npt3A]=iy; npt3A++;
      //cout << i << "   npt3A=" << npt3A << "   ix=" << ix << "   iy=" << iy << endl;
    }

    for(int i=0; i<nL3pt; i++){
      int ix=xL3[i], iy=yL3[i];
      if(ix<xmin3B)continue;
      xL3B[npt3B]=ix;  yL3B[npt3B]=iy; npt3B++;
      //cout << i << "   npt3B=" << npt3B << "   ix=" << ix << "   iy=" << iy << endl;
    }


    gL3A = new TGraphErrors(npt3A, xL3A, yL3A, err, err);
    f_pol3A->SetParameters(500, -1);	gL3A->Draw("a*");	gL3A->Fit("f_pol3A", "Q"); 
    TF1 *fL3A = gL3A->GetFunction("f_pol3A");
    float p0_L3A = fL3A->GetParameter(0);	float p0_L3A_err = fL3A->GetParError(0);
    double m_L3A = fL3A->GetParameter(1);	float m_L3A_err  = fL3A->GetParError(1);

    gL3B = new TGraphErrors(npt3B, xL3B, yL3B, err, err);
    f_pol3B->SetParameters(600, 1);	    gL3B->Draw("a*");	gL3B->Fit("f_pol3B", "Q");
    TF1 *fL3B = gL3B->GetFunction("f_pol3B");
    float p0_L3B = fL3B->GetParameter(0);	float p0_L3B_err = fL3B->GetParError(0);
    double m_L3B = fL3B->GetParameter(1);	float m_L3B_err  = fL3B->GetParError(1);

    cout << "p0_L3A = "     << p0_L3A << "   p1_L3A = " << m_L3A;
    cout << "    p0_L3B = " << p0_L3B << "   p1_L3B = " << m_L3B;
    cout << "    npt3A = "  << npt3A  << "    npt3B = " << npt3B << endl << endl;


    //ax+by+c = 0   mx-y+c = 0  a=m b=-1 c=c
    //x = b1c2−b2c1/a1b2−a2b1;      y = a2c1−a1c2/a1b2−a2b1;
    //x = (-c2+c1)/(-a1+a2);        y = (a2c1−a1c2)/(-a1+a2);
    //x = (-c2+c1)/(a2-a1);         y = (a2c1−a1c2)/(a2-a1);

    //x = (-p0_L1B + p0_L1A)/(m_L1B  - m_L1B)
    //y = (m_L1B*p0_L1A - m_L1A*p0_L1B)/(m_L1B  - m_L1B)

    //TLine *line = new TLine(-3,ymax,3,ymax);
    //line->SetLineColor(kRed);   line->Draw();

    //Get the intersection points
    float int_xL1 = (-p0_L1B + p0_L1A)/(m_L1B-m_L1A);
    float int_yL1 = (m_L1B*p0_L1A-m_L1A*p0_L1B)/(m_L1B-m_L1A);
    float xxL1A = -p0_L1A/m_L1A; float yyL1A=0;
    float xxL1B = 0; float yyL1B=p0_L1B;
    //cout << "int_xL1=" << int_xL1 << "    int_yL1=" << int_yL1 << endl;

    float int_xL2 = (-p0_L2B + p0_L2A)/(m_L2B-m_L2A);
    float int_yL2 = (m_L2B*p0_L2A - m_L2A*p0_L2B)/(m_L2B-m_L2A);
    float xxL2A = -p0_L2A/m_L2A; float yyL2A=0;
    float xxL2B = 512; float yyL2B= m_L2B*xxL2B + p0_L2B;
    //cout << "int_xL2=" << int_xL2 << "    int_yL2=" << int_yL2 << endl;
    //cout << "XXX: xxL2B=" << xxL2B << "    yyL2B=" << yyL2B << endl;

    float int_xL3 = (-p0_L3B + p0_L3A)/(m_L3B-m_L3A);
    float int_yL3 = (m_L3B*p0_L3A-m_L3A*p0_L3B)/(m_L3B-m_L3A);
    float yyL3A=400; float xxL3A = (yyL3A-p0_L3A)/m_L3A;
    float yyL3B=400; float xxL3B = (yyL3B-p0_L3B)/m_L3B;
    //cout << "int_xL3=" << int_xL3 << "    int_yL3=" << int_yL3 << endl;

    float centroid_x   = 0.3333*(int_xL1  + int_xL2  + int_xL3); 
    float centroid_y   = 0.3333*(int_yL1  + int_yL2  + int_yL3); 
    float frm_center_x = 0.5*frame_x;
    float frm_center_y = 0.5*frame_y;

    cout << "CentroidX = " << centroid_x   << "  CentroidY = " << centroid_y;
    cout << "  FrameX = "  << frm_center_x << "  FrameY = "    << frm_center_y << endl;

    //Plot Results
    c1->Clear(); c1->cd();
    g1 = new TGraph(nrec, xx, yy);
    g1->GetXaxis()->SetTitle("Pixel #");  g1->GetYaxis()->SetTitle("Pixel #");
    g1->SetTitle(fo1_name);
    g1->DrawClone("A*");

    TLine *line1A = new TLine(xxL1A, yyL1A, int_xL1, int_yL1);
    line1A->SetLineColor(kRed); line1A->SetLineWidth(3); line1A->DrawClone("same");
    TLine *line1B = new TLine(xxL1B, yyL1B, int_xL1, int_yL1);
    line1B->SetLineColor(kRed); line1B->SetLineWidth(3); line1B->DrawClone("same");

    TLine *line2A = new TLine(xxL2A, yyL2A, int_xL2, int_yL2);
    line2A->SetLineColor(kRed); line2A->SetLineWidth(3); line2A->DrawClone("same");
    TLine *line2B = new TLine(xxL2B, yyL2B, int_xL2, int_yL2);
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

    TMarker centroid(centroid_x, centroid_y, 22);
    centroid.DrawClone("same");

    TMarker frm_center(frm_center_x, frm_center_y, 21);
    frm_center.DrawClone("same");

    c1->SaveAs(outF);
    cout << endl << endl << endl;

    fprintf(fptr, "L1:  %02d  %03d  %3d  %3d  %3d  %3d  %3d  %3d \n", 
            iHole, iFile, npt1A, npt1B,  npt2A, npt2B,  npt3A, npt3B);

    fprintf(fptr, "L2:  %02d  %03d  %7.1f %7.3f %7.1f %7.3f \n", 
            iHole, iFile, p0_L1A, m_L1A,  p0_L1B, m_L1B);

    fprintf(fptr, "L3:  %02d  %03d  %7.1f %7.3f %7.1f %7.3f \n", 
            iHole, iFile, p0_L2A, m_L2A,  p0_L2B, m_L2B);

    fprintf(fptr, "L4:  %02d  %03d  %7.1f %7.3f %7.1f %7.3f \n", 
            iHole, iFile, p0_L3A, m_L3A,  p0_L3B, m_L3B);

    fprintf(fptr, "L5:  %02d  %03d  %7.1f %7.1f %7.1f %7.1f \n \n", 
            iHole, iFile, frm_center_x, frm_center_y, centroid_x, centroid_y);

    //fL1A->SetMaximum(150);    fL1A->DrawClone("same"); 
    //fL1B->SetRange(0, 200);   fL1B->DrawClone("same");
    //fL2A->SetMaximum(150);    fL2A->DrawClone("same"); 
    //fL2B->SetRange(300, 520); fL2B->DrawClone("same");
    //fL3A->SetRange(0, 250);   fL3A->DrawClone("same"); 
    //fL3B->SetRange(200, 475); fL3B->DrawClone("same");
 
    //gL1B->Draw("AP"); //fL1A->Draw("same");

    if(histL1X[fidx]->GetEntries()>5)histL1X[fidx]->Write();
    if(histL2X[fidx]->GetEntries()>5)histL2X[fidx]->Write();
    if(histL3X[fidx]->GetEntries()>5)histL3X[fidx]->Write();

    if(histL1Y[fidx]->GetEntries()>5)histL1Y[fidx]->Write();
    if(histL2Y[fidx]->GetEntries()>5)histL2Y[fidx]->Write();
    if(histL3Y[fidx]->GetEntries()>5)histL3Y[fidx]->Write();
  //}//fidx

  fclose(fptr);
  //hfile->Write();
  hfile->Close();
   if(slopanderror != NULL){
	slopanderror[0]=  fL1A->GetParameter(1); 
        slopanderror[1]=  fL1A->GetParError(1);
    }
  return 1;
}

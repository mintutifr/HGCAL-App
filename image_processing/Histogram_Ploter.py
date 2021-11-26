import ROOT as rt
def Histogram_creator(file,leaf,bins,cut=""):
    infile = rt.TFile(file,"Read")
    tree = infile.Get("tree_name")
    rt.gROOT.cd()
    if(len(bins)==0):
        bins.append(400)
        bins.append(-400)
        bins.append(400)
    if(leaf=="(int_yL2-int_yL1)/(int_xL2-int_xL1)"): #slop L12
        bins[0] = 20
        bins[1] = -0.1
        bins[2] = 0.1
    if (leaf == "x_offset"):  # x_offset
        bins[0] = 60
        bins[1] = -15
        bins[2] = 15
    if (leaf == "y_offset"):  # y_offset
        bins[0] = 36
        bins[1] = -2
        bins[2] = 16
    if(leaf == "slop_L1B"):
        bins[0] = 20
        bins[1] = -1.0
        bins[2] = 0.0
    if(leaf == "slop_L2B"):
        bins[0] = 20
        bins[1] = 0.0
        bins[2] = 1.0


    h1 = rt.TH1F("h1","h1",bins[0],bins[1],bins[2])
    h1.SetYTitle("#image")
    h1.SetXTitle("slop")
    tree.Project("h1",leaf,cut)
    return h1
if __name__ == "__main__":
    bins = []
    #h = Histogram_creator("slopsAndOffset.root", "y_offset", bins,
    #                     "(int_yL2-int_yL1)/(int_xL2-int_xL1)<0.01 && (int_yL2-int_yL1)/(int_xL2-int_xL1)>-0.05 && slop_L1B<-0.6 && slop_L1B>-0.85 && slop_L2B>0.6 && slop_L2B<0.7") #ONE SIGMA
    h = Histogram_creator("slopsAndOffset_Pass3_Image_75_02092021_run1.root", "(int_yL2-int_yL1)/(int_xL2-int_xL1)", bins,"")
                          #"(int_yL2-int_yL1)/(int_xL2-int_xL1)<0.02 && (int_yL2-int_yL1)/(int_xL2-int_xL1)>-0.05 && slop_L1B<-0.6 && slop_L1B>-0.7 && slop_L2B>0.55 && slop_L2B<0.7")  # TWO SIGMA
    #if((slopanderror[21]-slopanderror[20])/(slopanderror[18]-slopanderror[17])<0.02 and (slopanderror[21]-slopanderror[20])/(slopanderror[18]-slopanderror[17])>-0.05 and slopanderror[2]<-0.6 and slopanderror[2]>-0.7 and slopanderror[6]>0.55 and slopanderror[6]<0.7):
    #h = Histogram_creator("slopsAndOffset_Pass3_Image_75_02092021_run1.root", "slop_L2B", bins,"")
    #h = Histogram_creator("slopsAndOffset_pass2.root", "(int_yL2-int_yL1)/(int_xL2-int_xL1)", bins,"")
    h.Draw()
    input()

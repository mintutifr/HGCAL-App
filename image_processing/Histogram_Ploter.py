import ROOT as rt
def Histogram_creator(file,leaf,bins):
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
    h1 = rt.TH1F("h1","h1",bins[0],bins[1],bins[2])
    h1.SetYTitle("#image")
    h1.SetXTitle("slop")
    tree.Project("h1",leaf)
    return h1
if __name__ == "__main__":
    bins = []
    h=Histogram_creator("slopsAndOffset.root","(int_yL2-int_yL1)/(int_xL2-int_xL1)",bins)
    h.Draw()
    input()

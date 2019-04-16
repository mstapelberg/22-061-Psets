#include <iostream>
#include "TF3.h"
#include "TRandom.h"
#include "TH3.h"

void P6P4(){
    //auto c26 = new TCanvas("c26", "c26",600,400);
    gStyle->SetOptStat(kFALSE);
    auto h3iso = new TH3F("h3iso", "Option ISO", 15, -2, 2, 15, -2, 2, 15, 0 , 4);
    Double_t Current, Mag_field, Temp;
    for (Int_t i=0; i<10000; i++){
        gRandom->Rannor(Temp, Mag_field);
        Current = Temp*Temp + Mag_field* Mag_field;
        h3iso->Fill(Temp, Mag_field, Current);
    }
    h3iso->SetFillColor(kBlue);
    h3iso->Draw("ISO");

    //Create a ROOT Tree
    
    //For Loop to read in data
    //for (Int_t i=0; i< Current->GetEntries(); i++){
        
    //}

}

/*
void importSpectrum(string filename, TH1D* h){
        //Take spectrum data from filename and use it to fill the histogram h
        TTree* tree = new TTree("tree", "tree");
        tree->ReadFile(filename.c_str(), "countsPerChannel");
        float counts;
        tree->SetBranchAddress("countsPerChannel", &counts);
        for(int i = 0; i < tree->GetEntries(); i++){
                tree->GetEntry(i);
                h->SetBinContent(i+1, (double) counts);
                h->SetBinError(i+1, sqrt((double) counts));
        }
}
*/


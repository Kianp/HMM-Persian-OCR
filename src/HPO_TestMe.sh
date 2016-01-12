if [ $# -ne 2 ]; then
  echo "Usage: testme.sh <text> <m-state>"
  exit 1
fi
pango-view --text "$1" --no-display --font="B Mitra" --dpi=700 --align left --output temp.png
pngtopnm temp.png > temp.pnm
rm temp.png
ppmtopgm temp.pnm > temp.pgm 
rm temp.pnm 
pgmtopbm temp.pgm > temp.pbm 
rm temp.pgm 

f=temp.pbm
dim=20
pnmdepth 255 temp.pbm |
pgmmedian |          
pgmslope|            
pgmslant -M M |       
pgmnormsize -c 5 |    
pgmtextfea -c 20  > _tmp.fea     
pfl2htk _tmp.fea temp.fea

rm temp.pbm _tmp.fea
HVite -A -T 1 -o ST -p -17 -s 50 -H hmm/hmm_$2/Macros_hmm -l "*" -i res_single.mlf -w Network Dictionary HMMsList temp.fea
echo "Result stored in res_single.mlf"
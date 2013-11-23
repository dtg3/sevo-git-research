## Software Evolution
### Drew, Evan, Heather


## Literature Review
- What's a Typical Commit? A Characterization of Open Source Software Repositories
- The Commit SIze Distribution of Open Source Software
- What Do Large Commits Tell Us? A Taxonomical study of large commits


### What's a Typical Commit? A Characterization of Open Source Software Repositories
#### IEEE International Conference on Program Comprehension - 2008


#### Authors
- Abdulkareem Alali
- Huzefa Kagdi
- Jonathan Maletic


### Size Metrics
- Used GNU diff
- Measured commit size with different levels of granularity
   - No. files modified
   - No. LOC (add + deleted + modified)
   - No. hunks with line changes
- Single hunk changes are local, even trivial
- Multiple hunks suggest rippling impact


### Characterizing Commits
Commits put into categories within quartiles ranging from Extra-Small to Extra-Large

![Figure 2](/pics/fig1.2.png)

Figure 2.  A box plot showing the Inter Quartile Range (IQR) regions used to categorize commits into five categories.


### Evaluation Set-up
<!-- Lists the 9 open source systems that were studied. -->
![Eval Set-up](/pics/evalsetup.png)


## Evaluation Results


### Typical Commit Size
<!--
  Point out that 75% of the commits are small or extra-small.
  However, larger commits do happen with "non-trivial frequency"
  The largest commits tend to touch every file (ie, license update)
-->
![Eval Results - Histogram](/pics/evalresults1.png)


### Commit Size Ranges
<!-- 
  Same as previous data but in a table format.
  Note how files/lines/hunks are ranged.
-->
![Eval Results - Table](/pics/gcc-commits.png)


### Correlation between Characteristics
- Calculated linear correlation coefficient for:
    - files x lines
    - files x hunks
    - lines x hunks
- Corresponded this with categries extra-small to extra-large

<!--
  When r is positive, it indicates that as x increases, y increases
  When r is negative, it indicates that as x increases, y decreases
  They calculated this in comparison to each level of granularity and by size.
-->
![Correlation Coefficient Equation](/pics/correlation-coefficient-equation.png)


## Correlation Results


### Correlation by System
<!--
  Histogram of the correlation coefficients between each two size
  metrics for each of the 9 projects.
  Notice that hunks x lines have the strongest correlation.
-->
![Correlation by System](/pics/correlation-by-system.png)


### Correlation by Size
<!--
  Histogram of the correlation coefficients between each two size
  metrics separated by size ranges extra-small to extra-large. This
  includes all 9 projects.
  There is little correlation among the three characteristics.
-->
![Correlation by Size](/pics/correlation-by-size.png)


### The Commit Size Distribution of Open Source Software
#### International Conference on System Sciences - 2009


### What Do Large Commits Tell Us? A Taxonomical study of large commits
#### (?? Conference ??) - 2008

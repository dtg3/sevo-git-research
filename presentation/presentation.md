# Gitting a Grep on Git Commits
## Drew, Evan, Heather


## What is Git?


 * Revision Control / Source Code Management tool
 * Follows the distributed model
 * Offers fast and frictionless branching / merging
 * Extremely good performance and speed
 * Cryptographically secure revision tracking
 * And of course.. Open Source


## Distributed Version Control?

Maybe we're gitting ahead of ourselves...


First let's recap what a 'centralized' revision control...


 * Most version control tools are "Centralized".
 * Client-Server approach to SCM
 * There is only one blessed repositories
 * All commits are immediately available in this repository
 * Must connect to the repository to make a commit
 * Single point of failure


![Centralized version
control](http://git-scm.com/figures/18333fig0102-tn.png)


Git uses a distributed repository model


 * No **one** central repository
 * Anyone with access can clone the entire history of a repository, allowing
   them to have a complete local copy
 * Repositories are self contained. No need to commit to a server or even have
   an internet connection
 * Commits may be shared between repositories
 * Allows for multiple work flows


<!--
  So here we simply say why the aforementioned stuff matters and 
  what we plan to do. If there is a problem to solve (which I don't
  believe there is....exploratory), we could rename to The Problem.
-->
## The Questions

 * Does the use of Git impact the overall approach to commit "size" with respect
   to various source code change metrics?
   * Line Based
   * Hunk Based
   * File Based
 * At what level of granularity can Git commits be viewed?


<!--
  Layout what we plan to do and briefly describe related works.
-->
## Our Approach

 * Acquire open source projects found on GitHub
 * Analyze commits for current and previous revisions of each project
 * Process each commit based on the code change metrics to determine the "size"
   of the commit
 * Attempt to determine the different levels at which source code changes can be
   examined (commit, push, pull, etc.)


<!--
  What have we done....seriously, what have we done?
-->
## Progress Thus Far...
  
  * Metric Collection
  * Tool Assistance
    - [libgit2](http://libgit2.github.com/) / [pygit2](http://www.pygit2.org/)
    - [Ohcount](https://github.com/blackducksw/ohcount)
    - [CLOC](http://cloc.sourceforge.net/)
    - [GitHub API](http://developer.github.com/v3/)


## Literature Review

 * What's a Typical Commit? A Characterization of Open Source Software
   Repositories
 * The Commit Size Distribution of Open Source Software
 * What Do Large Commits Tell Us? A Taxonomical study of large commits


### What's a Typical Commit? A Characterization of Open Source Software Repositories
#### IEEE International Conference on Program Comprehension - 2008


#### Authors

 * Abdulkareem Alali
 * Huzefa Kagdi
 * Jonathan Maletic


### Size Metrics

 * Used GNU diff
 * Measured commit size with different levels of granularity
   - No. files modified
   - No. LOC (add + deleted + modified)
   - No. hunks with line changes
 * Single hunk changes are local, even trivial
 * Multiple hunks suggest rippling impact


### Characterizing Commits
Commits put into categories within quartiles ranging from Extra-Small to Extra-Large

![Figure 2](/diagrams/fig1.2.svg)

Figure 2.  A box plot showing the Inter Quartile Range (IQR) regions used to categorize commits into five categories.


### Evaluation Set-up
<!-- Lists the 9 open source systems that were studied. -->
![Eval Set-up](/diagrams/evalsetup.svg)


## Evaluation Results


### Typical Commit Size
<!--
  Point out that 75% of the commits are small or extra-small.
  However, larger commits do happen with "non-trivial frequency"
  The largest commits tend to touch every file (ie, license update)
-->
![Eval Results - Histogram](/diagrams/evalresults1.svg)


### Commit Size Ranges
<!-- 
  Same as previous data but in a table format.
  Note how files/lines/hunks are ranged.
-->
![Eval Results - Table](/diagrams/gcc-commits.svg)


### Correlation between Characteristics

 * Calculated linear correlation coefficient for:
   - files x lines
   - files x hunks
   - lines x hunks
 * Corresponded this with categries extra-small to extra-large

<!--
  When r is positive, it indicates that as x increases, y increases
  When r is negative, it indicates that as x increases, y decreases
  They calculated this in comparison to each level of granularity and by size.
-->
$$r=\frac{n\Sigma xy - (\Sigma x)(\Sigma y)}{\sqrt{n(\Sigma x^2) - (\Sigma x)^2}\sqrt{n(\Sigma y^2) - (\Sigma y)^2}}$$


## Correlation Results


### Correlation by System
<!--
  Histogram of the correlation coefficients between each two size
  metrics for each of the 9 projects.
  No significant relationship between file and line size measures.
  Notice that hunks x lines have the strongest correlation.
-->
![Correlation by System](/diagrams/correlation-by-system.svg)


### Correlation by Size
<!--
  Histogram of the correlation coefficients between each two size
  metrics separated by size ranges extra-small to extra-large. This
  includes all 9 projects.
  There is little correlation among the three characteristics.
-->
![Correlation by Size](/diagrams/correlation-by-size.svg)


### Vocabulary vs. Commit Size

 * Frequency of words used in commit messages, separated by size of commit
 * Identified 2+ terms in a set
 * All sizes: {file, fix}, {fix, use}, {file, update}
 * Extra-large: {file, fix}
 * Extra-small: {file, fix}, {add, bug}, {fix, use}, {remov, test}


### Conclusion

 * Most commits are very small with respect to
   - files (2-4)
   - lines (less than 50)
   - hunks (less than 8)
 * No significant correlation between file and line measures
 * Substantial co-relationship between hunk and line measures


### The Commit Size Distribution of Open Source Software
#### International Conference on System Sciences - 2009


### Approach

 * Analyze size of commits in over 9,000 open source projects
 * Measure over 8 million commits in SLOC
   - single commits (1-100 SLOC)
   - aggregate commits (101-10,000 SLOC)
   - repository refactorings (10,000+ SLOC)


### Results
<!-- The smaller the size of a commit, the more likely it is. -->
![Commit Size](/diagrams/commit-size.svg)


### What Do Large Commits Tell Us? A Taxonomical study of large commits
#### (?? Conference ??) - 2008


### Approach

 * Analyze 9 open source projects
 * Manually classified large commits
 * Found frequency of types of commits


### Results
<!--
  Distribution of types of changes for all projects.
  Most common: Merge, documentation, feature addition, and add module
-->
![Commit Size](/diagrams/types-of-commits.png)

# Data Platform System Design Interview tasks

The interview was for [Junior Research Associate in HPC ](https://www.linkedin.com/jobs/view/3567392829) at [CMCC Foundation - Centro Euro Mediterraneo sui Cambiamenti Climatici](https://www.linkedin.com/company/cmccfoundation/?lipi=urn%3Ali%3Apage%3Ad_flagship3_job_details%3BMjrOE58uR2excFxG2BZ2bg%3D%3D) focused on the technical exercise pointed below:

- The candidate should define a software architecture describing the functional modules for a full management of data collected from IoT sensors and satellite, from acquisition to visualisation. For each functional module, define some possible technological solutions.

- Develop a python script that takes as input a set of timeseries (Sensors.csv) of temperatures and extracts:

  a.  the maximum and minimum temperature detected, at which time and at which coordinates.
  
  b.  the list of values included in the bounding box identified by the vertices (lat, lon): (38, 16) - (40, 18) and the average temperature for each time step.
  
  c.  the list of values detected by the sensors whose average temperature exceeds 20C storing the result in a Results.csv file.

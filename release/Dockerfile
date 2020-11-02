FROM ousefuldemos/tm129-robotics2020:latest

# Create entry token
ARG TM129_VCE_TOKEN=letmein
ENV JUPYTER_TOKEN $TM129_VCE_TOKEN


# Tidying
#RUN mv content/README_FIRST.ipynb ./README_FIRST.ipynb
#RUN rm README.md && rm -rf content/00* && rm -rf outreach && rm -rf production && rm -rf release

# Setup search 
RUN rm -f $HOME/.nbsearch/notebooks.sqlite && nbsearch index -p ./content



#The ousefuldemos/tm129-robotics2020:latest is built from the repo
# https://github.com/innovationOUtside/tm129-robotics2020/
# by a Github Action watching releases
 
#Then run:

# docker pull ousefuldemos/tm129-robotics2020:latest
# docker build --tag ousefulcoursecontainers/ou-tm129:current .
# docker push ousefulcoursecontainers/ou-tm129:current

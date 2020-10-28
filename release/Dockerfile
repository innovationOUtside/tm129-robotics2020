FROM ousefuldemos/tm129-robotics2020:latest

# Create entry token
ARG TM129_VCE_TOKEN=letmein
ENV JUPYTER_TOKEN $TM129_VCE_TOKEN


# Remove tutor notes
rm -rf content/00*

# Setup search 
RUN rm -f $HOME/.nbsearch/notebooks.sqlite
RUN nbsearch index -p $HOME/content/notebooks



#The ousefuldemos/tm129-robotics2020:latest is built from the repo
# https://github.com/innovationOUtside/tm129-robotics2020/
# by a Github Action watching releases
 
#Then run:

# docker pull ousefuldemos/tm129-robotics2020:latest
# docker build --tag ousefulcoursecontainers/ou-tm129:current .
# docker push ousefulcoursecontainers/ou-tm129:current

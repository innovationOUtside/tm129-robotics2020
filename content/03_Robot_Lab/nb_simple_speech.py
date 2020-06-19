from IPython.display import Javascript


class Speech():
    def __init__(self, voice=None, reset=True):
        if reset:
            self.count = 1
        self.voice = voice
        self._get_voices()
        self.voicelist = ''

    def set_voice(self, voicenum):
        """Set voice number."""
        self.voice = voicenum

    def say(self, txt, showtext = True):
        """Speak an utterance."""
        js = f'''
        var utterance = new SpeechSynthesisUtterance("{txt}");
        '''
        if self.voice:
            js = js + f'''
            utterance.voice = window.speechSynthesis.getVoices()[{self.voice}];
            '''
        js = js + 'speechSynthesis.speak(utterance);'
        display(Javascript(js))
        
        if showtext:
            print(f'{self.count}: {txt}')
        self.count = self.count +1
        
    def reset_count(self):
        """Reset the counter."""
        self.count = 1
        
    def _get_voices(self):
        """Show a list of supported voices."""
        # via https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices
        js = '''
        var voices =  window.speechSynthesis.getVoices();
    var voicelist = '';
   for(var i = 0; i < voices.length; i++) {
   voicelist = voicelist+i+': '+ voices[i].name + ' ('+ voices[i].lang +')';
    if(voices[i].default) {
      voicelist += ' -- DEFAULT';
    }
   voicelist = voicelist + '\\n'
  }

IPython.notebook.kernel.execute('browser_voicelist = """'+ voicelist+'"""');
        '''
        display(Javascript(js))
        
    # browser_voicelist not seen; why not? I can see it in notebook?
    #def _set_voices(self):
    #    self.voicelist = browser_voicelist
        
    def show_voices(self):
        """Display voice list."""
        if not self.voicelist:
            self._set_voices() 
        outlist = '\n'.join([s.strip() for s in self.voicelist.split('*')])
        print(outlist)
        #return self.voicelist


# speaker = Speech()

# speaker.set_voice(49)
# speaker.say('hello how are you')

# speaker.show_voices()


# speaker.reset_count()
# speaker.say('hello again')

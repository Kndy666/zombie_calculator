import json
from pathlib import Path

class Config:
    def __init__(self, path = Path.cwd() / "config.json"):
        self.file = Path(path)

        self.defaultConfig = {}
        self.defaultConfig["logInterval"] = 0.2
        self.defaultConfig["defaultDensity"] = "-1"
        self.defaultConfig["defaultTheme"] = "dark_lightgreen.xml"
        self.defaultConfig["extra"] = {'density_scale': self.defaultConfig["defaultDensity"], 'QMenu':{'height': 5, 'padding': '5px 5px 5px 5px'}}
        self.defaultConfig["alertColor"] = {"warning" : "#FFFF00", "ok" : "#00FF00", "error" : "#FF0000"}
    def readConfig(self):
        self.file.touch(exist_ok = True)
        try:
            self.config  = json.loads(self.file.read_text())
        except:
            self.config = None
        return self.config     
    def updateConfig(self, config=None):
        self.file.touch(exist_ok = True)
        if config is None:
            self.config = self.defaultConfig
        self.file.write_text(json.dumps(self.config, sort_keys=True, indent=4))
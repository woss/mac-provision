# Bunch of useful tools we need in all environments
{% for pkg in pillar["brew"] %}
{{ pkg }}:
    cmd.run:
      -name: brew install {{pkg}}
    runas: danijel
{% endfor %}

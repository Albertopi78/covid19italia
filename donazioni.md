---
layout: page
title: Donazioni
permalink: /donazioni/
---
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Donazioni beni/strumenti'"%}
{% for member in filteredissues %}
<div class="panel-body">
<a href="/issues/{{ member.number | datapage_url: '.' }}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
	<p class="list-group-item-text">{{member.issue.data.data}}</p>
</a>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

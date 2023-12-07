#!/usr/bin/perl

use v5.012;

my $page = <<EOH;

<!DOCTYPE HTML>
<html lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta charset="UTF-8">
	<title>W5HGT Amateur Radio Club</title>
	<link rel="stylesheet" href="../css/main.css">

</head>

<body>
	<nav>
		<a href="https://orgs.latech.edu/amateurradio/index.html"> W5HGT </a>
		<a class="right" href = "https://orgs.latech.edu/amateurradio/officers.html"> People </a>
		<a class="right" href = "https://orgs.latech.edu/amateurradio/QSLcards/cards.html"> QSL<span style="width:5px;display:inline-block"></span>Cards </a>
		<a class="right" href = "https://orgs.latech.edu/amateurradio/history.hmtl"> History </a>
		<a class="right" href = "https://orgs.latech.edu/amateurradio/station.html"> Station </a>
	</nav>
	<nav>
		<a href="https://orgs.latech.edu/amateurradio/index.html"> W5HGT </a>
		<a class="right" href = "https://orgs.latech.edu/amateurradio/officers.html"> People </a>
	</nav>
	<div style="
	text-align: justify;
	width: 75%;
	background-color: #FFFFFF;
	border: 1px #777 solid;
	position: relative;
	margin: 0 auto;
	clear: both;
	overflow: hidden;
	padding: 0 0 10px 0;
">
		<div>
			<article>
				<div>
				${\list_cards()}
				</div>
			</article>
		</div>
	</div>
</body>
</html>

EOH

sub list_cards {
	my $result = "";
	for my $f (glob("orig/*.jpg")) {
		my $orig = $f;
		my $small = $f;
		$small =~ s{^orig/}{200px/200px_};
		if(not -e $small) {
			$result .= "<!-- $small not found -->\n";
		} else {
			$result .= qq{<a href="$orig"><img src="$small"/><a/>\n};
		}
	}
	return $result;
}

print "Content-type: text/html\r\n\r\n$page";

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>R1</p>
        </td>
        <td>
            <p>Unbefugte ohne Benutzer in der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer
                Benutzer sehen.</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch </p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Beschreibung</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				Unbefugte ohne Benutzeraccount in der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer sehen.<br/>
				Betrifft: A8, A9
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Alle Zugriffe auf die Anwendung m&uuml;ssen authentifiziert erfolgen. (vgl. F13, F14, F25)<br/>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br/>
				- BSI CON.10.A1<br/>
				- OWASP V1.2.3
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Benutzerverwaltung und Authentifizierung (Anmeldung) erzwingen vor Zugriff.</p>
        </td>
        <td>
            <p>Manueller Test<br/> Automatisierter Test<br/>Pentest<br>Code Review (Manuell)</p>
        </td>
        <td>
            <p>T1<br/>T2<br/>T3<br/>T5</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R2</p>
        </td>
        <td>
            <p>
				Benutzer der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer sehen.
			</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch<br/></p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				Benutzer der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer sehen.<br/>
				Betrifft: A8, A9
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Vor jedem Zugriff wird die Berechtigung des Benutzers durch den Dateiverwaltungsdienst ??berpr??ft und der Zugriff gegebenenfalls abgelehnt (vgl. NF2).<br/>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br/>
				- CON.10.A2
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Authentifizierung (Anmeldung) erzwingen vor Zugriff (siehe R1).<br/>
				Autorisierung (Berechtigunbgspr&uuml;fung) erzwingen vor Zugriff.
			</p>
        </td>
        <td>
            <p>Manueller Test<br/> Automatisierter Test<br/>Pentest<br/>Code Review (manuell)</p>
        </td>
        <td>
            <p>T6<br/>T7<br/>T8<br/>T10</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R3</p>
        </td>
        <td>
            <p>Sicherheit der Daten&uuml;bertragung</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Daten??bertragungen zwischen Webbrowser und Webserver beziehungsweise zwischen Webserver und Dateiverwaltungsdienst beziehungsweise zwischen Dateiverwaltungsdienst und Dateiverwaltungsdatenbankserver k??nnen durch Dritte mitgelesen werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Alle Kommunikation/Daten??bertragung muss sicher (vertraulich und integrit??tsgesch??tzt) erfolgen (vgl. NF2, NF7, NF19, NF20).<br/>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br/>
				- CON.10.A14<br/>
                Betrifft: A8, A9, A10, A13, A18
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				F??r Verbindungen zwischen Webanwendung und Webserver, Webserver und Dateiverwaltungsdienst sowie Dateiverwaltungsdienst und Dateiverwaltungsdatenbank TLS einsetzen.<br>
				Der Webserver setzt den HTTP-Header Strict-Transport-Security (OWASP ASVS V14.4.5)
			</p>
        </td>
        <td>
            <p>Manueller Test<br/>Automatisierter Test<br/>Pentest<br/>Code Review (SAST)</p>
        </td>
        <td>
            <p>T11<br/>T12<br/>T13<br/>T14</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R4</p>
        </td>
        <td>
            <p>Datenmanipulation</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Durch Abfragemanipulation k??nnen unbefugt Daten (A8, A9) aus der Datenbank gelesen oder ver??ndert werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Ein unbefugter Datenbankzugriff, ob lesend oder schreibend, muss verhindert werden (vgl. NF2, F26).<br/>
				- Der Dateiverwaltungsdienst muss resistent gegen SQL-Injection-Angriffe sein (vgl. BSI CON.10.A9, NF10).<br/>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.
            </p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Daten??bertragung sch??tzen (vgl. R3)<br>
				Eingabevalidierung in der Webanwendung<br>
				Eingabevalidierung im Dateiverwaltungsdienst<br>
				Verwendung von Prepared SQL Statements durch den Dateiverwaltungsdienst<br>
				Kryptografische Verschl??sselung mit Integrit??tsschutz anbringen (vgl. R11)
            </p>
        </td>
        <td>
            <p>Manueller Test<br>Code Review (SAST)</p>
        </td>
        <td>
            <p>T15<br/>T16</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R5</p>
        </td>
        <td>
            <p>Webanwendungs-Schwachstellen</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Es verbleiben typische Webschwachstellen in der Anwendung die nicht entdeckt werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Die Webanwendung ist resistent gegen XSS<br>
				- Die Webanwendung, Webserver und Dateiverwaltungsdienst sind resistent gegen Session Hijacking<br>
				- Der Webserver, Dateiverwaltungsdienst und Authentifizierungsdienst sind resistent gegen Session Prediction<br>
				- Der Webserver ist resistent gegen Path Traversal<br>
				- Der Webserver, Dateiverwaltungsdienst und Authentifizierungsdienst sind resistent gegen CSRF
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Der Webserver und der Dateiverwaltungsdienst reflektieren keine Benutzereingaben als HTML/CSS/JS<br>
				Der Webserver setzt den HTTP-Header Content-Security-Policy (OWASP ASVS V14.4.3)<br>
				Der Webserver setzt den HTTP-Header X-Content-Type-Options (OWASP ASVS V14.4.4)<br>
				Die Webanwendung verwendet keine Benutzereingaben zur DOM-Modifikation<br>
				Die Webanwendung zeigt Sitzungsgeheimnisse nicht in der URL an<br>
				Der Webserver pr??ft auf auff??llige ??nderungen des UserAgent Headers im Laufe einer Sitzung.<br>
				Der Webserver stellt sicher, dass Sitzungen nicht unbegrenzt g??ltig.<br>
				Alle Sitzungsgeheimnisse werden zuf??llig durch einen CSRNG gezogen.<br>
				Der Webserver pr??ft nachdem eine angefragte Ressource im Dateisystem gefunden wurde, ob die Datei im freigegebenen Bereich liegt.<br>
			</p>
        </td>
        <td>
            <p>Manueller Test<br/>Automatisierter Test<br/>Code Review (SAST)</p>
        </td>
        <td>
            <p>T17<br/>T18<br/>T19</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahr-<br>scheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R6</p>
        </td>
        <td>
            <p>Benutzer verwenden unsichere Passw??rter</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Benutzer w??hlen aus Bequemlichkeit, Unwissenheit oder anderen Gr??nden unsichere Passw??rter f??r die Authentifizierung.
                <br>Dadurch werden Sicherheitsmechanismen, die auf der Integrit??t des Benutzerkontos aufbauen, unwirksam.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Das Erraten des Kennworts mittels Bruteforce oder durch Nutzung von W??rterb??chern und Rainbowtables soll unwirtschaftlich sein (vgl. NF24)</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Single-Sign-On ??ber einen externen IDP erm??glichen. (optional)<br>
				Das Passwort muss gewisse Vorgaben erf??llen um verwendet werden zu k??nnen.<br>
				Zum Speichern und Pr??fen von Passw??rtern wird eine geeignete Hashfunktion und ein Salz verwendet.
			</p>
        </td>
        <td>
            <p>
                Automatisierter Test<br/> 
                Pentest<br/>
                Code Review<br/>
                Design Review
            </p>
        </td>
        <td>
            <p>T20<br>T21<br>T22<br>T23</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahr-<br>scheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R7</p>
        </td>
        <td>
            <p>Benutzer vergessen Passw??rter</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				Wegen hoher Anforderungen (siehe R6) an das Passwort ist dieses nicht sehr einpr??gsam. Hinzu kommt, dass die Gesundheitsakte von den meisten Benutzern nicht regelm????ig verwendet wird.<br>
				Infolgedessen werden viele Benutzer ihr Zugangsdaten vergessen und somit ihre verschl??sselten Daten verlieren (vgl. Konzept "Sch??tzen von Data-at-rest").
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Benutzer werden auf dieses Risiko aufmerksam gemacht und M??glichkeiten zur Vermeidung genannt (vgl. F28, F29)</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Bei der Erstellung des Kontos wird darauf hingewiesen, dass es sich bei der Anwendung nicht um einen Onlinespeicher, sondern um eine Datenaustauschplattform handelt. Das hat zur Folge, dass die Verf??gbarkeit der Daten der Vertraulichkeit und der Integrit??t der Daten untergeordnet ist.<br>
				Bei der Erstellung des Kontos wird darauf hingewiesen, dass in der Anwendung zum Schutz der Vertraulichkeit die Daten Ende-zu-Ende verschl??sselt werden. Das hat zur Folge, dass beim Zur??cksetzen des Anmeldekennworts s??mtliche gespeicherte Daten gel??scht werden.<br>
				Bei der Erstellung des Kontos wird darauf hingewiesen, dass zum Verwalten von komplexen Passw??rtern ein Passwortmanager eine gro??e Hilfe ist.<br>
				Bei der Initialisierung kryptografischer Parameter wird dem Benutzer angeboten, eine Wiederherstellungsdatei abzuspeichern, die es erm??glicht, nach einem Zur??cksetzen des Kennworts weiterhin auf verschl??sselte Daten zuzugreifen (vgl. Konzept "Sch??tzen von Data-at-rest").
			</p>
        </td>
        <td>
            Manueller Test<br/> 
            Code Review
        </td>
        <td>
            <p>T24<br>T25</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahr-<br>scheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R8</p>
        </td>
        <td>
            <p>??berlastung der Speicherressourcen durch zu viele Dokumente.</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				Benutzer belegen ??berm????ig viele Speicherressourcen, indem sie Dateien in ihr Profil laden und verhindern so, dass anderen Benutzern dieser Speicherplatz zur Verf??gung steht.
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Das System ist resistent gegen einen DoS durch zu hohe Speicherbelegung durch einzelne Benutzer (vgl. F27, NF18)
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Pro Benutzer wird der verwendbare Speicherplatz beschr??nkt.<br>
				Pro Benutzer wird eine Netzwerkquota gesetzt.<br>
				BSI CON.10.A17
			</p>
        </td>
        <td>
            <p>Manueller Test</p>
        </td>
        <td>
            <p>T26</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R9</p>
        </td>
        <td>
            <p>Benutzer der Anwendung laden b&ouml;sartige Dateien hoch.</p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Benutzer der Anwendung laden b&ouml;sartige Dateien hoch.<br>
            Diese k&ouml;nnten dann von anderen Benutzern heruntergeladen und ge&ouml;ffnet werden und dadurch ihr System infizieren.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Das Hochladen einer solchen Datei soll erschwert und wenn m&ouml;glich verhindert werden. <br>
            Benutzer sollten vor dem Ausf??hren / beim Herunterladen einer Datei vor Risiken gewarnt werden (vgl. F30).</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
                Benutzer werden beim Herunterladen vor m??glichen Risiken gewarnt<br>
				Nur Dateien mit freigegebenen Dateiendungen d??rfen hochgeladen werden. Diese Ma??nahme ist jedoch nur bedingt wirksam, weil Dateiendungen nicht auf allen Plattformen ma??geblich daf??r sind, wie eine Datei interpretiert wird. Daher wird diese Ma??nahme nicht umgesetzt und stattdessen eine Warnung an den Benutzer ausgegeben.
            </p>
        </td>
        <td>
            <p>Manueller Test<p>
        </td>
        <td>
            <p>T27</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R10</p>
        </td>
        <td>
            <p>Unbefugte sehen geheime Konfigurationsparameter ein</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren/Akzeptieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Unbefugte Prozesse oder Benutzer k??nnen geheime Konfigurationsparameter einsehen, insbesondere kryptografische Schl??ssel, die von einer Anwendungskomponente ben??tigt werden, zum Beispiel zum Erbringen eines Identit??tsnachweises.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Geheime Konfigurationsparameter werden vertraulich gespeichert (vgl. NF21)<br>
				- OWASP ASVS V1.6.2 wird explizit nicht eingesetzt (vgl. Konzept "Sch??tzen von konfigurierten Geheimnissen produktiver Systeme")<br>
				Betrifft: A4, A6
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Ausgeben einer Warnung an den Administrator, falls f??r geheime Konfigurationsparameter im Dateisystem ung??nstige Zugriffsrechte gesetzt sind. Diese Ma??nahme ist sehr einfach umsetzbar, erm??glicht aber nur die Erkennung eines einzelnen, speziellen Szenarios und reduziert damit formell das bezeichnete Risiko. Weil dies aber die einzige Ma??nahme ist, w??re es irref??hrend, die Risikobehandlung als kommentarlos als Reduzieren zu bezeichnen, weil das nur unerheblich unter dem Ursprungsrisiko liegende Restrisiko de facto akzeptiert wird.</p>
        </td>
        <td>
            <p>Manueller Test</p>
        </td>
        <td>
            <p>T28</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R11</p>
        </td>
        <td>
            <p>Privilegierte Benutzer sehen Gesundheitsdaten anderer Benutzer ein</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Privilegierte Benutzer k??nnen Gesundheitsdaten anderer Benutzer einsehen. Dieses Risiko unterscheidet sich von R1 dahingehend, dass der Benutzer, der unbefugt Daten einsehen kann, berechtigterweise erweiterte Rechte auf Systemen der Anwendung hat.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Ma??nahmen, die die M??glichkeiten privilegierter Benutzer beschr??nken, Vertraulichkeit und Integrit??t gespeicherter Gesundheitsdaten zu verletzen, und deren Aufwand ihren Nutzen nicht unangemessen ??bersteigt, werden implementiert (vgl. NF22).<br>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br>
				Betrifft: A8<br>
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				Einsatz von Ende-zu-Ende-Verschl??sselung f??r Benutzerdaten mittels asymmetrischer Kryptografie (vgl. Konzept "Sch??tzen von Data-at-rest")<br>
				Ma??nahmen gem???? R1
            </p>
        </td>
        <td>
            <p>Manueller Test<br>Design Review<br>Code Review</p>
        </td>
        <td>
            <p>T29<br>T30<br>T31</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R12</p>
        </td>
        <td>
            <p>Privilegierte Benutzer sehen personenbezogene Daten anderer Benutzer ein</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Akzeptieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				Privilegierte Benutzer k??nnen personenbezogenen Daten anderer Benutzer einsehen. Dieses Risiko unterscheidet sich von R1 dahingehend, dass der Benutzer, der unbefugt Daten einsehen kann, berechtigterweise erweiterte Rechte auf Systemen der Anwendung hat.<br>
				F??r privilegierte Benutzer, die aus gesch??ftlichen Gr??nden auf die oder eine Teilmenge der gespeicherten personenbezogenen Daten zugreifen m??ssen, besteht die M??glichkeit, dass dieser Zugang missbraucht wird. Aufgrund der Datenminimierung nach DSGVO ist die Menge der vorhandenen und damit zugreifbaren Daten bereits minimal. Das Ergreifen weiterer technischer Ma??nahmen gegen einen Missbrauch des Zugangs w??re risikobasiert nicht angemessen. Stattdessen sollten f??r den Betrieb der Anwendung gegebenenfalls geeignete organisatorische Ma??nahmen implementiert werden, die dieses Risiko auf ein akzeptables Ma?? reduzieren (NDO).
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br>
				Betrifft: A9
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>???Principle of least privilege??? wird angewendet: Durch die Aufteilung der Anwendung in einzelne Dienste wird der Kreis der privilegierten Benutzer auf die Administratoren des Authentifizierungsdienstes reduziert.</p>
        </td>
        <td>
            <p>n/a</p>
        </td>
        <td>
            <p>n/a</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R13</p>
        </td>
        <td>
            <p>Eine Person, gibt vor, eine andere Person zu sein.</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Eine Person gibt sich als Arzt oder anderer Benutzer aus, um sich so das Vertrauen von anderen Benutzern erschleichen und sie zum Austausch der Patientendaten animieren.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Benutzer sollen ihr Gegen??ber zu jeder Zeit eindeutig identifizieren k??nnen (vgl. F31).
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
			    Jedem Benutzer wird bei der Erstellung seines Kontos eine eindeutige ID zugewiesen. Der Empf??nger gibt sie an Personen weiter, von denen er Dokumente erhalten m??chte.
				Der Sender kann mit dieser Nummer sein Gegen??ber eindeutig identifizieren: Vor der ersten Dateifreigabe gibt der Sender die Identifikationsnummer an, um das Benutzerprofil
				des Empf??ngers zu finden. Nachdem eine g??ltige Identifikationsnummer angegeben wurde, werden allgemeine Profilinformationen zur eingegebenen Nummer angezeigt und erneut
				durch den Benutzer best??tigt. Erst danach steht dieser Empf??nger f??r Freigaben im Profil des Senders zur Verf??gung. Weil die Identifikationsnummern in nicht vorhersagbarer
				Folge zugewiesen werden, ist deren Absch??tzung erheblich erschwert und es ist unwahrscheinlich, dass ein Fehler des Senders bei der Eingabe der Nummer eine Nummer erzeugt,
				die einem anderen Profil zugeordnet ist.
			</p>
        </td>
        <td>
            <p>
                Manueller Test<br>
                Design Review
            </p>
        </td>
        <td>
            <p>T32<br>T33</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R14</p>
        </td>
        <td>
            <p>Die Webanwendung wird zum Abgreifen sensibler Daten manipuliert</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Eine schadhafte Ver??nderung der Webanwendung f??hrt zu einer Offenlegung von sensiblen Daten, beispielsweise von Gesundheitsdaten oder Passw??rtern.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Die Integrit??t der Webanwendung, also von HTML-, CSS-, JavaScript- und anderen Ressourcen, muss sichergestellt werden (vgl. NF23)
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				- Verwendung von TLS f??r die ??bertragung der Webanwendung (vgl. R3)<br>
				- Verwendung eines TLS-Serverzertifikats, das es Benutzern erlaubt, die Identit??t des Servers vor der Verwendung der Webanwendung zu ??berpr??fen. Dabei ist zu ber??cksichtigen,
				dass dadurch nur ein Schutz erzielt wird, solange die gef??lschte Webanwendung unter dem echten Hostnamen abgerufen wird und solange der F??lscher keinen Zugriff auf die private
				Komponente des verwendeten Zertifikats hat.
			</p>
        </td>
        <td>
            <p>
                Manueller Test
            </p>
        </td>
        <td>
            <p>T33</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

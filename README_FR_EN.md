# BYTE NDT — TWIN FORMATION ALPHA REV0 8512

## FR — Utilisation
1. Ouvrir `operator_view.html` dans Chrome, ou lancer `streamlit run app.py` après `pip install -r requirements.txt`.
2. Les quatre vues (opérateur, coupe Y–Z, A-scan, champ acoustique) sont regroupées sur une page.
3. Glisser le MWB pour balayer; tourner avec la molette ou les boutons ±5°. Utiliser **Autre côté du cordon** pour passer sur la rive opposée.
4. Choisir MWB 45°, 60° ou 70° et régler le gain d'affichage A-scan (non étalonné).
5. En mode élève, les défauts restent cachés. Le mode instructeur révèle les trois indications.
6. Enregistrer des points dans les portes A/B/C pour examiner les mesures et l'étendue indicative à −6 dB.

**Limites :** rayons et réflexions géométriques illustratifs, réponses d'indications heuristiques. Les amplitudes, la diffraction et les estimations XYZ ne sont pas validées sur mesures réelles. Ce n'est pas CIVA ni un solveur Born/Kirchhoff/GTD/Green validé. Ne pas utiliser pour une décision de conformité industrielle.

## EN — Instructions
1. Open `operator_view.html` in Chrome, or run `streamlit run app.py` after `pip install -r requirements.txt`.
2. Four views (operator, Y–Z section, A-scan, acoustic field) share one dashboard.
3. Drag the MWB to scan; rotate with mouse wheel or ±5° controls. Use **Opposite weld side** to switch sides.
4. Select 45°, 60° or 70° MWB; adjust the uncalibrated A-scan display gain.
5. Student mode hides flaws; instructor mode reveals the three indications.
6. Record A/B/C gate samples for provisional XYZ and −6 dB extent readings.

**Limitations:** illustrative geometric rays/reflections and heuristic flaw amplitudes. Diffraction, XYZ estimates and amplitude response have not been validated with measured data. Not a validated CIVA or Born/Kirchhoff/GTD/Green solver. Not for industrial acceptance decisions.

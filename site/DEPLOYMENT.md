# GitHub Pages migration runbook — 2026-09-18

## Scope

Move only the website for `rootsequence.systems` from Fastmail to GitHub Pages.
Fastmail continues to provide the domain's DNS and email. Do not change the
nameservers, MX records, SPF/DKIM/DMARC records, mail-related CNAMEs, or any
other mail configuration.

## Verified starting point

- The public site responds over HTTPS from Fastmail.
- Apex and `www` web traffic use Fastmail addresses `103.168.172.52` and
  `103.168.172.37`.
- Nameservers are `ns1.messagingengine.com` and `ns2.messagingengine.com`.
- Mail uses `us1-smtp.messagingengine.com` and `us2-smtp.messagingengine.com`.
- GitHub Pages was not enabled for `Root-Sequence/root-sequence` when this
  runbook was written.
- A byte-for-byte copy of the current Fastmail homepage and response headers
  was saved outside the repository before migration work began.

## Staged migration

1. Run `python site/test_site.py` and build a release into a new empty folder.
2. Enable GitHub Pages with GitHub Actions as the publishing source.
3. Run the Pages workflow and verify the GitHub-provided Pages origin before
   changing public DNS.
4. Set the repository's custom domain to `rootsequence.systems`.
5. In Fastmail DNS, replace only the two apex web A records with GitHub Pages:

   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

6. Replace only the two `www` web A records with one CNAME to
   `root-sequence.github.io`.
7. Leave all mail and nameserver records untouched.
8. Verify the apex and `www` results from more than one public resolver, then
   verify the deployed page, navigation, overlays, external links, HTTPS, and
   response headers at the public domain.
9. Enable "Enforce HTTPS" after GitHub has issued the certificate.
10. Keep the Fastmail rollback copy for at least 48 hours after the verified
    cutover.

DNS propagation and certificate issuance are asynchronous. A partially updated
resolver is not proof of failure or success.

## Rollback

If the GitHub origin or certificate is not healthy, restore only the former web
records:

- apex A: `103.168.172.52`, `103.168.172.37`
- `www` A: `103.168.172.52`, `103.168.172.37`

Do not alter mail records during rollback. Confirm that the preserved Fastmail
page is serving again before closing the incident.

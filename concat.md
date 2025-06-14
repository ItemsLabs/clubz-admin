# Repository Structure

- **.github/**
  - **workflows/**
    - dev.yml
    - prd.yml
- **blockchain_web3/**
  - GAME.json
  - __init__.py
  - playersabi.json
  - services.py
  - sync.py
  - tasks.py
  - utils.py
- **core/**
  - **migrations/**
    - 0001_initial.py
    - 0002_auto_20190311_2023.py
    - 0003_auto_20190312_2155.py
    - 0004_auto_20190313_1046.py
    - 0005_optafeed_match.py
    - 0006_gameevent.py
    - 0007_auto_20190314_1821.py
    - 0008_teamplayer_is_star.py
    - 0009_auto_20190320_1905.py
    - 0010_actions_powerup_seed.py
    - 0011_auto_20190320_1948.py
    - 0012_auto_20190320_2017.py
    - 0013_auto_20190320_2137.py
    - 0014_player_avg_score.py
    - 0015_auto_20190321_2233.py
    - 0016_matchleaderboard.py
    - 0017_customuser_avatar_url.py
    - 0018_auto_20190326_2221.py
    - 0019_auto_20190326_2252.py
    - 0020_auto_20190328_2218.py
    - 0021_matchplayer_from_lineups.py
    - 0022_matchplayer_score.py
    - 0023_auto_20190330_1732.py
    - 0024_matchheadline.py
    - 0025_auto_20190330_2138.py
    - 0026_auto_20190403_0934.py
    - 0027_auto_20190404_0924.py
    - 0028_player_image_url.py
    - 0029_competition_short_name.py
    - 0030_auto_20190405_2134.py
    - 0031_auto_20190409_1729.py
    - 0032_auto_20190416_2031.py
    - 0033_auto_20190419_1451.py
    - 0034_matchevent_status.py
    - 0035_auto_20190420_0933.py
    - 0036_auto_20190420_0946.py
    - 0037_auto_20190423_1822.py
    - 0038_auto_20190423_1843.py
    - 0039_team_abbr.py
    - 0040_auto_20190423_1935.py
    - 0041_matchplayer_played_seconds.py
    - 0042_matchheadline_image_type.py
    - 0043_gamepick_user_swapped.py
    - 0044_matchnotification.py
    - 0045_matchnotification_user.py
    - 0046_matchplayer_avg_score.py
    - 0047_auto_20190530_1246.py
    - 0048_customuser_verified.py
    - 0049_auto_20190620_1642.py
    - 0050_auto_20190627_1132.py
    - 0051_auto_20200524_2026.py
    - 0052_team_ortec_selection_id.py
    - 0053_auto_20200610_0052.py
    - 0054_match_last_synced_at.py
    - 0055_auto_20201025_2202.py
    - 0056_auto_20201128_1415.py
    - 0057_auto_20201129_1959.py
    - 0058_auto_20201204_1637.py
    - 0059_player_nick_name.py
    - 0060_auto_20201217_2051.py
    - 0061_auto_20201217_2051.py
    - 0062_auto_20201218_2045.py
    - 0063_player_soccer_wiki_player.py
    - 0064_auto_20201218_2200.py
    - 0065_auto_20201218_2329.py
    - 0066_matchevent_period.py
    - 0067_auto_20201226_1526.py
    - 0068_auto_20210112_2332.py
    - 0069_auto_20210130_0033.py
    - 0070_customuser_name_changed.py
    - 0071_auto_20210221_1246.py
    - 0072_auto_20210322_1555.py
    - 0073_banpenalty.py
    - 0074_customuser_moderator.py
    - 0075_auto_20210428_1357.py
    - 0076_matchevent_has_real_timestamp.py
    - 0077_customuser_premium.py
    - 0078_subscription_subscriptionhistory_subscriptionrequest.py
    - 0079_subscriptionrequest_app_user.py
    - 0080_game_premium.py
    - 0081_auto_20210602_2102.py
    - 0082_customuser_influencer.py
    - 0083_auto_20210617_1909.py
    - 0084_auto_20210622_1216.py
    - 0085_game_subscription_tier.py
    - 0086_customuser_avg_rank_percent.py
    - 0087_customuser_last_name_change.py
    - 0088_auto_20210920_2057.py
    - 0089_auto_20210920_2145.py
    - 0090_update_models.py
    - 0091_update_models.py
    - 0092_update_models.py
    - 0093_update_models.py
    - 0094_update_models.py
    - 0095_update_models.py
    - 0096_update_models.py
    - 0097_update_models.py
    - 0098_update_models.py
    - 0099_update_models.py
    - 0100_update_models.py
    - 0101_update_models.py
    - 0102_update_models.py
    - 0103_update_models.py
    - 0104_add_new_model.py
    - 0105_update_db_trigger.py
    - 0106_update_fields.py
    - 0107_update_feed_models.py
    - 0108_update_feed_models.py
    - 0109_matchleaderboard_transaction.py
    - 0110_chatmessage_chatroom.py
    - 0111_chatroommember.py
    - 0112_update_import_ids.py
    - 0113_update_position_choices.py
    - 0114_chatroommember_mod.py
    - 0115_match_week.py
    - 0116_competition_config.py
    - 0117_sports_and_pwoerups.py
    - 0118_player_normalized_name.py
    - 0119_normalized_names.py
    - 0120_boosts_initial.py
    - 0121_auto_20240521_1825.py
    - 0122_datafeedsimmodel.py
    - 0123_eventthrottler.py
    - 0124_powerup_conditions.py
    - 0125_powerup_actions.py
    - 0126_update_models.py
    - 0127_add_sport_relation_to_match_and_game.py
    - 0128_ads_sport_to_competition_and_config.py
    - 0129_update_models.py
    - 0130_update_models.py
    - 0131_update_models.py
    - 0132_update_models.py
    - 0133_chatroom_match.py
    - 0134_chatroom_import_id.py
    - 0135_match_enabled.py
    - 0136_ppg_materialized_views.py
    - 0137_auto_20240621_1913.py
    - 0138_product_producttransactions.py
    - 0139_update_models.py
    - 0140_product_transaction_flow.py
    - 0141_producttransactions_external_transaction_id.py
    - 0142_product_name_to_product_id.py
    - 0143_nftbucket.py
    - 0144_auto_20240712_1925.py
    - 0145_assignedplayer_player_nft.py
    - 0146_rename_products_to_store_products.py
    - 0147_rename_product_id_to_store_product_id.py
    - 0148_assignedplayer_nft_id.py
    - 0149_auto_20240717_2247.py
    - 0150_remove_assignedplayer_rarity.py
    - 0151_remove_assignedplayer_user.py
    - 0152_assignedcardpack_card_ids.py
    - 0153_auto_20240719_1958.py
    - 0154_auto_20240718_1218.py
    - 0155_gamepick_assigned_player.py
    - 0156_assignedplayer_rarity.py
    - 0157_auto_20240723_1804.py
    - 0158_add_trigger.py
    - 0159_auto_20240725_1518.py
    - 0160_assignedcardpack_transaction_id.py
    - 0161_storeproducttransactions_origin_store.py
    - 0162_auto_20240730_1312.py
    - 0163_cardpacktype_card_pack_code.py
    - 0164_add_season_start_end.py
    - 0165_nftbucket_players_group.py
    - 0166_nftbucket_opta_id.py
    - 0167_auto_20240802_1405.py
    - 0168_auto_20240802_2242.py
    - 0169_auto_20240802_2350.py
    - 0170_auto_20240806_1411.py
    - 0171_auto_20240806_1857.py
    - 0172_auto_20240809_1632.py
    - 0173_appinbox.py
    - 0174_appinbox_user_id.py
    - 0175_auto_20240813_0157.py
    - 0176_auto_20240813_1633.py
    - 0177_auto_20240815_1507.py
    - 0178_assignedcardpack_refunded.py
    - 0179_auto_20240827_1851.py
    - 0180_gameweekdivision.py
    - 0181_auto_20240903_1225.py
    - 0182_auto_20240903_2211.py
    - 0183_auto_20240905_1623.py
    - 0184_action_nft_category.py
    - 0185_auto_20240925_1343.py
    - 0186_appinbox_game.py
    - 0187_auto_20241010_1600.py
    - 0188_customuser_referral_bonus_used.py
    - 0189_auto_20241014_1412.py
    - 0190_pushnotification.py
    - 0191_cardpacktype_collection.py
    - 0192_badges_banner_frames_userbadges_userbanners_userframes.py
    - __init__.py
  - **templates/**
    - **admin/**
      - **core/**
        - **customuser/**
          - change_list.html
      - custom_task_form.html
    - assign_card_pack.html
    - match_change.html
    - notifications.html
    - send_inbox_message.html
    - terms.html
    - unclaimed_prizes.html
    - withdraw_change.html
  - __init__.py
  - admin.py
  - apps.py
  - authentication.py
  - commands.py
  - const.py
  - exceptions.py
  - models.py
  - notifications.py
  - renderers.py
  - serializers.py
  - sync.py
  - tasks.py
  - tests.py
  - urls.py
  - views.py
  - views_inner.py
- **deploy/**
  - **do/**
    - deployment.yaml
    - service.yaml
  - **docker/**
    - start.sh
  - **eks/**
    - deployment_prod.yaml
    - deployment_qa.yaml
    - ingress_prod.yaml
    - ingress_qa.yaml
    - service.yaml
  - **gce/**
    - cloudbuild_production.yaml
    - cloudbuild_staging.yaml
  - **k8s/**
    - deployment.yaml
- **divisions/**
  - __init__.py
  - apps.py
  - const.py
  - simulation.py
  - sync.py
  - tests.py
- **images/**
  - **laliga-matchfantasy-admin/**
    - deployment_dev.yaml
    - deployment_prd.yaml
    - service_prd.yaml
- **mobile_api/**
  - **settings/**
    - __init__.py
    - base.py
    - development.py
    - production.py
    - staging.py
  - __init__.py
  - celery.py
  - urls.py
  - wsgi.py
- **opta/**
  - __init__.py
  - api.py
  - conv.py
  - parser.py
  - sync.py
  - utils.py
  - websocket.py
- **ortec/**
  - __init__.py
  - api.py
  - conv.py
  - parser.py
  - sync.py
- **rabbit/**
  - **migrations/**
    - 0001_create_events_table.py
    - 0002_create_event_index.py
    - 0003_create_trigger_func.py
    - 0004_create_trigger.py
    - 0005_auto_20190314_1318.py
    - __init__.py
  - __init__.py
  - apps.py
  - models.py
- **revenue_cat/**
  - __init__.py
  - api.py
  - sync.py
- **scripts/**
  - dev.sh
  - makemigrations.sh
  - migrate.sh
- **soccer_wiki/**
  - **migrations/**
    - 0001_initial.py
    - 0002_auto_20190404_1225.py
    - __init__.py
  - __init__.py
  - apps.py
  - models.py
  - sync.py
  - tests.py
  - views.py
- **util/**
  - __init__.py
  - calc.py
  - drf.py
  - events.py
  - gce.py
  - json.py
  - middlewares.py
  - parse.py
  - sort.py
- GAME.json
- README.md
- manage.py
- playersabi.json
- requirements.txt

---

# README.md

# Need to be installed in database
`CREATE EXTENSION pg_trgm;`# laliga-matchfantasy-admin

# Setting up proxy server for Opta

After assigning reserved IP for droplet with tinyproxy installed, check this manual for passing outgoing traffic over reserved IP https://docs.digitalocean.com/products/networking/reserved-ips/how-to/outbound-traffic/

---

## File: `.github/workflows/dev.yml`
- **File Size:** 2646 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add prd yaml file to main

```
name: "[dev] K8S Admin Deploy"
defaults:
  run:
    shell: bash

env:
  DIGITALOCEAN_ACCESS_TOKEN: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
  ENV: dev
  NAMESPACE: fanclash-dev

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  laliga-matchfantasy-admin:  # Create infrastructure for services on push to Main branch
    name: laliga-matchfantasy-admin
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
        with:
          submodules: true
      - name: Install doctl 
        uses: digitalocean/action-doctl@v2
        with:
            token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
      - name: Log in to DO Container Registry 
        run: doctl registry login --expiry-seconds 600

      - name: Configure Kubectl for DOKS
        run: doctl kubernetes cluster kubeconfig save dev-fanclash

      - name: Build and Push Docker Image
        run: |
          SHORT_SHA=$(echo $GITHUB_SHA | cut -c1-7)
          DOCKER_IMAGE="laliga-matchfantasy-admin:$SHORT_SHA"
          docker build -t $DOCKER_IMAGE .
          docker tag $DOCKER_IMAGE registry.digitalocean.com/gameon-ams3/$DOCKER_IMAGE
          docker push registry.digitalocean.com/gameon-ams3/$DOCKER_IMAGE

      - name: Update Image Tag in K8S Deployment
        run: |
          SHORT_SHA=$(echo $GITHUB_SHA | cut -c1-7)
          sed -i 's/TAG_PLACEHOLDER/'"$SHORT_SHA"'/g' $GITHUB_WORKSPACE/images/laliga-matchfantasy-admin/deployment_${{ env.ENV }}.yaml
      
      - name: K8S Admin Deploy
        run: kubectl apply -f images/laliga-matchfantasy-admin/deployment_${{ env.ENV }}.yaml
      
      - name: Check Deployment Health and Rollback if Necessary
        run: |
          if ! kubectl rollout status deployment/mobile-api -n $NAMESPACE; then
            echo "Deployment health check failed. Rolling back..."
            kubectl rollout undo deployment/mobile-api -n $NAMESPACE
          else
            echo "Deployment is healthy."
          fi
        timeout-minutes: 5

      - name: Slack Notification
        if: always()
        uses: rtCamp/action-slack-notify@v2
        env:
          SLACK_CHANNEL: staging-deployments
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_STAGING_URL }}
          SLACK_ICON_EMOJI: ':gameon:'
          SLACK_USERNAME: GitHubAction
          SLACK_COLOR: ${{ job.status }}i # Sets the color of the Slack notification bar to red for failures
          SLACK_TITLE: 'Staging Laliga Admin (mobile API) K8s deployment. Commit message: ${{ github.event.head_commit.message }}'
          SLACK_FOOTER: Powered By GameOn DevOps team
```

## File: `.github/workflows/prd.yml`
- **File Size:** 2901 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add prd yaml file to main

```
name: "[prd] K8S Admin Deploy"
defaults:
  run:
    shell: bash

env:
  DIGITALOCEAN_ACCESS_TOKEN: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
  ENV: prd
  NAMESPACE: prd-fanclash

on:
  push:
    branches:
      - prd
  workflow_dispatch:

jobs:
  laliga-matchfantasy-admin:
    name: laliga-matchfantasy-admin
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
        with:
          submodules: true
      - name: Install doctl
        uses: digitalocean/action-doctl@v2
        with:
            token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
      - name: Log in to DO Container Registry
        run: doctl registry login --expiry-seconds 600

      - name: Configure Kubectl for DOKS
        run: doctl kubernetes cluster kubeconfig save prd-fanclash

      - name: Build and Push Docker Image
        run: |
          SHORT_SHA=$(echo $GITHUB_SHA | cut -c1-7)
          DOCKER_IMAGE="laliga-matchfantasy-admin:$SHORT_SHA"
          docker build -t $DOCKER_IMAGE .
          # Tagging
          docker tag $DOCKER_IMAGE registry.digitalocean.com/gameon-ams3/$DOCKER_IMAGE
          docker tag $DOCKER_IMAGE registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:prd
          # Pushing
          docker push registry.digitalocean.com/gameon-ams3/$DOCKER_IMAGE
          docker push registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:prd

      - name: Update Image Tag in K8S Deployment
        run: |
          SHORT_SHA=$(echo $GITHUB_SHA | cut -c1-7)
          sed -i 's/TAG_PLACEHOLDER/'"$SHORT_SHA"'/g' $GITHUB_WORKSPACE/images/laliga-matchfantasy-admin/deployment_${{ env.ENV }}.yaml

      - name: K8S Admin Deploy
        run: |
            kubectl apply -f images/laliga-matchfantasy-admin/deployment_${{ env.ENV }}.yaml
            kubectl apply -f images/laliga-matchfantasy-admin/service_${{ env.ENV }}.yaml

      - name: Check Deployment Health and Rollback if Necessary
        run: |
          if ! kubectl rollout status deployment/mobile-api -n $NAMESPACE; then
            echo "Deployment health check failed. Rolling back..."
            kubectl rollout undo deployment/mobile-api -n $NAMESPACE
          else
            echo "Deployment is healthy."
          fi
        timeout-minutes: 5
      - name: Slack Notification
        if: always()
        uses: rtCamp/action-slack-notify@v2
        env:
          SLACK_CHANNEL: production-deployments
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_PRD_URL }}
          SLACK_ICON_EMOJI: ':gameon:'
          SLACK_USERNAME: GitHubAction
          SLACK_COLOR: ${{ job.status }}i # Sets the color of the Slack notification bar to red for failures
          SLACK_TITLE: 'Prd Laliga Admin (mobile API) K8s deployment. Commit message: ${{ github.event.head_commit.message }}'
          SLACK_FOOTER: Powered By GameOn DevOps team
```

## File: `GAME.json`
- **File Size:** 3685 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add fields to user, transactions and app inbox / change abi

```
[
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_spender",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_from",
        "type": "address"
      },
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [
      {
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "balance",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      },
      {
        "name": "_spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "payable": true,
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  }
]

```

## File: `README.md`
- **File Size:** 344 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** set machine for production opta proxy

```
# Need to be installed in database
`CREATE EXTENSION pg_trgm;`# laliga-matchfantasy-admin

# Setting up proxy server for Opta

After assigning reserved IP for droplet with tinyproxy installed, check this manual for passing outgoing traffic over reserved IP https://docs.digitalocean.com/products/networking/reserved-ips/how-to/outbound-traffic/
```

## File: `blockchain_web3/GAME.json`
- **File Size:** 3685 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add fields to user, transactions and app inbox / change abi

```
[
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_spender",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_from",
        "type": "address"
      },
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [
      {
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "balance",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      },
      {
        "name": "_spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "payable": true,
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  }
]

```

## File: `blockchain_web3/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 implement cron job for checking Blockchain statuses and change statuses in order and change user balance

```

```

## File: `blockchain_web3/playersabi.json`
- **File Size:** 12607 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** players abi change name

```
[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "AddressEmptyCode",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "ERC1967InvalidImplementation",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "ERC1967NonPayable",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "ERC721IncorrectOwner",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ERC721InsufficientApproval",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "approver",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidApprover",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidOperator",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidOwner",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "receiver",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidReceiver",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "sender",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidSender",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ERC721NonexistentToken",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "FailedInnerCall",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "InvalidInitialization",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "NotInitializing",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "OwnableInvalidOwner",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "OwnableUnauthorizedAccount",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "UUPSUnauthorizedCallContext",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "slot",
        "type": "bytes32"
      }
    ],
    "name": "UUPSUnsupportedProxiableUUID",
    "type": "error"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "approved",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "approved",
        "type": "bool"
      }
    ],
    "name": "ApprovalForAll",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint64",
        "name": "version",
        "type": "uint64"
      }
    ],
    "name": "Initialized",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "Upgraded",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "UPGRADE_INTERFACE_VERSION",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256[]",
        "name": "tokenIds",
        "type": "uint256[]"
      }
    ],
    "name": "batchMint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "getApproved",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "initialOwner",
        "type": "address"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      }
    ],
    "name": "isApprovedForAll",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ownerOf",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "proxiableUUID",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "renounceOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "safeMint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "safeTransferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "safeTransferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "approved",
        "type": "bool"
      }
    ],
    "name": "setApprovalForAll",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "interfaceId",
        "type": "bytes4"
      }
    ],
    "name": "supportsInterface",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "tokenURI",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "transferOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newImplementation",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "upgradeToAndCall",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
]

```

## File: `blockchain_web3/services.py`
- **File Size:** 4860 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** minor syntax fix

```
import json
import os
from web3 import Web3
import logging
from web3.gas_strategies.rpc import rpc_gas_price_strategy

logger = logging.getLogger(__name__)

class CryptoTransactionService:
    def __init__(self):
        WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
        PRIVATE_KEY = os.getenv("PRIVATE_KEY_TOKENS")

        self.web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
        self.private_key = PRIVATE_KEY

    def send_crypto(self, to_address, amount_in_wei, token_contract_address=None):
        account_from = {
            'private_key': self.private_key,
            'address': self.web3.eth.account.from_key(self.private_key).address
        }
        if token_contract_address:
            json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GAME.json')
            with open(json_path) as f:
                contract_abi = json.load(f)
            contract = self.web3.eth.contract(address=token_contract_address, abi=contract_abi)
            self.web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)
            tx = contract.functions.transfer(to_address, amount_in_wei).build_transaction({
                'from': account_from['address'],
                'gasPrice': self.web3.eth.generate_gas_price(),
                'nonce': self.web3.eth.get_transaction_count(account_from['address'])
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, account_from['private_key'])
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt.status == 1:
                return tx_hash.hex()
            else:
                raise ValueError("Transaction failed")
        #     json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GAME.json')
        #     with open(json_path) as f:
        #         contract_abi = json.load(f)
        #     contract = self.web3.eth.contract(address=token_contract_address, abi=contract_abi)
        #     account = self.web3.eth.account.privateKeyToAccount(self.private_key)
        #     self.web3.eth.default_account = account
        #     # send transaction
        #     tx_hash = contract.functions.transfer(to_address , amount_in_wei).transact()
        #     return tx_hash.hex()
        # else:
        #     account = self.web3.eth.account.privateKeyToAccount(self.private_key)
        #     self.web3.eth.default_account = account
        #     tx_hash = self.web3.eth.send_transaction({
        #         'from': account.address,
        #         'to': to_address,
        #         'value': amount_in_wei
        #     })
        #     return tx_hash.hex()
            
        # PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS_TOKENS")
        # nonce = self.web3.eth.get_transaction_count(PUBLIC_ADDRESS)

        # # Get the latest block to retrieve the base fee
        # latest_block = self.web3.eth.get_block('latest')
        # base_fee_per_gas = latest_block.get('baseFeePerGas', 0)

        # transaction = None  # Initialize variable

        # if token_contract_address:
        #     # Load the ABI from the JSON file
        #     current_dir = os.path.dirname(os.path.abspath(__file__))
        #     json_path = os.path.join(current_dir, 'GAME.json')

        #     try:
        #         with open(json_path) as f:
        #             contract_abi = json.load(f)

        #         # Interact with the token contract
        #         contract = self.web3.eth.contract(address=token_contract_address, abi=contract_abi)
                
        #         transaction = contract.functions.transfer(to_address, amount_in_wei).build_transaction({
        #             'nonce': nonce,
        #             'from': PUBLIC_ADDRESS,
        #             'gas': 2000000,
        #         })
                
        #         # gas = self.web3.eth.estimate_gas(transaction)
        #         # gas = int(gas * 1.5)  
        #         # transaction.update({'gas': gas})

        #     except (json.JSONDecodeError, FileNotFoundError) as e:
        #         logger.error(f"Error loading ABI: {str(e)}")
        #         raise ValueError(f"Error loading ABI: {str(e)}")

        # if transaction is not None:
        #     # Sign and send the transaction
        #     signed_tx = self.web3.eth.account.sign_transaction(transaction, self.private_key)
        #     tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
        #     receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        #     if receipt.status == 1:
        #         return tx_hash.hex()
        #     else:
        #         raise ValueError("Transaction failed")
        # else:
        #     raise ValueError("Failed to build transaction")

```

## File: `blockchain_web3/sync.py`
- **File Size:** 819 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 implement cron job for checking Blockchain statuses and change statuses in order and change user balance

```
from core.models import Order
from .utils import get_transaction_status, create_transaction_on_completed

def update_order_statuses():
    print("Running check and update order statuses")
    orders = Order.objects.filter(blockchain_order_status=Order.MINT_IN_PROGRESS).filter(delivered=False).filter(
        payment_platform_status=Order.COMPLETED)

    for order in orders:
        old_status = order.blockchain_order_status
        new_status = get_transaction_status(order.blockchain_uuid)
        print("old:", old_status, "new:", new_status)
        if new_status != old_status:
            order.blockchain_order_status = new_status
            order.save()
            if order.blockchain_order_status == Order.MINT_SUCCEEDED and not order.delivered:
                create_transaction_on_completed(order.id)

```

## File: `blockchain_web3/tasks.py`
- **File Size:** 13724 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix staging site

```
from datetime import timedelta
import uuid
from celery import shared_task
from django.utils import timezone
from core.models import CardPackType, CustomUser, AssignedCardPack, AssignedPlayer, NftBucket, StoreProduct, Transactions, StoreProductTransactions
from blockchain_web3.services import CryptoTransactionService
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os
import boto3
import requests
import logging

# Set up logging
logger = logging.getLogger(__name__)

WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
FOLDER = os.getenv("FOLDER")
CONTRACT_ADDRESS_SEASON = os.getenv("CONTRACT_ADDRESS_SEASON")
FOLDER_SEASON = os.getenv("FOLDER_SEASON")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")

def get_metadata_url(player):
    rarity = player.rarity
    nft_bucket = NftBucket.objects.get(pk=player.player_nft_id)

    if rarity == "common":
        return nft_bucket.common_metadata
    elif rarity == "uncommon":
        return nft_bucket.uncommon_metadata
    elif rarity == "rare":
        return nft_bucket.rare_metadata
    elif rarity == "ultra_rare":
        return nft_bucket.ultra_rare_metadata
    elif rarity == "legendary":
        return nft_bucket.legendary_metadata
    else:
        return None

def mint_nfts_for_cardpacks(card_packs):
    web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to playersabi.json
    json_path = os.path.join(current_dir, 'playersabi.json')

    # Open and load the JSON file
    with open(json_path) as f:
        contract_abi = json.load(f)
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name="us-east-1"
    )

    for pack in card_packs:
        print(f"Processing card pack {pack.id}")
        try:
            # Get the CustomUser wallet address
            user = CustomUser.objects.get(pk=pack.user_id)
            # If pack.collectio is season then folder is FOLDER_SEASON and contract address is CONTRACT_ADDRESS_SEASON
            if pack.collection == "season":
                FOLDER = FOLDER_SEASON
                CONTRACT_ADDRESS = CONTRACT_ADDRESS_SEASON
            if not user.wallet_address:
                logger.warning(f"User {user.id} does not have a wallet address, skipping")
                continue

            # Get the NFT IDs and metadata URLs from the assigned players
            nft_ids = []
            metadata_files = []
            for player_nft_id in pack.card_ids:
                assigned_player = AssignedPlayer.objects.get(id=player_nft_id)
                nft_ids.append(int(assigned_player.nft_id))

                metadata_url = get_metadata_url(assigned_player)
                if metadata_url:
                    response = requests.get(metadata_url)
                    if response.status_code == 200:
                        metadata = response.json()
                        metadata_files.append({
                            'token_id': assigned_player.nft_id,
                            'metadata': metadata
                        })
                    else:
                        logger.warning(f"Failed to fetch metadata from {metadata_url}, received status code {response.status_code}")
                else:
                    logger.warning(f"No metadata URL found for player {assigned_player.id} with rarity {assigned_player.rarity}")
            userWallet = user.wallet_address
            # Convert userWallet to string
            to = str(userWallet)
            ids = nft_ids
            # Convert to list of integers
            ids = [int(i) for i in ids]
            # Prepare the   transaction
            nonce = web3.eth.get_transaction_count(PUBLIC_ADDRESS)

            # Upload metadata to S3
            for metadata in metadata_files:
                metadata_key = f"{FOLDER}/{metadata['token_id']}"
                s3_client.put_object(
                    Bucket=S3_BUCKET,
                    Key=metadata_key,
                    Body=json.dumps(metadata['metadata']),
                    ContentType='application/json'
                )
                print(f"Metadata for token ID {metadata['token_id']} uploaded to S3")

            txn = contract.functions.batchMint(to, ids).build_transaction({
                'nonce': nonce,
                'from': PUBLIC_ADDRESS
            })
            # Sign and send the transaction
            signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
            txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
            
            # Mark the pack as revealed
            pack.revealed = True
            pack.revealed_at = timezone.now()
            pack.save()
            print(f"Successfully minted NFTs for card pack {pack.id} to {user.wallet_address}")

        except Exception as e:
            logger.error(f"Error minting NFTs for card pack {pack.id}: {str(e)}")
            print(f"Error minting NFTs for card pack {pack.id}: {str(e)}")

@shared_task
def process_mint_nfts_for_expired_cardpacks():
    print("Starting mint_nfts_for_expired_cardpacks task")
    # Query for assigned card packs that are older than 48 hours and not revealed
    threshold_time = timezone.now() - timedelta(hours=50)
    try:
        # Query for all assigned card packs
        card_packs = AssignedCardPack.objects.filter(
            opened=True,
            opened_at__lte=threshold_time,
            revealed=False
        )
        print(f"Found {card_packs.count()} card packs to process")

        for pack in card_packs:
            if pack.store_transaction_id and not pack.refunded:
                print(f"Processing minting for card pack {pack.id}")
                mint_nfts_for_cardpacks([pack])
            else:
                print(f"Removing card_ids for card pack {pack.id} due to missing store_transaction_id or refunded status")
                # Remove card_ids and mark the pack as revealed
                pack.revealed = True
                pack.revealed_at = timezone.now()
                pack.save(update_fields=['revealed', 'revealed_at'])

    except Exception as e:
        logger.critical(f"Critical error in mint_nfts_for_expired_cardpacks: {str(e)}")
        
@shared_task
def process_pending_crypto_transactions():
    print("Starting process_pending_crypto_transactions task")
    
    # Define the contract addresses for GAME and LAPT tokens
    GAME_CONTRACT_ADDRESS = os.getenv('GAME_CONTRACT_ADDRESS')
    LAPT_CONTRACT_ADDRESS = os.getenv('LAPT_CONTRACT_ADDRESS')

    # Initialize the crypto transaction service
    crypto_service = CryptoTransactionService()

    # Fetch pending GAME and LAPT transactions
    transactions = Transactions.objects.filter(
        delivered=False,
        object_type__in=[Transactions.GAME, Transactions.LAPT]
    )
    print(f"Found {transactions.count()} transactions to process")

    for transaction in transactions:
        try:
            # Determine which token to send based on the object type
            token_contract_address = GAME_CONTRACT_ADDRESS if transaction.object_type == Transactions.GAME else LAPT_CONTRACT_ADDRESS
            token_type = "GAME" if transaction.object_type == Transactions.GAME else "LAPT"

            # Check if the wallet address is valid
            to_address = transaction.user.wallet_address
            if not to_address:
                logger.warning(f"Invalid wallet address for transaction {transaction.id}")
                # Mark the transaction as invalid or skip it
                transaction.status = 'invalid'
                transaction.save()
                continue  # Skip to the next transaction

            # Convert the transaction amount to Wei using Web3's `to_wei` method
            amount_in_wei = Web3.to_wei(transaction.amount, 'ether')

            # Send the cryptocurrency
            tx_hash = crypto_service.send_crypto(to_address, amount_in_wei, token_contract_address)

            # Update the transaction record as delivered
            transaction.delivered = True
            transaction.blockchain_uuid = tx_hash
            transaction.save()

            print(f"Successfully processed {token_type} transaction {transaction.id} for user {transaction.user_id}")

        except ValueError as ve:
            logger.error(f"Transaction {transaction.id} failed due to: {str(ve)}")
            print(f"Error processing transaction {transaction.id}: {str(ve)}")

        except Exception as e:
            logger.error(f"Error processing transaction {transaction.id}: {str(e)}")
            print(f"Error processing transaction {transaction.id}: {str(e)}")
@shared_task
def process_pending_cardpack_transactions():
    print("Starting process_pending_cardpack_transactions task")
    
    # Filter transactions for kickoff packs where delivery is false
    transactions = Transactions.objects.filter(
        delivered=False,
        object_type__in=[
            Transactions.SEASON_PACK_1,
            Transactions.SEASON_PACK_2,
            Transactions.SEASON_PACK_3
        ]
    )
    
    print(f"Found {transactions.count()} pending kickoff pack transactions to process")

    for transaction in transactions:
        try:
            # Get the user for the transaction
            user = transaction.user

            # Determine the card pack type based on the object_type
            if transaction.object_type == Transactions.SEASON_PACK_1:
                pack_type_uuid = 'f9adef06-85fd-498b-83f1-86ac25a16367'
                pack_type_staging_uuid = 'cd8fbb55-692d-491c-b4d3-4c1e42afec20'
                product_id = 'season_24_pack_1' 
                pack_name = "Season Pack 1"
            elif transaction.object_type == Transactions.SEASON_PACK_2:
                pack_type_uuid = 'd15c5248-cdfe-45bc-aec6-83dbd2814965'
                pack_type_staging_uuid = 'c0c6b781-14f8-40f8-aefb-19f56a4021d5'
                product_id = 'season_24_pack_2'
                pack_name = "Season Pack 2"
            elif transaction.object_type == Transactions.SEASON_PACK_3:
                pack_type_uuid = 'b4825f20-c611-4316-98ee-fc9433d9cd00'
                pack_type_staging_uuid = '064bfff2-4e8e-4701-bfc4-348a248df6be'
                product_id = 'season_24_pack_3'
                pack_name = "Season Pack 3"
            else:
                logger.error(f"Invalid transaction type {transaction.object_type} for transaction {transaction.id}")
                continue

            # Check if the user has a wallet address
            if not user.wallet_address:
                logger.warning(f"User {user.id} does not have a wallet address, skipping")
                continue

            # Fetch the StoreProduct instance
            product = StoreProduct.objects.get(store_product_id=product_id)

            # Create and save the StoreProductTransaction, linking it with the transaction
            store_transaction = StoreProductTransactions.objects.create(
                transaction=transaction,
                user=user,
                external_transaction_id=str(uuid.uuid4()),  # Generate a unique external transaction ID
                initiated=True,
                initiated_at=timezone.now(),
                product=product,
                origin_store="DivisionReward",  # Update with the actual origin store if needed
            )

            # Try to create and assign the new card pack with `pack_type`
            card_pack_type = None
            try:
                # Get the `CardPackType` instance for the primary `pack_type_uuid`
                card_pack_type = CardPackType.objects.get(pk=pack_type_uuid)
            except CardPackType.DoesNotExist:
                logger.warning(f"CardPackType with id {pack_type_uuid} does not exist, trying pack_type_staging {pack_type_staging_uuid}")
                print(f"CardPackType with id {pack_type_uuid} does not exist, trying pack_type_staging {pack_type_staging_uuid}")
                # Fallback to `pack_type_staging`
                try:
                    card_pack_type = CardPackType.objects.get(pk=pack_type_staging_uuid)
                except CardPackType.DoesNotExist:
                    logger.error(f"Both CardPackType {pack_type_uuid} and staging {pack_type_staging_uuid} do not exist.")
                    continue

            # Create the assigned card pack using the correct store_transaction's primary key (id)
            new_card_pack = AssignedCardPack(
                user=user,
                card_pack_type=card_pack_type,  # Assign the `CardPackType` instance
                opened=False,
                store_transaction=store_transaction  # Link to the `StoreProductTransactions` instance
            )
            new_card_pack.save()

            # Mark the transaction as delivered
            transaction.delivered = True
            transaction.save()

            print(f"Assigned {pack_name} to user {user.id} for transaction {transaction.id}")

        except Exception as e:
            logger.error(f"Error processing card pack transaction {transaction.id}: {str(e)}")
            print(f"Error processing card pack transaction {transaction.id}: {str(e)}")

```

## File: `blockchain_web3/utils.py`
- **File Size:** 1745 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 implement cron job for checking Blockchain statuses and change statuses in order and change user balance

```
from django.db import transaction
from web3 import Web3
from core.models import Order, Transactions, Item
import os

w3 = Web3(Web3.HTTPProvider(os.getenv("ETHEREUM_URL")))

def get_transaction_status(transaction_hash):
    print("get transaction status")
    tx_receipt = w3.eth.getTransactionReceipt(transaction_hash)
    print("receipt:", tx_receipt)
    if tx_receipt is None:
        return Order.MINT_NOT_STARTED
    elif tx_receipt['status'] == 1:
        return Order.MINT_SUCCEEDED
    else:
        return Order.MINT_FAILED

@transaction.atomic
def create_transaction_on_completed(order_id):
    try:
        order_instance = Order.objects.select_for_update().get(id=order_id)
        if not Transactions.objects.filter(order_id=order_id).exists():

            order_instance.delivered = True
            order_instance.save()

            tr = Transactions.objects.create(
                amount=order_instance.amount,
                quantity=order_instance.quantity,
                user_id=order_instance.user_id,
                text="internal payment method created transaction for ItemID:"
                     f" {order_instance.item_id}, quantity: {order_instance.quantity}, amount: {order_instance.amount}",
                blockchain_uuid=order_instance.blockchain_uuid,
                order_id=order_instance.id,
                object_type='v' if order_instance.item.type == Item.CREDIT_TOKEN else 'n'
            )

            return tr

        else:
            print(f"A transaction already exists for order with ID {order_instance.id}")
            return None
    except Exception as e:
        transaction.set_rollback(True)
        print(f"Error occurred while creating transaction: {e}")
        return None

```

## File: `core/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `core/admin.py`
- **File Size:** 41211 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add new packs

```
from datetime import timedelta

from django import forms
from django.db import models
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin import SimpleListFilter
from django.contrib.admin.widgets import AutocompleteSelect
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import BaseInlineFormSet
from django.http import HttpResponseRedirect
from django.utils import timezone, html
from django.utils.safestring import mark_safe
from django.conf import settings
from django.shortcuts import render, redirect
from core.notifications import send_push_to_user, send_push_to_all
from core import const
from core.models import AppInbox, AssignedCardPack, CustomUser, NftBucket, Rewards, Team, Match, Player, Game, Action, PowerUp, PowerUpAction, MatchReward, \
    CompetitionConfig, Competition, MatchLeaderboard, Transactions, BanPenalty, CompetitionEdition, CompetitionPhase, \
    ManualSubscription, DataFeedSimModel, MatchEvent, OptaFeedItem, OptaFeedItemVersion, GameEvent, GamePowerUp, \
    StoreProduct, StoreProductTransactions, DivisionReward, UserDivision, UserGameWeekHistory, GameWeek, Division, \
    GameSeason, CardPackType

from soccer_wiki.models import SoccerWikiPlayer
from core import commands
from opta.sync import sync_feed
import uuid
from csvexport.actions import csvexport
from django import forms
from core.models import CustomUser
from django.urls import path

class NotificationForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter notification title'}), label="Title")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter notification message'}), label="Message")
    user_ids = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter comma-separated user IDs'}),
        required=False,
        label="User IDs (comma-separated)"
    )

class BanPenaltiesInline(admin.TabularInline):
    model = BanPenalty
    readonly_fields = ('start_time',)
    ordering = ('-start_time',)
    extra = 0
    fields = ('start_time', 'end_time', 'reason',)

class UserGameWeekHistoriesInline(admin.TabularInline):
    model = UserGameWeekHistory
    extra = 0  # Number of empty forms to display
    readonly_fields = ('week_division_position', 'week_division_tier', 'week_points', 'week_coins','new_division_tier', 'status')
    fields = ('week_division_position', 'week_division_tier', 'week_points', 'week_coins', 'new_division_tier', 'status')

class DivisionsInline(admin.TabularInline):
    model = UserDivision
    extra = 0  # Number of empty forms to display
    fields = ('game_week_name', 'division_tier')
    readonly_fields = ('game_week_name', 'division_tier')

    def game_week_name(self, obj):
        return obj.game_week.name
    game_week_name.short_description = 'Week period'

    def division_tier(self, obj):
        return obj.division.tier
    division_tier.short_description = 'Division Tier'

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]
    list_filter = (
        'verified', 'subscription_tier', 'moderator', 'premium', 'influencer',
        'email_verified', 'name_changed', 'last_name_change', 'created_at', 'updated_at',
    )
    search_fields = (
        'name', 'email', 'paypal_email', 'firebase_id', 'referral_code',
        'wallet_address', 'sequence_session_id', 'verification_token'
    )
    fields = [field.name for field in CustomUser._meta.fields if field.name not in ('id', 'password')]
    readonly_fields = (
        'firebase_id', 'balance', 'referral_code', 'referrer_id', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)
    inlines = (BanPenaltiesInline, UserGameWeekHistoriesInline, DivisionsInline)
    autocomplete_fields = ('referrer',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-notification/', self.admin_site.admin_view(self.send_notification), name='send-notification'),
        ]
        return custom_urls + urls

    def send_notification(self, request):
        if request.method == 'POST':
            form = NotificationForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                message = form.cleaned_data['message']
                user_ids = form.cleaned_data['user_ids']
                if not user_ids:
                    send_push_to_all.delay(title, message)
                else:
                    user_id_list = user_ids.split(',')
                    for user_id in user_id_list:
                        try:
                            user = CustomUser.objects.get(id=user_id.strip())
                            if user.firebase_id and user.firebase_id.startswith("Expo"):
                                send_push_to_user.delay(user.id, title, message)
                        except CustomUser.DoesNotExist:
                            continue
                messages.success(request, "Notification tasks have been initiated.")
                return redirect('..')
        else:
            form = NotificationForm()

        return render(request, '../templates/notifications.html', {'form': form})

class CompetitionConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'filter', 'enabled', 'sport')
    fields = ('sport', 'name', 'filter', 'enabled')
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            competition = obj.related_competition
            if competition is not None:
                competition.enabled = obj.enabled
                competition.save()
        super().save_model(request, obj, form, change)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'code','enabled')
    fields = ('name', 'code', 'short_name','enabled')
    readonly_fields = ('name', 'code',)

class CompetitionEditingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'competition', 'import_id')
    list_filter = ('competition',)
    search_fields = ('name', 'import_id')
    fields = ('import_id', 'name', 'competition', 'enabled',)
    readonly_fields = ('import_id', 'name', 'competition',)

    def has_change_permission(self, request, obj=None):
        return True

class CompetitionPhaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'import_id', 'competition_name')
    list_filter = ('competition_edition__competition',)
    search_fields = ('name', 'import_id')

    def competition_name(self, obj):
        return obj.competition_edition.competition.name

    competition_name.short_description = 'Competition'

    def has_change_permission(self, request, obj=None):
        return False

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'abbr')
    search_fields = ('id', 'name', 'short_name', 'abbr',)
    fields = ('short_name', 'abbr', 'crest_url', 'name', 'country', 'region')
    readonly_fields = ('name', 'country', 'region',)

class IsSimulationFilter(SimpleListFilter):
    title = 'Is Simulated'
    parameter_name = 'is_simulated'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.exclude(simulation_from_match__isnull=True)
        elif value == 'No':
            return queryset.filter(simulation_from_match__isnull=True)
        return queryset

class MatchTimeFilter(SimpleListFilter):
    title = 'Match Time'
    parameter_name = 'match_time'

    def lookups(self, request, model_admin):
        return (
            ('today', 'Today'),
            ('past_7_days', 'Past 7 days'),
            ('next_7_days', 'Next 7 days'),
        )

    def queryset(self, request, queryset):
        now = timezone.now()
        start = now.replace(hour=0, minute=0, second=0)

        value = self.value()
        if value == 'today':
            return queryset.filter(match_time__gte=start, match_time__lt=start + timedelta(hours=24))
        elif value == 'past_7_days':
            return queryset.filter(match_time__gte=start - timedelta(days=7), match_time__lt=start)
        elif value == 'next_7_days':
            return queryset.filter(match_time__gte=start, match_time__lt=start + timedelta(days=7))
        return queryset

class CompetitionFilter(SimpleListFilter):
    title = 'Competition'
    parameter_name = 'competition'

    def lookups(self, request, model_admin):
        return tuple((c.pk, c.name) for c in Competition.objects.order_by('name'))

    def queryset(self, request, queryset):
        value = self.value()

        if value:
            return queryset.filter(competition=value)
        return queryset

class MatchRewardFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        positions = []
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                min_position = form.cleaned_data.get('min_position')
                max_position = form.cleaned_data.get('max_position')
                if min_position is not None:
                    positions.append((min_position, max_position))
        print(positions)
        if not commands.validate_positions(positions):
            raise ValidationError(
                "Invalid position ranges. Please ensure there are no gaps and min_position is less than or equal to "
                "max_position.")

class MatchRewardInline(admin.TabularInline):
    model = MatchReward
    extra = 1  # Number of empty forms to display

    fields = ('min_position', 'max_position', 'amount', 'game', 'lapt', 'event', 'balls', 'signed_balls', 'shirts', 'signed_shirts', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3')
    ordering = ('min_position',)

class MatchAdmin(admin.ModelAdmin):
    def toggle_enabled(self, request, queryset):
        for match in queryset:
            match.enabled = not match.enabled
            match.save()

    toggle_enabled.short_description = "Toggle enabled status of selected matches"

    list_display = ('enabled', 'import_id', 'home_team', 'away_team',
                    'status', 'match_time', 'competition_name',
                    'is_simulated', 'leaderboard_link',)
    list_display_links = ('import_id',)
    list_filter = ('enabled', IsSimulationFilter, 'match_type', MatchTimeFilter, 'status', CompetitionFilter)
    search_fields = ('id', 'import_id',)
    inlines = (MatchRewardInline,)
    change_form_template = "match_change.html"
    ordering = ('-match_time',)
    actions = [toggle_enabled]

    def response_change(self, request, obj):
        if "_start-short-simulation" in request.POST:
            obj.create_simulation(duration=timedelta(minutes=10))
            self.message_user(request, "Simulation successfully started")
            return HttpResponseRedirect(".")
        elif "_start-long-simulation" in request.POST:
            obj.create_simulation(duration=timedelta(minutes=90))
            self.message_user(request, "Simulation successfully started")
            return HttpResponseRedirect(".")

        return super().response_change(request, obj)

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields if f.name != 'match_type']

    def is_simulated(self, obj):
        return obj.simulation_from_match is not None

    def competition_name(self, obj):
        return obj.competition.name

    def leaderboard_link(self, obj):
        return mark_safe(
            '<a href="/admin/core/matchleaderboard/?match_id={}" target="_blank">Leaderboard</a>'.format(obj.pk))

    leaderboard_link.short_description = 'Leaderboard'

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'full_name', 'first_name', 'last_name', 'nick_name',)
    list_display = ('id', 'first_name', 'last_name', 'nick_name', 'soccer_wiki_player_id',)
    autocomplete_fields = ('soccer_wiki_player',)

class SoccerWikiPlayerAdmin(admin.ModelAdmin):
    search_fields = ('import_id', 'first_name', 'second_name')
    list_display = ('id', 'first_name', 'second_name', 'import_id', 'internal_image_url')

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id',)
    readonly_fields = ('match', 'user',)

class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'score', 'category', 'nft_category')
    ordering = ('ordering',)

class PowerUpActionInline(admin.TabularInline):
    model = PowerUpAction
    ordering = ('ordering',)

class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('store_product_id', 'description', 'price', 'currency', 'google_product_id', 'apple_product_id')
    ordering = ('id', 'store_product_id', 'price', 'currency')
    actions = [csvexport]
    csvexport_export_fields = [
        'store_product_id',
        'price',
        'currency',
        'google_product_id',
        'apple_product_id',
    ]
    csvexport_selected_fields = [
        'store_product_id',
        'price',
        'currency',
        'google_product_id',
        'apple_product_id',
    ]

class PowerUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport')
    ordering = ('id',)
    inlines = [PowerUpActionInline]

class MatchLeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'position', 'score', 'get_match')
    ordering = ('position',)
    actions = [csvexport]
    csvexport_export_fields = [
        'user.name',
        'user.email',
        'position',
        'score',
        'user.verified',
        'match.id',
    ]
    csvexport_selected_fields = [
        'user.name',
        'user.email',
        'position',
        'score',
        'user.verified',
        'match.id',
    ]

    def get_match(self, obj):
        if obj.match is not None:
            label =  f"{obj.match}"
            return html.format_html(f'<a href="/admin/core/match/{obj.match_id}/change/">{label}</a>')
        return html.format_html('<a href="/admin/core/match/{}/change/">No match set</a>', obj.match_id)
    get_match.short_description = 'Match'

    def get_queryset(self, request):
        qs = super(MatchLeaderboardAdmin, self).get_queryset(request)
        return qs.select_related('user')

    def user_name(self, obj):
        return '{} ({})'.format(obj.user.name, obj.user_id)

    def user_email(self, obj):
        return '{}'.format(obj.user.email)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ObjectTypeFilter(SimpleListFilter):
    title = 'Object Type'
    parameter_name = 'object_type'

    def lookups(self, request, model_admin):
        return Transactions.OBJECT_TYPE

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(object_type=self.value())
        return queryset

class DeliveredFilter(SimpleListFilter):
    title = 'Delivered Status'
    parameter_name = 'delivered'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Delivered'),
            ('False', 'Not Delivered'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(delivered=True)
        elif self.value() == 'False':
            return queryset.filter(delivered=False)
        return queryset

class UnclaimedPrizesFilter(SimpleListFilter):
    title = 'Unclaimed Prizes'
    parameter_name = 'unclaimed'

    def lookups(self, request, model_admin):
        return (
            ('undelivered', 'Undelivered'),
            ('unsent', 'Unsent'),
            ('both', 'Undelivered & Unsent'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'undelivered':
            return queryset.filter(delivered=False)
        elif value == 'unsent':
            return queryset.filter(sent=False)
        elif value == 'both':
            return queryset.filter(delivered=False, sent=False)
        return queryset

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user_name', 'amount', 'object_type', 'quantity', 'delivered', 'sent')
    list_filter = (ObjectTypeFilter, DeliveredFilter, UnclaimedPrizesFilter, 'created_at')
    search_fields = ('user__name', 'user__email', 'blockchain_uuid', 'text')
    ordering = ('-created_at',)

    # Make 'delivered' and 'sent' fields editable in both the list and detail view
    list_editable = ('delivered', 'sent')

    # Include 'delivered' and 'sent' fields in the detail view
    fields = ('user', 'amount', 'object_type', 'quantity', 'delivered', 'sent')

    # Ensure these fields are editable and not readonly
    def get_readonly_fields(self, request, obj=None):
        return []

    def user_name(self, obj):
        return f'{obj.user.name} ({obj.user_id})'

    # Optionally, you can override save_model to include any custom logic if needed
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class ManualSubscriptionForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        CustomUser.objects.all(), required=True,
        widget=AutocompleteSelect(ManualSubscription.user.field.remote_field, admin.site),
    )
    subscription_duration = forms.ChoiceField(choices=(
        (i + 1, '{} Month ({}$)'.format(i + 1, (i + 1) * settings.PREMIUM_SUBSCRIPTION_PRICE))
        for i in range(12)
    ), required=True, label='Subscription Duration')

    def clean(self):
        duration_in_months = int(self.cleaned_data['subscription_duration'])
        amount = settings.PREMIUM_SUBSCRIPTION_PRICE * duration_in_months

        with transaction.atomic():
            locked_user = CustomUser.objects.select_for_update().get(pk=self.cleaned_data['user'].pk)
            if locked_user.balance < amount:
                raise ValidationError('Not enough money on balance')

    class Meta:
        model = ManualSubscription
        exclude = ['expires_at', 'tier']

class ManualSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user_name', 'tier', 'expires_at', 'transaction_amount')
    autocomplete_fields = ('user',)
    ordering = ('-created_at',)
    search_fields = ('user__name',)

    def user_name(self, obj):
        return '{} ({})'.format(obj.user.name, obj.user_id)

    def transaction_amount(self, obj):
        return obj.transaction.first().amount

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj:
            return super(ManualSubscriptionAdmin, self).get_form(request, obj, change, **kwargs)
        # use custom form only for `add` action
        return ManualSubscriptionForm

    def save_model(self, request, obj, form, change):
        # calculate expires at and amount to be written off
        duration_in_months = int(form.cleaned_data['subscription_duration'])
        obj.expires_at = timezone.now() + timedelta(days=30 * duration_in_months)
        obj.tier = const.TIER_PREMIUM
        amount = settings.PREMIUM_SUBSCRIPTION_PRICE * duration_in_months

        with transaction.atomic():
            locked_user = CustomUser.objects.select_for_update().get(pk=obj.user.pk)
            if locked_user.balance < amount:
                raise ValidationError('Not enough money on balance')

            print('Amount if', amount)

            super().save_model(request, obj, form, change)
            # insert transaction pointing to subscription
            Transactions.objects.create(
                user=locked_user,
                amount=-amount,
                text='Manual subscription',
                manual_subscription=obj,
                delivered=True,
            )
            locked_user.update_premium()

class MatchInline(admin.TabularInline):
    model = Match

class DataFeedSimAdmin(admin.ModelAdmin):
    list_display = ('id', 'import_id', 'get_match', 'processed')

    def get_match(self, obj):
        if obj.match is not None:
            label =  f"{obj.match}"
            return html.format_html(f'<a href="/admin/core/datafeedsimmodel/{obj.id}/change/">{label}</a>')
        return html.format_html('<a href="/admin/core/datafeedsimmodel/{}/change/">No match set</a>', obj.id)
    get_match.short_description = 'Match'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'match':
            kwargs["queryset"] = Match.objects.filter(
                    simulation_from_match_id__isnull=False
                ).order_by("-match_time")  # We just need simulated matches only
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            matchtmp = obj.match
            if obj.import_id is None:
                obj.import_id = matchtmp.get_import_id()
            if (obj.import_id is not None and obj.import_id != "") and \
                (obj.json_events is None or obj.json_events == "" or obj.json_events == "null"):
                obj.json_events = settings.OPTA_CLIENT.get_match_events(obj.import_id)
                obj.processed = False
            if not obj.processed:
                if matchtmp.import_id is None:
                    matchtmp.import_id = f"simulation-{uuid.uuid4()}-{obj.import_id}"
                # cleanup game events
                obj.match.status = "g"
                obj.match.save()
                MatchEvent.objects.filter(match=obj.match).delete()
                optaItems = OptaFeedItem.objects.filter(match=obj.match)
                OptaFeedItemVersion.objects.filter(item__in=optaItems).delete()
                optaItems.delete()
                GameEvent.objects.filter(game__in=Game.objects.filter(match=obj.match)).delete()
                GamePowerUp.objects.filter(game__in=Game.objects.filter(match=obj.match)).delete()
                # sync feed again
                sync_feed(matchtmp, obj.json_events, True)
                obj.processed = True
                messages.success(request, "Events has been processed.")
            super().save_model(request, obj, form, change)

class InboxForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    user_ids = forms.CharField(
        required=False,
        help_text="Comma-separated list of user IDs to send the inbox message to. Leave blank to send to all users."
    )
    status = forms.ChoiceField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    priority = forms.ChoiceField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    category = forms.ChoiceField(choices=[('Update', 'Update'), ('Reward', 'Reward')])
    image_url = forms.URLField(required=False)
    link_url = forms.URLField(required=False)
    
@admin.register(AppInbox)
class AppInboxAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'category', 'user', 'created_at', 'read')
    
    def send_inbox_message(self, request):
        if request.method == 'POST':
            form = InboxForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                user_ids = form.cleaned_data['user_ids']
                status = form.cleaned_data['status']
                priority = form.cleaned_data['priority']
                category = form.cleaned_data['category']
                image_url = form.cleaned_data['image_url']
                link_url = form.cleaned_data['link_url']
                
                if not user_ids:
                    # Send to all users
                    users = CustomUser.objects.all()
                else:
                    user_id_list = [user_id.strip() for user_id in user_ids.split(',')]
                    users = CustomUser.objects.filter(id__in=user_id_list)

                for user in users:
                    AppInbox.objects.create(
                        title=title,
                        description=description,
                        status=status,
                        priority=priority,
                        category=category,
                        image_url=image_url,
                        link_url=link_url,
                        user=user,
                    )
                
                messages.success(request, "Inbox messages have been successfully sent.")
                return redirect('..')
        else:
            form = InboxForm()

        return render(request, '../templates/send_inbox_message.html', {'form': form})

    # Register the admin action
    actions = [send_inbox_message]

@admin.register(UserDivision)
class UserDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'division', 'game_week', 'join_date')
    search_fields = ('user__username', 'division__name', 'game_week__name', 'user_id')
    list_filter = ('division', 'game_week')

@admin.register(UserGameWeekHistory)
class UserGameWeekHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'game_week', 'week_division', 'week_division_position', 'week_division_tier',
        'week_points', 'week_coins', 'new_division', 'new_division_tier', 'status'
    )
    search_fields = ('user__username', 'game_week__name', 'week_division__name', 'new_division__name')
    list_filter = ('game_week', 'week_division', 'new_division', 'status')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tier', 'percentage', 'relegation_min_range', 'relegation_max_range', 'promotion_min_range', 'promotion_max_range',  'updated_at',)
    search_fields = ('id', 'name',)
    list_filter = ('tier',)

@admin.register(GameSeason)
class GameSeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_at', 'end_at','created_at')
    search_fields = ('name',)

@admin.register(CardPackType)
class CardPackTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'card_pack_code', 'description', 'image', 'tier1', 'tier2', 'tier3', 'tier4', 'tier5', 'created_at')
    search_fields = ('name',)

@admin.register(NftBucket)
class NftBucketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'team_id', 'age', 'game_position', 'position', 'nationality', 
        'common_limit', 'uncommon_limit', 'rare_limit', 'ultra_rare_limit', 'legendary_limit',
    )
    search_fields = ('name', 'team_id', 'nationality', 'position', 'game_position',)
    list_filter = ('game_position', 'position', 'team_id',)

    def player_name(self, obj):
        return f"{obj.name}"

    player_name.short_description = 'Player Name'

class DivisionRewardForm(forms.ModelForm):
    credits = forms.FloatField(label="Credits")
    game_token = forms.FloatField(label="Game Token")
    lapt_token = forms.FloatField(label="Lapt Token")
    event_tickets = forms.IntegerField(label="Event Tickets")
    ball = forms.IntegerField(label="Ball")
    signed_ball = forms.IntegerField(label="Signed Ball")
    shirt = forms.IntegerField(label="Shirt")
    signed_shirt = forms.IntegerField(label="Signed Shirt")
    kickoff_pack_1 = forms.IntegerField(label="Kickoff Pack 1", required=False)
    kickoff_pack_2 = forms.IntegerField(label="Kickoff Pack 2", required=False)
    kickoff_pack_3 = forms.IntegerField(label="Kickoff Pack 3", required=False)
    season_pack_1 = forms.IntegerField(label="Season Pack 1", required=False)
    season_pack_2 = forms.IntegerField(label="Season Pack 2", required=False)
    season_pack_3 = forms.IntegerField(label="Season Pack 3", required=False)

    class Meta:
        model = DivisionReward
        fields = ['week', 'division', 'min_position', 'max_position']  # Exclude 'reward'

    def __init__(self, *args, **kwargs):
        super(DivisionRewardForm, self).__init__(*args, **kwargs)
        
        # Ensure reward exists before accessing it
        if self.instance and self.instance.reward:
            self.fields['credits'].initial = self.instance.reward.credits
            self.fields['game_token'].initial = self.instance.reward.game_token
            self.fields['lapt_token'].initial = self.instance.reward.lapt_token
            self.fields['event_tickets'].initial = self.instance.reward.event_tickets
            self.fields['ball'].initial = self.instance.reward.ball
            self.fields['signed_ball'].initial = self.instance.reward.signed_ball
            self.fields['shirt'].initial = self.instance.reward.shirt
            self.fields['signed_shirt'].initial = self.instance.reward.signed_shirt

            # Check if the kickoff pack fields exist before initializing them
            for field_name in ['kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']:
                if hasattr(self.instance.reward, field_name):
                    self.fields[field_name].initial = getattr(self.instance.reward, field_name)

    def save(self, commit=True):
        instance = super(DivisionRewardForm, self).save(commit=False)

        # Ensure reward object is created or updated
        if instance.reward is None:
            # Create a new reward if none exists
            instance.reward = Rewards.objects.create(
                name=f'Reward for {instance.week.name} - {instance.division.name}',
                credits=self.cleaned_data['credits'],
                game_token=self.cleaned_data['game_token'],
                lapt_token=self.cleaned_data['lapt_token'],
                event_tickets=self.cleaned_data['event_tickets'],
                ball=self.cleaned_data['ball'],
                signed_ball=self.cleaned_data['signed_ball'],
                shirt=self.cleaned_data['shirt'],
                signed_shirt=self.cleaned_data['signed_shirt'],
                kickoff_pack_1=self.cleaned_data.get('kickoff_pack_1'),
                kickoff_pack_2=self.cleaned_data.get('kickoff_pack_2'),
                kickoff_pack_3=self.cleaned_data.get('kickoff_pack_3'),
                season_pack_1=self.cleaned_data.get('season_pack_1'),
                season_pack_2=self.cleaned_data.get('season_pack_2'),
                season_pack_3=self.cleaned_data.get('season_pack')
            )
        else:
            # Update existing reward
            instance.reward.credits = self.cleaned_data['credits']
            instance.reward.game_token = self.cleaned_data['game_token']
            instance.reward.lapt_token = self.cleaned_data['lapt_token']
            instance.reward.event_tickets = self.cleaned_data['event_tickets']
            instance.reward.ball = self.cleaned_data['ball']
            instance.reward.signed_ball = self.cleaned_data['signed_ball']
            instance.reward.shirt = self.cleaned_data['shirt']
            instance.reward.signed_shirt = self.cleaned_data['signed_shirt']
            
            # Check if the kickoff pack fields exist before updating them
            for field_name in ['kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']:
                if field_name in self.cleaned_data:
                    setattr(instance.reward, field_name, self.cleaned_data.get(field_name))

            instance.reward.save()

        if commit:
            instance.save()

        return instance

class RewardsInline(admin.StackedInline):
    model = Rewards
    extra = 0  # No extra empty forms
    fields = (
        'name', 'credits', 'game_token', 'lapt_token', 
        'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3'
    )

class DivisionRewardInline(admin.TabularInline):
    model = DivisionReward
    extra = 1  # Number of empty forms to display
    form = DivisionRewardForm

    fields = (
        'division', 'min_position', 'max_position',
        'reward',  # Include the reward field
        'credits', 'game_token', 'lapt_token',
        'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3'
    )
    readonly_fields = []

    def credits(self, obj):
        return obj.reward.credits

    def game_token(self, obj):
        return obj.reward.game_token

    def lapt_token(self, obj):
        return obj.reward.lapt_token

    def event_tickets(self, obj):
        return obj.reward.event_tickets

    def ball(self, obj):
        return obj.reward.ball

    def signed_ball(self, obj):
        return obj.reward.signed_ball

    def shirt(self, obj):
        return obj.reward.shirt

    def signed_shirt(self, obj):
        return obj.reward.signed_shirt

@admin.register(DivisionReward)
class DivisionRewardAdmin(admin.ModelAdmin):
    form = DivisionRewardForm
    
    # Define the fields that will be displayed in the admin list view
    list_display = (
        'week', 'division', 'min_position', 'max_position',
        'credits', 'game_token', 'lapt_token',
        'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 
        'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3'
    )

    search_fields = ('week__name', 'division__name')
    list_filter = ('week', 'division')

    # Custom methods to display related rewards fields in the list
    def credits(self, obj):
        return obj.reward.credits if obj.reward else None
    credits.short_description = 'Credits'  # Optional, adds a better display label

    def game_token(self, obj):
        return obj.reward.game_token if obj.reward else None
    game_token.short_description = 'Game Token'

    def lapt_token(self, obj):
        return obj.reward.lapt_token if obj.reward else None
    lapt_token.short_description = 'Lapt Token'

    def event_tickets(self, obj):
        return obj.reward.event_tickets if obj.reward else None
    event_tickets.short_description = 'Event Tickets'

    def ball(self, obj):
        return obj.reward.ball if obj.reward else None
    ball.short_description = 'Ball'

    def signed_ball(self, obj):
        return obj.reward.signed_ball if obj.reward else None
    signed_ball.short_description = 'Signed Ball'

    def shirt(self, obj):
        return obj.reward.shirt if obj.reward else None
    shirt.short_description = 'Shirt'

    def signed_shirt(self, obj):
        return obj.reward.signed_shirt if obj.reward else None
    signed_shirt.short_description = 'Signed Shirt'

    def kickoff_pack_1(self, obj):
        return obj.reward.kickoff_pack_1 if obj.reward else None
    kickoff_pack_1.short_description = 'Kickoff Pack 1'

    def kickoff_pack_2(self, obj):
        return obj.reward.kickoff_pack_2 if obj.reward else None
    kickoff_pack_2.short_description = 'Kickoff Pack 2'

    def kickoff_pack_3(self, obj):
        return obj.reward.kickoff_pack_3 if obj.reward else None
    kickoff_pack_3.short_description = 'Kickoff Pack 3'
    
    def season_pack_1(self, obj):
        return obj.reward.season_pack_1 if obj.reward else None
    season_pack_1.short_description = 'Season Pack 1'
    
    def season_pack_2(self, obj):
        return obj.reward.season_pack_2 if obj.reward else None
    season_pack_2.short_description = 'Season Pack 2'
    
    def season_pack_3(self, obj):
        return obj.reward.season_pack_3 if obj.reward else None
    season_pack_3.short_description = 'Season Pack 3'

@admin.register(GameWeek)
class GameWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_at', 'end_at', 'scored_at', 'status')
    search_fields = ('id', 'name',)
    list_filter = ('status',)
    inlines = [DivisionRewardInline]

class UserModelChoiceField(forms.ModelChoiceField):
    def to_python(self, value):
        if not value:
            raise ValidationError("This field is required.")
        try:
            # Attempt to fetch by UUID
            return CustomUser.objects.get(pk=uuid.UUID(value))
        except (CustomUser.DoesNotExist, ValueError):
            # Fallback to fetching by username
            try:
                return CustomUser.objects.get(name=value)
            except CustomUser.DoesNotExist:
                raise ValidationError("User not found by username or ID.")

class AssignedCardPackForm(forms.ModelForm):
    user = UserModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.TextInput(attrs={'placeholder': 'Enter username or ID'}),
        label='User (by username or ID)',
        help_text="Enter the username or ID of the user."
    )
    card_pack_type = forms.ModelChoiceField(
        queryset=CardPackType.objects.all().order_by('name'),
        label="Card Pack Type"
    )
    store_transaction_id = forms.ModelChoiceField(
        queryset=StoreProductTransactions.objects.all().order_by('id'),
        required=False,
        label="Store Transaction ID",
        widget=forms.Select(attrs={'placeholder': 'Select store transaction ID'})
    )

    class Meta:
        model = AssignedCardPack
        fields = ['user', 'card_pack_type', 'opened', 'opened_at', 'revealed_at', 'revealed', 'store_transaction_id']

    def clean_user(self):
        user_input = self.cleaned_data['user']
        try:
            # Attempt to fetch by UUID
            return CustomUser.objects.get(id=user_input.id)
        except (CustomUser.DoesNotExist, ValueError):
            try:
                # Fallback to fetching by username
                return CustomUser.objects.get(name=user_input.name)
            except CustomUser.DoesNotExist:
                raise ValidationError("User not found by username or ID.")

@admin.register(AssignedCardPack)
class AssignedCardPackAdmin(admin.ModelAdmin):
    form = AssignedCardPackForm
    list_display = ('user', 'card_pack_type', 'opened', 'revealed')
    search_fields = ('user__name', 'card_pack_type__name')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('assign-card-pack/', self.admin_site.admin_view(self.assign_card_pack), name='assign-card-pack'),
        ]
        return custom_urls + urls

    def assign_card_pack(self, request):
        if request.method == 'POST':
            form = AssignedCardPackForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, "Assigned Card Pack created successfully.")
                    return redirect('..')
                except Exception as e:
                    messages.error(request, f"An error occurred: {str(e)}")
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = AssignedCardPackForm()

        context = {
            'form': form,
            'opts': self.model._meta,
            'title': 'Assign Card Pack to User',
        }
        return render(request, '../templates/assign_card_pack.html', context)

class RewardsAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the admin form
    list_display = ['name', 'credits', 'game_token', 'lapt_token', 'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']

    # Optional: Specify the fields in the form layout order
    fields = ['name', 'credits', 'game_token', 'lapt_token', 'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']

# Register the Rewards model with the custom admin
admin.site.register(Rewards, RewardsAdmin)

admin.site.register(DataFeedSimModel, DataFeedSimAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(CompetitionConfig, CompetitionConfigAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(CompetitionEdition, CompetitionEditingAdmin)
admin.site.register(CompetitionPhase, CompetitionPhaseAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(SoccerWikiPlayer, SoccerWikiPlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(PowerUp, PowerUpAdmin)
admin.site.register(Transactions, TransactionAdmin)
admin.site.register(MatchLeaderboard, MatchLeaderboardAdmin)
admin.site.register(ManualSubscription, ManualSubscriptionAdmin)
admin.site.register(StoreProduct, StoreProductAdmin)

```

## File: `core/apps.py`
- **File Size:** 83 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'

```

## File: `core/authentication.py`
- **File Size:** 863 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.db import IntegrityError
from firebase_admin import auth
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from core.models import CustomUser

class JWTAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, token):
        if token and token.startswith("debug:"):
            uid = token.replace("debug:", "")
        else:
            try:
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token['uid']
            except Exception:
                raise exceptions.AuthenticationFailed('Invalid token')

        try:
            user = CustomUser.objects.get(firebase_id=uid)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        return user, token

```

## File: `core/commands.py`
- **File Size:** 789 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1656 make new rewards

```
from django.conf import settings

from util import events

def update_played_time(match_id):
    events.create_amqp_event(
        settings.AMQP_SYSTEM_EXCHANGE,
        "update_played_time",
        {
            "match_id": match_id,
        }
    )

def validate_positions(positions):
    positions = sorted(positions, key=lambda x: x[0])
    last_max = None

    for i, (min_val, max_val) in enumerate(positions):
        if last_max is not None:
            if min_val > last_max + 1:
                return False
            if last_max is not None and min_val <= last_max:
                return False
        if max_val is None:
            # it should be last range
            if i != len(positions) - 1:
                return False
        last_max = max_val
    return True

```

## File: `core/const.py`
- **File Size:** 2835 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** added nft-category to action

```
POSITION_DEFENDER = 'd'
POSITION_MIDFIELDER = 'm'
POSITION_FORWARD = 'f'
POSITION_GOALKEEPER = 'g'
POSITION_SUBSTITUTE = 's'
POSITION_UNKNOWN = 'u'

# Goalkeeper | Wing Back | Defender | Defensive Midfielder | Attacking Midfielder | Midfielder | Striker | Substitute
POSITIONS = (
    (POSITION_DEFENDER, 'Wing Back'),
    (POSITION_DEFENDER, 'Defender'),
    (POSITION_MIDFIELDER, 'Defensive Midfielder'),
    (POSITION_MIDFIELDER, 'Midfielder'),
    (POSITION_MIDFIELDER, 'Attacking Midfielder'),
    (POSITION_FORWARD, 'Striker'),
    (POSITION_GOALKEEPER, 'Goalkeeper'),
    (POSITION_SUBSTITUTE, 'Substitute'),
    (POSITION_UNKNOWN, 'Unknown'),
)

MATCH_STATUS_EMPTY = ''
MATCH_STATUS_UNKNOWN = 'u'
MATCH_STATUS_WAITING = 'w'
MATCH_STATUS_LINEUPS = 'l'
MATCH_STATUS_GAME = 'g'
MATCH_STATUS_ENDED = 'e'
MATCH_STATUS_CANCELLED = 'c'

MATCH_STATUSES = (
    (MATCH_STATUS_EMPTY, 'Empty'),
    (MATCH_STATUS_UNKNOWN, 'Unknown'),
    (MATCH_STATUS_WAITING, 'Waiting'),
    (MATCH_STATUS_LINEUPS, 'Lineups'),
    (MATCH_STATUS_GAME, 'Game'),
    (MATCH_STATUS_ENDED, 'Ended'),
    (MATCH_STATUS_CANCELLED, 'Cancelled'),
)

MATCH_PERIOD_PREGAME = 'p'
MATCH_PERIOD_FIRST_HALF = 'f'
MATCH_PERIOD_HALF_TIME = 'h'
MATCH_PERIOD_SECOND_HALF = 's'
MATCH_PERIOD_BREAK_X1 = 'bx1'
MATCH_PERIOD_FIRST_EXT = 'x1'
MATCH_PERIOD_BREAK_X2 = 'bx2'
MATCH_PERIOD_SECOND_EXT = 'x2'
MATCH_PERIOD_BREAK_P = 'bp'
MATCH_PERIOD_PENALTIES = 'pe'
MATCH_PERIOD_POST_GAME = 'pg'

MATCH_PERIODS = (
    (MATCH_PERIOD_PREGAME, 'Pregame'),
    (MATCH_PERIOD_FIRST_HALF, 'First half'),
    (MATCH_PERIOD_HALF_TIME, 'Half time'),
    (MATCH_PERIOD_SECOND_HALF, 'Second half'),
    (MATCH_PERIOD_BREAK_X1, 'Break x1'),
    (MATCH_PERIOD_FIRST_EXT, 'First ext'),
    (MATCH_PERIOD_BREAK_X2, 'Break x2'),
    (MATCH_PERIOD_SECOND_EXT, 'Second ext'),
    (MATCH_PERIOD_BREAK_P, 'Break penalties'),
    (MATCH_PERIOD_PENALTIES, 'Penalties'),
    (MATCH_PERIOD_POST_GAME, 'Post game'),
)

DEFAULT_MATCH_RULES = {
    'num_of_picks': 4,
    'max_star_player_picks': 2,
}

TIER_NONE = 0
TIER_PREMIUM = 1
TIER_LITE = 2

TIER_CHOICES = (
    (TIER_NONE, 'None'),
    (TIER_PREMIUM, 'Premium'),
    (TIER_LITE, 'Lite'),
)

NFT_CATEGORY_DISTRIBUTION = 'distribution'
NFT_CATEGORY_SHOOTING = 'shooting'
NFT_CATEGORY_PASSING = 'passing'
NFT_CATEGORY_DRIBBLING = 'dribbling'
NFT_CATEGORY_DEFENCE = 'defence'
NFT_CATEGORY_DISCIPLINARY = 'disciplinary'
NFT_CATEGORY_STOPPING = 'stopping'
NFT_CATEGORY_CLAIMING = 'claiming'

NFT_CATEGORIES = (
    (NFT_CATEGORY_DISTRIBUTION, 'distribution'),
    (NFT_CATEGORY_SHOOTING, 'shooting'),
    (NFT_CATEGORY_PASSING, 'passing'),
    (NFT_CATEGORY_DRIBBLING, 'dribbling'),
    (NFT_CATEGORY_DEFENCE, 'defence'),
    (NFT_CATEGORY_DISCIPLINARY, 'disciplinary'),
    (NFT_CATEGORY_STOPPING, 'stopping'),
    (NFT_CATEGORY_CLAIMING, 'claiming'),
)

```

## File: `core/exceptions.py`
- **File Size:** 1844 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 add credits

```
from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    if isinstance(exc, serializers.ValidationError):
        return Response({
            'code': 99999,
            'message': 'Validation error',
            'detail': exc.detail,
        }, status=exc.status_code)

    if isinstance(exc, Http404):
        exc = ObjectNotFound()

    # custom exception
    if isinstance(exc, CustomException):
        return Response({
            'code': exc.code,
            'message': exc.message
        }, status=exc.status_code)

    # fallback to default handler
    return exception_handler(exc, context)

class CustomException(Exception):
    code = 99999
    status_code = 400
    message = 'Unknown error'

class ObjectNotFound(CustomException):
    message = 'Not found'

class CannotUploadAvatar(CustomException):
    message = 'Upload avatar error'

class MatchIsNotAvailable(CustomException):
    message = 'Match is not available'

class InvalidNumberOfPicks(CustomException):
    message = 'Invalid number of picks'

class PickAlreadyEnded(CustomException):
    message = 'Pick already ended'

class YouAlreadyPickedThisPlayer(CustomException):
    message = 'You already picked this player'

class InvalidPowerUpPosition(CustomException):
    message = 'Invalid power-up position'

class InvalidMatchStatusForPowerUp(CustomException):
    message = 'You can apply power-ups when match is active'

class AlreadyActivePowerUpForPosition(CustomException):
    message = 'You already have active power-up for this position'

class NotEnoughBalanceForWithdraw(CustomException):
    message = 'Sorry, you need a minimum balance of $20 to cashout. Win some more games!'

```

## File: `core/migrations/0001_initial.py`
- **File Size:** 15627 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixes for migrations from scratch to work

```
# Generated by Django 2.1.7 on 2019-03-09 17:34

from django.db import migrations, models
import django.db.models.deletion
import uuid

def create_third_party_extension(apps, schema_editor):
    schema_editor.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

def drop_third_party_extension(apps, schema_editor):
    schema_editor.execute("DROP EXTENSION IF EXISTS pg_trgm;")

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_third_party_extension, reverse_code=drop_third_party_extension, atomic=True),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'competitions',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
                ('iso', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('device_id', models.CharField(max_length=400, unique=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='w', max_length=1)),
                ('version', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='GamePick',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ended_at', models.DateTimeField(null=True)),
                ('position', models.IntegerField()),
                ('score', models.FloatField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='picks', to='core.Game')),
            ],
            options={
                'db_table': 'game_picks',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('match_time', models.DateTimeField()),
                ('last_processed_id', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'matches',
            },
        ),
        migrations.CreateModel(
            name='MatchEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField()),
                ('type', models.IntegerField()),
                ('points', models.FloatField(null=True)),
                ('payload', models.TextField(null=True)),
                ('minute', models.IntegerField()),
                ('second', models.IntegerField()),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
                ('match_event_id', models.IntegerField()),
                ('provider_id', models.CharField(max_length=30)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'match_events',
            },
        ),
        migrations.CreateModel(
            name='MatchEventProcessor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(1, 'scores')])),
                ('last_processed_id', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'match_event_processors',
            },
        ),
        migrations.CreateModel(
            name='OptaFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processing_started', models.DateTimeField(null=True)),
                ('processing_ended', models.DateTimeField(null=True)),
                ('feed_object_id', models.CharField(max_length=50, unique=True)),
                ('feed_hash', models.TextField(null=True)),
                ('feed_type', models.CharField(choices=[('F1', 'F1'), ('F24', 'F24'), ('F40', 'F40')], max_length=3)),
                ('status', models.IntegerField(choices=[(1, 'Received'), (2, 'Processing'), (3, 'Processed'), (4, 'Error')], default=1)),
                ('headers', models.TextField()),
            ],
            options={
                'db_table': 'opta_feeds',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('first_name', models.TextField(null=True)),
                ('last_name', models.TextField(null=True)),
                ('full_name', models.TextField(null=True)),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='SeasonCompetitionMember',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Competition')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season')),
            ],
            options={
                'db_table': 'season_competition_members',
            },
        ),
        migrations.CreateModel(
            name='SeasonTeamPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season')),
            ],
            options={
                'db_table': 'season_team_players',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Country')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Region')),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team')),
            ],
            options={
                'db_table': 'team_players',
            },
        ),
        migrations.AddField(
            model_name='seasonteamplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
        migrations.AddField(
            model_name='seasoncompetitionmember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
        migrations.AddField(
            model_name='matchevent',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player'),
        ),
        migrations.AddField(
            model_name='matchevent',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='away_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Competition'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='home_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season'),
        ),
        migrations.AddField(
            model_name='gamepick',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.AlterUniqueTogether(
            name='seasonteamplayer',
            unique_together={('player', 'team', 'season')},
        ),
        migrations.AlterIndexTogether(
            name='seasonteamplayer',
            index_together={('player', 'team', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='seasoncompetitionmember',
            unique_together={('competition', 'team', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='matcheventprocessor',
            unique_together={('match', 'type')},
        ),
        migrations.AlterUniqueTogether(
            name='matchevent',
            unique_together={('match', 'match_event_id')},
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('match', 'user')},
        ),
    ]

```

## File: `core/migrations/0002_auto_20190311_2023.py`
- **File Size:** 3308 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-11 20:23

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='home_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='away_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='match_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='f_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='f_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='s_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='s_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='x1_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='x1_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='x2_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='x2_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='p_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='p_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='version',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepick',
            name='version',
            field=models.IntegerField(default=0),
        ),

        # triggers to increase game version when pick is updated
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION pass_score_from_pick()
  RETURNS TRIGGER AS $$
BEGIN
  IF (TG_OP = 'UPDATE')
  THEN
    IF OLD.score != NEW.score THEN 
      update games g 
         set g.score = g.score + NEW.score,
             g.version = g.version + 1
       where g.id = NEW.game_id;
    END IF; 

    RETURN NEW;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION pass_score_from_pick();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_pass_score_from_pick
AFTER UPDATE ON game_picks
FOR EACH ROW EXECUTE PROCEDURE pass_score_from_pick();
            """,
            """DROP TRIGGER trg_pass_score_from_pick ON game_picks;"""
        ),
    ]

```

## File: `core/migrations/0003_auto_20190312_2155.py`
- **File Size:** 2804 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-12 21:55

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190311_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchEventSimulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('simulated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'match_event_simulations',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='simulation_from_match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='import_id',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='matcheventsimulation',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AddField(
            model_name='matcheventsimulation',
            name='match_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.MatchEvent'),
        ),
        migrations.AlterUniqueTogether(
            name='matcheventsimulation',
            unique_together={('match', 'match_event')},
        ),
    ]

```

## File: `core/migrations/0004_auto_20190313_1046.py`
- **File Size:** 3051 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-13 10:46

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190312_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'match_players',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='has_lineups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='period',
            field=models.CharField(choices=[('p', 'Pregame'), ('f', 'First half'), ('h', 'Half time'), ('s', 'Second half'), ('bx1', 'Break x1'), ('x1', 'First ext'), ('bx2', 'Break x2'), ('x2', 'Second ext'), ('bp', 'Break penalties'), ('pe', 'Penalties'), ('pg', 'Post game')], default='p', max_length=3),
        ),
        migrations.AddField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('u', 'Unknown'), ('w', 'Waiting'), ('l', 'Lineups'), ('g', 'Game'), ('e', 'Ended'), ('c', 'Cancelled')], default='w', max_length=1),
        ),
        migrations.AlterField(
            model_name='seasonteamplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='teamplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player'),
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
    ]

```

## File: `core/migrations/0005_optafeed_match.py`
- **File Size:** 477 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-13 11:22

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190313_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='optafeed',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
    ]

```

## File: `core/migrations/0006_gameevent.py`
- **File Size:** 2428 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-13 18:45

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_optafeed_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('minute', models.IntegerField()),
                ('second', models.IntegerField()),
                ('type', models.IntegerField()),
                ('score', models.FloatField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Game')),
                ('game_pick', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.GamePick')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team')),
            ],
            options={
                'db_table': 'game_events',
            },
        ),
        # triggers to increase game version when pick is updated
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION pass_score_from_game_event()
  RETURNS TRIGGER AS $$
BEGIN 
    update game_picks
       set score = score + NEW.score,
           version = version + 1
     where id = NEW.game_pick_id;
     
    update games
       set score = score + NEW.score,
           version = version + 1
     where id = NEW.game_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION pass_score_from_game_event();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_pass_score_from_game_event
AFTER INSERT ON game_events
FOR EACH ROW EXECUTE PROCEDURE pass_score_from_game_event();
            """,
            """DROP TRIGGER trg_pass_score_from_game_event ON game_events;"""
        ),
        migrations.RunSQL(
            """DROP TRIGGER if exists trg_pass_score_from_pick ON game_picks;""",
            """"""
        ),
        migrations.RunSQL(
            """DROP FUNCTION if exists pass_score_from_pick();""",
            """"""
        ),
    ]

```

## File: `core/migrations/0007_auto_20190314_1821.py`
- **File Size:** 413 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-14 18:21

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_gameevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matcheventprocessor',
            name='type',
            field=models.IntegerField(choices=[(1, 'points'), (2, 'system')]),
        ),
    ]

```

## File: `core/migrations/0008_teamplayer_is_star.py`
- **File Size:** 389 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-19 11:37

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190314_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamplayer',
            name='is_star',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0009_auto_20190320_1905.py`
- **File Size:** 2612 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-20 19:05

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_teamplayer_is_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('score', models.FloatField()),
                ('ordering', models.IntegerField()),
            ],
            options={
                'db_table': 'actions',
            },
        ),
        migrations.CreateModel(
            name='PowerUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('duration', models.IntegerField(help_text='duration in minutes')),
                ('multiplier', models.FloatField()),
            ],
            options={
                'db_table': 'powerups',
            },
        ),
        migrations.CreateModel(
            name='PowerUpAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Action')),
                ('power_up', models.ForeignKey(db_column='powerup_id', on_delete=django.db.models.deletion.DO_NOTHING, to='core.PowerUp')),
            ],
            options={
                'db_table': 'powerup_actions',
            },
        ),
        migrations.AlterField(
            model_name='team',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Country'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Region'),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.TextField(blank=True),
        ),
    ]

```

## File: `core/migrations/0010_actions_powerup_seed.py`
- **File Size:** 4346 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-20 18:57

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190320_1905'),
    ]

    operations = [

        # insert actions
        migrations.RunSQL(
            '''INSERT INTO actions(id,description,name,score,ordering) values
(70, 'Last Line Save', 'Save off line', 10, 100),
(71, 'Last Man Tackle', 'Last Man Tackle', 10, 200),
(36, 'Defensive Block', 'Defensive Block', 8, 300),
(32, 'Tackle - Won', 'Tackle + Ball', 6, 400),
(31, 'Interception', 'Intercepts Ball', 5, 500),
(33, 'Tackle - Won (without Possession)', 'Tackle', 5, 600),
(38, 'Effective Clearance', 'Clears Ball', 3, 700),
(18, 'Aerial Duel - Won', 'Header Won', 2, 800),
(19, 'Aerial Duel - Lost', 'Header Lost', -2, 900),
(26, 'Foul - Conceded', 'Foul Conceded', -2, 1000),
(57, 'Penalty Conceded', 'Penalty Fault', -12, 1100),
(49, 'Own Goal', 'Own Goal', -15, 1200),
(27, 'Handball Conceded', 'Handball', -3, 1300),
(58, 'Yellow Card', 'Yellow Card', -8, 1400),
(59, '2nd Yellow Card', '2nd Yellow Card', -8, 1500),
(60, 'Red Card', 'Red Card', -18, 1600),
(69, 'Won Corner', 'Won Corner', 4, 1700),
(73, 'Penalty Won', 'Pen Won', 20, 1800),
(61, 'Great Skill', 'Great Skill', 8, 1900),
(55, 'Successful Take On (dribble)', 'Dribble Success', 6, 2000),
(25, 'Foul - Won', 'Foul Won', 2, 2100),
(67, 'Dispossessed', 'Loses Ball', -2, 2200),
(56, 'Unsuccessful dribble', 'Dribble Fail', -2, 2300),
(62, 'Big Error - lead to shot', 'Bad Mistake', -8, 2400),
(80, 'Goalkeeper Save', 'Save', 12, 2500),
(37, 'Goalkeeper Claim', 'Cross Caught', 6, 2600),
(75, 'Goalkeeper Punch', 'Punch Clear', 5, 2700),
(77, 'Keeper pick-up', 'Pick-up', 2, 2800),
(87, 'Goal Kick  Successful', 'Goal Kick', 2, 2900),
(85, 'Goalkeeper Throw - Successful', 'Keeper Throw', 2, 3000),
(88, 'Goal Kick Unsuccessful', 'Goal Kick Miss', -1, 3100),
(79, 'Cross not claimed', 'Cross Dropped', -4, 3200),
(7, 'Assist', 'Assist', 25, 3300),
(8, 'Key Pass', 'Key Pass', 5, 3400),
(68, 'Through Ball', 'Through Ball', 5, 3500),
(5, 'Successful Cross - Bonus', 'Crosses Ball', 5, 3600),
(29, 'Corners Into box - Successful', 'Corner Success', 4, 3700),
(2, 'Pass - Successful', 'Pass', 1, 3800),
(3, 'Pass - Unsuccessful', 'Pass Miss', -2, 3900),
(6, 'Unsuccessful Crosses Total (excl corners & freekicks)', 'Cross Miss', -2, 4000),
(86, 'Goalkeeper Throw - Unsuccessful', 'Throw Miss', -2, 4100),
(64, 'Big Error - lead to goal', 'Big Mistake', -12, 4200),
(45, 'Goal', 'GOAL!!', 50, 4300),
(63, 'Shot hit the Post', 'Shot Hit Post', 16, 4400),
(43, 'Shot on Target', 'Shot On Goal', 12, 4500),
(53, 'Shot Blocked', 'Shot Blocked', 8, 4600),
(44, 'Shot off Target', 'Shot Off Goal', 5, 4700),
(65, 'Caught Offside', 'Offside', -3, 4800),
(72, 'Big Chance Missed', 'Big Miss!', -12, 4900),
(74, 'Penalty Missed', 'Pen Miss', -14, 5000);''',
            '''DELETE FROM actions;'''),

        # insert powerups
        migrations.RunSQL(
            '''INSERT INTO powerups(id,name,duration,multiplier) values
(1, 'Golden Gloves', 600, 2),
(2, 'Defensive Rock', 600, 2),
(3, 'Anchorman', 600, 2),
(4, 'Playmaker', 600, 2),
(5, 'Sharp Shooter', 600, 2),
(6, 'Wing Wizard', 600, 2);''',
            '''DELETE FROM powerups;'''),

        # insert powerup actions
        migrations.RunSQL(
            '''INSERT INTO powerup_actions(powerup_id, action_id, ordering) values
(1, 80, 10),
(1, 37, 20),
(1, 75, 30),
(1, 2, 40),
(1, 88, 50),
(1, 3, 60),
(1, 58, 70),

(2, 70, 10),
(2, 36, 20),
(2, 32, 30),
(2, 31, 40),
(2, 33, 50),
(2, 38, 60),
(2, 18, 70),
(2, 19, 80),
(2, 64, 90),
(2, 62, 100),
(2, 26, 110),
(2, 57, 120),
(2, 49, 130),
(2, 58, 140),

(3, 2, 10),
(3, 32, 20),
(3, 38, 30),
(3, 33, 40),
(3, 18, 50),
(3, 19, 60),
(3, 3, 70),
(3, 26, 80),
(3, 64, 90),
(3, 62, 100),
(3, 58, 110),

(4, 45, 10),
(4, 2, 20),
(4, 8, 30),
(4, 68, 40),
(4, 5, 50),
(4, 29, 60),
(4, 7, 70),
(4, 3, 80),
(4, 6, 90),
(4, 65, 100),
(4, 58, 110),

(5, 45, 10),
(5, 63, 20),
(5, 43, 30),
(5, 53, 40),
(5, 44, 50),
(5, 67, 60),
(5, 65, 70),
(5, 72, 80),
(5, 74, 90),
(5, 58, 100),
(5, 27, 110),

(6, 45, 10),
(6, 69, 20),
(6, 73, 30),
(6, 55, 40),
(6, 25, 50),
(6, 7, 60),
(6, 8, 70),
(6, 67, 80),
(6, 56, 90),
(6, 72, 100),
(6, 74, 110);''',
            '''DELETE FROM powerup_actions;'''
        ),
    ]

```

## File: `core/migrations/0011_auto_20190320_1948.py`
- **File Size:** 712 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-20 19:48

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_actions_powerup_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerup',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='powerup',
            name='icon_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='powerup',
            name='duration',
            field=models.IntegerField(help_text='duration in seconds'),
        ),
    ]

```

## File: `core/migrations/0012_auto_20190320_2017.py`
- **File Size:** 1531 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-20 20:17

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190320_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePowerUp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ended_at', models.DateTimeField(null=True)),
                ('position', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('multiplier', models.FloatField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Game')),
                ('powerup', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.PowerUp')),
            ],
            options={
                'db_table': 'game_powerups',
            },
        ),
        migrations.RenameField(
            model_name='powerupaction',
            old_name='power_up',
            new_name='powerup',
        ),
        migrations.AlterField(
            model_name='powerupaction',
            name='powerup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.PowerUp'),
        ),
    ]

```

## File: `core/migrations/0013_auto_20190320_2137.py`
- **File Size:** 644 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-20 21:37

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190320_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameevent',
            name='initial_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='gameevent',
            name='powerup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.GamePowerUp'),
        ),
    ]

```

## File: `core/migrations/0014_player_avg_score.py`
- **File Size:** 381 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-21 21:49

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190320_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='avg_score',
            field=models.FloatField(null=True),
        ),
    ]

```

## File: `core/migrations/0015_auto_20190321_2233.py`
- **File Size:** 926 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-21 22:33

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_player_avg_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='facebook_id',
        ),
        migrations.AddField(
            model_name='customuser',
            name='firebase_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0016_matchleaderboard.py`
- **File Size:** 2884 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-25 18:04

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190321_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchLeaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(null=True)),
                ('position', models.IntegerField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Game')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser')),
            ],
            options={
                'db_table': 'match_leaderboard',
            },
        ),
        migrations.RunSQL(
            """
create or replace function update_match_leaderboard(p_match_id uuid)
  returns void as $$
begin
  update match_leaderboard
     set score = t.score,
         position = t.position
    from (select g.id game_id,
                 g.score,
                 rank() over(order by g.score desc) as position
            from games g
           where g.match_id = p_match_id
         ) t
   where match_leaderboard.game_id = t.game_id;
end;
$$ language plpgsql;
            """,
            """DROP FUNCTION update_match_leaderboard(p_match_id uuid);"""
        ),

        # trigger to insert match_leaderboard record on game insert
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION insert_match_leaderboard_record()
  RETURNS TRIGGER AS $$
BEGIN 
    insert into match_leaderboard(match_id, game_id, user_id, score, position)
    values (NEW.match_id, NEW.id, NEW.user_id, null, null);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION insert_match_leaderboard_record();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_insert_match_leaderboard_record
AFTER INSERT ON games
FOR EACH ROW EXECUTE PROCEDURE insert_match_leaderboard_record();
            """,
            """DROP TRIGGER trg_insert_match_leaderboard_record ON games;"""
        ),

        # insert match_leaderboard for each match
        migrations.RunSQL(
            """
insert into match_leaderboard(match_id, user_id, game_id)
select match_id,
       user_id,
       id
  from games
""", """"""
        ),

        # update match_leaderboard for each match
        migrations.RunSQL(
            """
select t.match_id,
       update_match_leaderboard(t.match_id)
  from (select distinct match_id from games) t
            """,
            """"""
        )
    ]

```

## File: `core/migrations/0017_customuser_avatar_url.py`
- **File Size:** 395 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-26 18:22

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_matchleaderboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0018_auto_20190326_2221.py`
- **File Size:** 3256 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-26 22:21

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_customuser_avatar_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchReward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
            options={
                'db_table': 'match_rewards',
            },
        ),
        migrations.AlterField(
            model_name='match',
            name='f_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='f_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='last_processed_id',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='p_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='p_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='s_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='s_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='simulation_from_match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='x1_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='x1_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='x2_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='x2_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AlterUniqueTogether(
            name='matchreward',
            unique_together={('match', 'position')},
        ),
    ]

```

## File: `core/migrations/0019_auto_20190326_2252.py`
- **File Size:** 981 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-26 22:52

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20190326_2221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'Matches'},
        ),
        migrations.AddField(
            model_name='match',
            name='match_type',
            field=models.IntegerField(choices=[(0, 'Unknown'), (1, 'Free'), (2, 'Cash'), (3, 'Cash Plus')], db_index=True, default=0),
        ),
        migrations.RunSQL(
            '''
insert into match_rewards(match_id, position, amount)
select * 
  from (
select id, 1, 100 from matches
union all
select id, 2, 50 from matches
union all
select id, 3, 25 from matches
union all
select id, 4, 15 from matches
union all
select id, 5, 10 from matches
) t
            ''',
            '''delete from match_rewards'''
        )
    ]

```

## File: `core/migrations/0020_auto_20190328_2218.py`
- **File Size:** 498 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-28 22:18

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190326_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayer',
            name='is_star',
        ),
        migrations.AddField(
            model_name='matchplayer',
            name='is_star',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0021_matchplayer_from_lineups.py`
- **File Size:** 395 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-29 09:30

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20190328_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='from_lineups',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0022_matchplayer_score.py`
- **File Size:** 388 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-30 15:34

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_matchplayer_from_lineups'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]

```

## File: `core/migrations/0023_auto_20190330_1732.py`
- **File Size:** 1141 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-30 17:32

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_matchplayer_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepick',
            name='minute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepick',
            name='second',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepowerup',
            name='minute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepowerup',
            name='second',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='minute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='second',
            field=models.IntegerField(default=0),
        ),
    ]

```

## File: `core/migrations/0024_matchheadline.py`
- **File Size:** 1033 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-30 19:59

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190330_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchHeadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('images', models.TextField()),
                ('type', models.CharField(max_length=15)),
                ('screen_type', models.IntegerField(choices=[(1, 'lobby'), (2, 'gameplay'), (3, 'fulltime')])),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'match_headlines',
            },
        ),
    ]

```

## File: `core/migrations/0025_auto_20190330_2138.py`
- **File Size:** 2256 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-03-30 21:38

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_matchheadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField()),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='paypal_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='withdraw_processing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION update_user_balance()
  RETURNS TRIGGER AS $$
DECLARE
    v_rec record;
BEGIN 
    select *
      into v_rec
      from users
     where id = NEW.user_id
       for update;

    update users
       set balance = balance + NEW.amount
     where id = NEW.user_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION update_user_balance();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_update_user_balance
AFTER INSERT ON transactions
FOR EACH ROW EXECUTE PROCEDURE update_user_balance();
            """,
            """DROP TRIGGER trg_update_user_balance ON transactions;"""
        ),
    ]

```

## File: `core/migrations/0026_auto_20190403_0934.py`
- **File Size:** 530 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-03 09:34

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20190330_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='crest_url',
            field=models.TextField(blank=True),
        ),
    ]

```

## File: `core/migrations/0027_auto_20190404_0924.py`
- **File Size:** 783 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-04 09:24

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190403_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='crest_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RunSQL('''
update teams
   set short_name = null
 where short_name = ''
        ''', ''''''),
        migrations.RunSQL('''
update teams
   set crest_url = null
 where crest_url = ''
            ''', ''''''),
    ]

```

## File: `core/migrations/0028_player_image_url.py`
- **File Size:** 380 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-04 12:57

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20190404_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image_url',
            field=models.TextField(null=True),
        ),
    ]

```

## File: `core/migrations/0029_competition_short_name.py`
- **File Size:** 396 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-04 13:13

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_player_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='short_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0030_auto_20190405_2134.py`
- **File Size:** 660 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-05 21:34

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0029_competition_short_name'),
    ]

    operations = [
        migrations.RunSQL(
            '''create unique index idx_game_picks_position_uk on game_picks(game_id, position) where ended_at is null;''',
            '''drop index idx_game_picks_position_uk;''',
        ),
        migrations.RunSQL(
            '''create unique index idx_game_picks_player_uk on game_picks(game_id, player_id) where ended_at is null;''',
            '''drop index idx_game_picks_player_uk;''',
        ),
    ]

```

## File: `core/migrations/0031_auto_20190409_1729.py`
- **File Size:** 835 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-09 17:29

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20190405_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='rewarded',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='transactions',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AlterField(
            model_name='teamplayer',
            name='jersey_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0032_auto_20190416_2031.py`
- **File Size:** 1251 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-16 20:31

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20190409_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('r', 'Requested'), ('p', 'Processing'), ('c', 'Completed'), ('d', 'Cancelled')], max_length=1)),
                ('amount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='withdraw_processing',
        ),
        migrations.AddField(
            model_name='withdrawrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
    ]

```

## File: `core/migrations/0033_auto_20190419_1451.py`
- **File Size:** 2735 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-19 14:51

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20190416_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptaFeedItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unique_id', models.BigIntegerField()),
                ('event_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'opta_feed_items',
            },
        ),
        migrations.CreateModel(
            name='OptaFeedItemVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'No Diff'), (3, 'Partial Cancel'), (4, 'Full Cancel')])),
                ('version', models.BigIntegerField()),
                ('last_modified_at', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.OptaFeedItem')),
            ],
            options={
                'db_table': 'opta_feed_item_versions',
            },
        ),
        migrations.AddField(
            model_name='gameevent',
            name='match_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.MatchEvent'),
        ),
        migrations.AddField(
            model_name='optafeeditem',
            name='current_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.OptaFeedItemVersion'),
        ),
        migrations.AddField(
            model_name='optafeeditem',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AddField(
            model_name='matchevent',
            name='opta_feed_item_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.OptaFeedItemVersion'),
        ),
        migrations.AlterUniqueTogether(
            name='optafeeditem',
            unique_together={('unique_id', 'event_id')},
        ),
    ]

```

## File: `core/migrations/0034_matchevent_status.py`
- **File Size:** 443 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-19 16:07

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20190419_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchevent',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Cancelled'), (3, 'Ignored')], default=1),
        ),
    ]

```

## File: `core/migrations/0035_auto_20190420_0933.py`
- **File Size:** 1456 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-20 09:33

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_matchevent_status'),
    ]

    operations = [
        migrations.RunSQL(
            '''create index idx_opta_feed_unprocessed on opta_feeds(id) where status = 1;''',
            '''drop index idx_opta_feed_unprocessed;'''
        ),
        migrations.RunSQL(
            """
create or replace function update_match_leaderboard(p_match_id uuid)
  returns void as $$
begin
  update match_leaderboard
     set score = t.score,
         position = t.position
    from (select g.id game_id,
                 g.score,
                 rank() over(order by g.score desc) as position
            from games g
           where g.match_id = p_match_id
         ) t
   where match_leaderboard.game_id = t.game_id
     and match_leaderboard.match_id = p_match_id;
end;
$$ language plpgsql;
            """,
            """
create or replace function update_match_leaderboard(p_match_id uuid)
  returns void as $$
begin
  update match_leaderboard
     set score = t.score,
         position = t.position
    from (select g.id game_id,
                 g.score,
                 rank() over(order by g.score desc) as position
            from games g
           where g.match_id = p_match_id
         ) t
   where match_leaderboard.game_id = t.game_id;
end;
$$ language plpgsql;"""
        ),
    ]

```

## File: `core/migrations/0036_auto_20190420_0946.py`
- **File Size:** 362 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-20 09:46

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20190420_0933'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='matchplayer',
            index_together={('match', 'player', 'team')},
        ),
    ]

```

## File: `core/migrations/0037_auto_20190423_1822.py`
- **File Size:** 344 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-23 18:22

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20190420_0946'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='withdrawrequest',
            table='withdraw_requests',
        ),
    ]

```

## File: `core/migrations/0038_auto_20190423_1843.py`
- **File Size:** 508 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-23 18:43

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20190423_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayer',
            name='player',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='team',
        ),
        migrations.DeleteModel(
            name='TeamPlayer',
        ),
    ]

```

## File: `core/migrations/0039_team_abbr.py`
- **File Size:** 399 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-23 19:16

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20190423_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='abbr',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]

```

## File: `core/migrations/0040_auto_20190423_1935.py`
- **File Size:** 377 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixes for migrations from scratch to work

```
# Generated by Django 2.1.7 on 2019-04-23 19:35

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0039_team_abbr'),
    ]

    operations = [
        migrations.RunSQL(
            '''create sequence if not exists user_guest_index;''',
            '''drop sequence if exists user_guest_index;''',
        )
    ]

```

## File: `core/migrations/0041_matchplayer_played_seconds.py`
- **File Size:** 393 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-25 18:19

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20190423_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='played_seconds',
            field=models.IntegerField(null=True),
        ),
    ]

```

## File: `core/migrations/0042_matchheadline_image_type.py`
- **File Size:** 411 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-05-03 14:49

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_matchplayer_played_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchheadline',
            name='image_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

```

## File: `core/migrations/0043_gamepick_user_swapped.py`
- **File Size:** 397 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-05-06 17:58

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_matchheadline_image_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepick',
            name='user_swapped',
            field=models.BooleanField(default=True),
        ),
    ]

```

## File: `core/migrations/0044_matchnotification.py`
- **File Size:** 898 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-05-20 21:11

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_gamepick_user_swapped'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchNotification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'match_notifications',
            },
        ),
    ]

```

## File: `core/migrations/0045_matchnotification_user.py`
- **File Size:** 489 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-05-21 20:18

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_matchnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchnotification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
    ]

```

## File: `core/migrations/0046_matchplayer_avg_score.py`
- **File Size:** 585 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-05-28 21:06

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_matchnotification_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='avg_score',
            field=models.FloatField(null=True),
        ),
        migrations.RunSQL(
            '''update match_players mp
                  set avg_score=(select p.avg_score from players p where p.id = mp.player_id);''',
            '''''',
        )
    ]

```

## File: `core/migrations/0047_auto_20190530_1246.py`
- **File Size:** 422 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-05-30 12:46

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_matchplayer_avg_score'),
    ]

    operations = [
        migrations.RunSQL(
            '''create index idx_matches_time_and_type on matches(match_time) where match_type != 0;''',
            '''drop index idx_matches_time_and_type;'''
        )
    ]

```

## File: `core/migrations/0048_customuser_verified.py`
- **File Size:** 390 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-06-05 10:11

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20190530_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0049_auto_20190620_1642.py`
- **File Size:** 1006 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-06-20 16:42

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_customuser_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bonus_powerups',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='referral_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='referrer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.AddField(
            model_name='gamepowerup',
            name='bonus',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0050_auto_20190627_1132.py`
- **File Size:** 677 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-06-27 11:32

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20190620_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bonus_powerups',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='referrer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
    ]

```

## File: `core/migrations/0051_auto_20200524_2026.py`
- **File Size:** 2407 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-05-24 20:26

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20190627_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionEdition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, null=True, unique=True)),
                ('name', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'competition_editions',
            },
        ),
        migrations.CreateModel(
            name='CompetitionPhase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, null=True, unique=True)),
                ('name', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
                ('competition_edition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CompetitionEdition')),
            ],
            options={
                'db_table': 'competition_phases',
            },
        ),
        migrations.AddField(
            model_name='competition',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('', 'Empty'), ('u', 'Unknown'), ('w', 'Waiting'), ('l', 'Lineups'), ('g', 'Game'), ('e', 'Ended'), ('c', 'Cancelled')], default='w', max_length=1),
        ),
        migrations.AddField(
            model_name='competitionedition',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Competition'),
        ),
    ]

```

## File: `core/migrations/0052_team_ortec_selection_id.py`
- **File Size:** 414 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-05-26 21:59

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20200524_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='ortec_selection_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

```

## File: `core/migrations/0053_auto_20200610_0052.py`
- **File Size:** 377 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-06-10 00:52

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_team_ortec_selection_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='optafeeditem',
            unique_together={('match', 'unique_id', 'event_id')},
        ),
    ]

```

## File: `core/migrations/0054_match_last_synced_at.py`
- **File Size:** 400 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-06-13 19:52

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20200610_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='last_synced_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0055_auto_20201025_2202.py`
- **File Size:** 390 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-10-25 22:02

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_match_last_synced_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchheadline',
            name='type',
            field=models.CharField(max_length=30),
        ),
    ]

```

## File: `core/migrations/0056_auto_20201128_1415.py`
- **File Size:** 480 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-11-28 14:15

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20201025_2202'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchplayer',
            unique_together={('match', 'player', 'team')},
        ),
        migrations.AlterIndexTogether(
            name='matchplayer',
            index_together=set(),
        ),
    ]

```

## File: `core/migrations/0057_auto_20201129_1959.py`
- **File Size:** 397 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-11-29 19:59

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20201128_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optafeeditemversion',
            name='version',
            field=models.CharField(max_length=64),
        ),
    ]

```

## File: `core/migrations/0058_auto_20201204_1637.py`
- **File Size:** 708 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-04 16:37

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20201129_1959'),
    ]

    operations = [
        # insert powerups
        migrations.RunSQL(
            '''INSERT INTO powerups(id,name,duration,multiplier) values
(7, 'Double Points', 600, 2);''',
            '''DELETE FROM powerups;'''),

        # insert powerup actions
        migrations.RunSQL(
            '''INSERT INTO powerup_actions(powerup_id, action_id, ordering)
(select 7,
        id,
        (row_number() over(order by id))*10
   from actions
);''',
            '''DELETE FROM powerup_actions;'''
        ),
    ]

```

## File: `core/migrations/0059_player_nick_name.py`
- **File Size:** 380 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-11 23:40

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_auto_20201204_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nick_name',
            field=models.TextField(null=True),
        ),
    ]

```

## File: `core/migrations/0060_auto_20201217_2051.py`
- **File Size:** 338 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-17 20:51

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_player_nick_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchplayer',
            unique_together=set(),
        ),
    ]

```

## File: `core/migrations/0061_auto_20201217_2051.py`
- **File Size:** 364 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-17 20:51

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_auto_20201217_2051'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchplayer',
            unique_together={('match', 'player', 'team')},
        ),
    ]

```

## File: `core/migrations/0062_auto_20201218_2045.py`
- **File Size:** 356 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-18 20:45

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20201217_2051'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchplayer',
            unique_together={('match', 'player')},
        ),
    ]

```

## File: `core/migrations/0063_player_soccer_wiki_player.py`
- **File Size:** 570 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-18 21:30

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('soccer_wiki', '0002_auto_20190404_1225'),
        ('core', '0062_auto_20201218_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='soccer_wiki_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='soccer_wiki.SoccerWikiPlayer'),
        ),
    ]

```

## File: `core/migrations/0064_auto_20201218_2200.py`
- **File Size:** 1388 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-18 22:00

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_player_soccer_wiki_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avg_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='full_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='nick_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0065_auto_20201218_2329.py`
- **File Size:** 487 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-18 23:29

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0064_auto_20201218_2200'),
    ]

    operations = [
        migrations.RunSQL(
            """CREATE INDEX IF NOT EXISTS soccer_wiki_player_gin_idx 
                ON soccer_wiki_players USING gin ((first_name||' '||second_name) gin_trgm_ops);""",
            """DROP INDEX soccer_wiki_player_gin_idx;""",
        ),
    ]

```

## File: `core/migrations/0066_matchevent_period.py`
- **File Size:** 410 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-25 12:11

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20201218_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchevent',
            name='period',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]

```

## File: `core/migrations/0067_auto_20201226_1526.py`
- **File Size:** 1133 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2020-12-26 15:26

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_matchevent_period'),
    ]

    operations = [
        # triggers to increase game version when pick is updated
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION decrease_score_on_game_event_deletion()
  RETURNS TRIGGER AS $$
BEGIN 
    update game_picks
       set score = score - OLD.score,
           version = version + 1
     where id = OLD.game_pick_id;

    update games
       set score = score - OLD.score,
           version = version + 1
     where id = OLD.game_id;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION decrease_score_on_game_event_deletion();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_decrease_score_on_game_event_deletion
AFTER DELETE ON game_events
FOR EACH ROW EXECUTE PROCEDURE decrease_score_on_game_event_deletion();
            """,
            """DROP TRIGGER trg_decrease_score_on_game_event_deletion ON game_events;"""
        ),
    ]

```

## File: `core/migrations/0068_auto_20210112_2332.py`
- **File Size:** 1408 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2021-01-12 23:32

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20201226_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepick',
            name='ended_minute',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gamepick',
            name='ended_second',
            field=models.IntegerField(null=True),
        ),
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION set_ended_minute_and_second()
  RETURNS TRIGGER AS $$
BEGIN 
    if OLD.ended_at is null and NEW.ended_at is not null then
      select matches.minute,
             matches.second
        into new.ended_minute,
             new.ended_second
        from matches,
             games
       where games.id = NEW.game_id
         and games.match_id = matches.id;
    end if;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION set_ended_minute_and_second();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_set_ended_minute_and_second
BEFORE UPDATE ON game_picks
FOR EACH ROW EXECUTE PROCEDURE set_ended_minute_and_second();
            """,
            """DROP TRIGGER trg_set_ended_minute_and_second ON game_picks;"""
        ),
    ]

```

## File: `core/migrations/0069_auto_20210130_0033.py`
- **File Size:** 2416 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-01-30 00:33

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20210112_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avg_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='avg_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='follower_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='games_played',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='followers', to='core.CustomUser')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='followings', to='core.CustomUser')),
            ],
            options={
                'db_table': 'followers',
                'unique_together': {('from_user', 'to_user')},
            },
        ),
        migrations.RunSQL("""
        update users
           set avg_rank = t.avg_rank,
               avg_points = t.avg_points,
               games_played = t.games_played
          from (
          select games.user_id,
                 round(avg(match_leaderboard.position)) avg_rank,
                 round(avg(match_leaderboard.score)) avg_points,
                 count(1) games_played
            from match_leaderboard,
                 games
           where match_leaderboard.game_id = games.id
           group by games.user_id
          ) t
         where users.id = t.user_id; 
        """,
                          """""")
    ]

```

## File: `core/migrations/0070_customuser_name_changed.py`
- **File Size:** 547 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-01-30 00:58

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20210130_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name_changed',
            field=models.BooleanField(default=False),
        ),
        migrations.RunSQL("""
        update users
           set name_changed = true
         where users.name not like 'Guest#%'
           """, """""")
    ]

```

## File: `core/migrations/0071_auto_20210221_1246.py`
- **File Size:** 429 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-02-21 12:46

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_customuser_name_changed'),
    ]

    operations = [
        migrations.RunSQL('''create extension if not exists pg_trgm;''', ''''''),
        migrations.RunSQL('''
        CREATE INDEX idx_users_name ON users USING gist (name gist_trgm_ops);
        '''),
    ]

```

## File: `core/migrations/0072_auto_20210322_1555.py`
- **File Size:** 795 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-03-22 15:55

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20210221_1246'),
    ]

    operations = [
        migrations.RunSQL(
            """
update users
   set name = t.name
from (select id,
             name || num as name
      from (select id,
                   name,
                   row_number() over (partition by name order by created_at) num
            from users
            order by name, num) t
      where num > 1
     ) t
where users.id = t.id""",
            """"""
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

```

## File: `core/migrations/0073_banpenalty.py`
- **File Size:** 1019 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-03-24 20:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20210322_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='BanPenalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, help_text='Empty end time means permanent ban', null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='penalties', to='core.CustomUser')),
            ],
            options={
                'db_table': 'ban_penalties',
            },
        ),
    ]

```

## File: `core/migrations/0074_customuser_moderator.py`
- **File Size:** 381 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-03-24 20:38

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_banpenalty'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='moderator',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0075_auto_20210428_1357.py`
- **File Size:** 505 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-04-28 13:57

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_customuser_moderator'),
    ]

    operations = [
        migrations.RunSQL(
            """update users set name = replace(name, ' ', '_');""",
            """"""
        ),
        migrations.RunSQL(
            """create index users_name_unique on users(lower(name));""",
            """drop index users_name_unique;"""
        )
    ]

```

## File: `core/migrations/0076_matchevent_has_real_timestamp.py`
- **File Size:** 398 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-04-28 14:46

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_auto_20210428_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchevent',
            name='has_real_timestamp',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0077_customuser_premium.py`
- **File Size:** 398 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-05-12 18:14

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_matchevent_has_real_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0078_subscription_subscriptionhistory_subscriptionrequest.py`
- **File Size:** 2945 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-05-22 14:35

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_customuser_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(unique=True)),
                ('last_billing_update', models.DateTimeField()),
                ('raw_data', models.TextField()),
                ('expiration_time', models.DateTimeField()),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'subscriptions',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('last_billing_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'subscription_requests',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_billing_update', models.DateTimeField()),
                ('raw_data', models.TextField()),
                ('expiration_time', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Subscription')),
            ],
            options={
                'db_table': 'subscription_history',
            },
        ),
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION insert_subscription_history()
  RETURNS TRIGGER AS $$
DECLARE
BEGIN 
    insert into subscription_history(
        created_at,
        subscription_id,
        last_billing_update,
        raw_data,
        expiration_time,
        active
    ) values (
        current_timestamp,
        NEW.id,
        OLD.last_billing_update,
        OLD.raw_data,
        OLD.expiration_time,
        OLD.active
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION insert_subscription_history();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_insert_subscription_history
AFTER UPDATE ON subscriptions
FOR EACH ROW EXECUTE PROCEDURE insert_subscription_history();
            """,
            """DROP TRIGGER trg_insert_subscription_history ON subscriptions;"""
        ),
    ]

```

## File: `core/migrations/0079_subscriptionrequest_app_user.py`
- **File Size:** 807 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-05-22 15:08

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_subscription_subscriptionhistory_subscriptionrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionrequest',
            name='app_user',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='core.Subscription'),
        ),
    ]

```

## File: `core/migrations/0080_game_premium.py`
- **File Size:** 391 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-05-28 00:39

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0079_subscriptionrequest_app_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0081_auto_20210602_2102.py`
- **File Size:** 775 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-02 21:02

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_game_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('match', 'user'), ('user', 'num')},
        ),
        migrations.RunSQL(
            '''
update games
   set num = t.num
  from (
select g.id,
       row_number() over(partition by g.user_id order by g.created_at) num
  from games g
  ) t
 where games.id = t.id
    ''',
            ''''''
        )
    ]

```

## File: `core/migrations/0082_customuser_influencer.py`
- **File Size:** 390 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-08 14:46

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_auto_20210602_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='influencer',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0083_auto_20210617_1909.py`
- **File Size:** 1280 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-17 19:09

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_customuser_influencer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tier', models.IntegerField(choices=[(1, 'Premium'), (2, 'Lite')])),
                ('expires_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser')),
            ],
            options={
                'db_table': 'manual_subscriptions',
            },
        ),
        migrations.AddField(
            model_name='transactions',
            name='manual_subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction', to='core.ManualSubscription'),
        ),
    ]

```

## File: `core/migrations/0084_auto_20210622_1216.py`
- **File Size:** 1101 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-22 12:16

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_auto_20210617_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='subscription_tier',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Premium'), (2, 'Lite')], default=0),
        ),
        migrations.AddField(
            model_name='subscription',
            name='tier',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Premium'), (2, 'Lite')], null=True),
        ),
        migrations.AlterField(
            model_name='manualsubscription',
            name='tier',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Premium'), (2, 'Lite')]),
        ),
        migrations.RunSQL(
            '''update users set subscription_tier = 1 where premium = true;''',
            ''''''
        ),
        migrations.RunSQL(
            '''update subscriptions set tier = 1;''',
            ''''''
        )
    ]

```

## File: `core/migrations/0085_game_subscription_tier.py`
- **File Size:** 575 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-22 12:29

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_auto_20210622_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='subscription_tier',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Premium'), (2, 'Lite')], default=0),
        ),
        migrations.RunSQL(
            '''update games set subscription_tier = 1 where premium = true;''',
            ''''''
        )
    ]

```

## File: `core/migrations/0086_customuser_avg_rank_percent.py`
- **File Size:** 408 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-29 11:08

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_game_subscription_tier'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avg_rank_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0087_customuser_last_name_change.py`
- **File Size:** 402 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-06-29 12:21

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_customuser_avg_rank_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_name_change',
            field=models.DateTimeField(null=True),
        ),
    ]

```

## File: `core/migrations/0088_auto_20210920_2057.py`
- **File Size:** 1876 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-09-20 20:57

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0087_customuser_last_name_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team_selection_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_selection_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='SelectionTeamPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('selection_id', models.CharField(max_length=10)),
                ('position', models.CharField(
                    choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper'),
                             ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team')),
            ],
            options={
                'db_table': 'selection_team_players',
                'unique_together': {('selection_id', 'team', 'player')},
                'index_together': {('selection_id', 'team', 'player')},
            },
        ),
    ]

```

## File: `core/migrations/0089_auto_20210920_2145.py`
- **File Size:** 630 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.2 on 2021-09-20 21:45

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0088_auto_20210920_2057'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='selectionteamplayer',
            unique_together={('selection_id', 'player')},
        ),
        migrations.AlterIndexTogether(
            name='selectionteamplayer',
            index_together={('selection_id', 'player')},
        ),
        migrations.RemoveField(
            model_name='selectionteamplayer',
            name='team',
        ),
    ]

```

## File: `core/migrations/0090_update_models.py`
- **File Size:** 3596 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add wallet_address field to CustomUser model and create new models for CardPackType, AssignedCardPack, PlayersTeams, PlayerBucket, and AssignedPlayer

```
# Generated by Django 2.2 on 2024-02-03 21:38

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_auto_20210920_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPackType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'card_pack_types',
            },
        ),
        migrations.CreateModel(
            name='PlayersTeams',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'players_teams',
            },
        ),
        migrations.CreateModel(
            name='PlayerBucket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Team')),
            ],
            options={
                'db_table': 'player_bucket',
            },
        ),
        migrations.CreateModel(
            name='AssignedPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PlayerBucket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'assigned_players',
            },
        ),
        migrations.CreateModel(
            name='AssignedCardPack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('opened', models.BooleanField(default=False)),
                ('card_pack_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CardPackType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'assigned_card_packs',
            },
        ),
    ]

```

## File: `core/migrations/0091_update_models.py`
- **File Size:** 468 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add wallet_address field to CustomUser model and create new models for CardPackType, AssignedCardPack, PlayersTeams, PlayerBucket, and AssignedPlayer

```
# Generated by Django 2.2 on 2024-02-03 22:19

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0090_update_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerbucket',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PlayersTeams'),
        ),
    ]

```

## File: `core/migrations/0092_update_models.py`
- **File Size:** 410 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add wallet_address field to CustomUser model and create new models for CardPackType, AssignedCardPack, PlayersTeams, PlayerBucket, and AssignedPlayer

```
# Generated by Django 2.2 on 2024-02-03 23:18

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0093_update_models.py`
- **File Size:** 1788 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-06 20:45

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0092_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedcardpack',
            name='opened_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='common_guarantee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='legendary_guarantee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='rare_guarantee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='ultra_rare_guarantee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='uncommon_guarantee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='rarity',
            field=models.CharField(choices=[('common', 'Common'), ('uncommon', 'Uncommon'), ('rare', 'Rare'), ('ultra_rare', 'Ultra Rare'), ('legendary', 'Legendary')], default='common', max_length=10),
        ),
        migrations.AlterField(
            model_name='playersteams',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Country'),
        ),
    ]

```

## File: `core/migrations/0094_update_models.py`
- **File Size:** 961 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-06 22:14

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_update_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderboardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leaderboard_types',
            },
        ),
        migrations.AddField(
            model_name='matchleaderboard',
            name='leaderboard_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.LeaderboardType'),
        ),
    ]

```

## File: `core/migrations/0095_update_models.py`
- **File Size:** 3100 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-07 00:25

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0094_update_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('season', 'Season'), ('country', 'Country'), ('team', 'Team')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaderboards', to='core.Season')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaderboards', to='core.Team')),
            ],
            options={
                'db_table': 'leaderboards',
            },
        ),
        migrations.CreateModel(
            name='MatchDay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'match_days',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='match_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='core.MatchDay'),
        ),
        migrations.CreateModel(
            name='UserLeaderboardSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscription_date', models.DateTimeField(auto_now_add=True)),
                ('leaderboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Leaderboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'user_leaderboard_subscriptions',
                'unique_together': {('user', 'leaderboard')},
            },
        ),
    ]

```

## File: `core/migrations/0096_update_models.py`
- **File Size:** 516 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-07 00:46

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0095_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaderboards', to='core.Country'),
        ),
    ]

```

## File: `core/migrations/0097_update_models.py`
- **File Size:** 483 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-07 14:05

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0096_update_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='category',
            field=models.CharField(choices=[('season', 'Season'), ('country', 'Country'), ('team', 'Team'), ('matchday', 'Matchday')], max_length=50),
        ),
    ]

```

## File: `core/migrations/0098_update_models.py`
- **File Size:** 3671 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-08 01:32

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0097_update_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerbucket',
            name='rarity',
        ),
        migrations.AddField(
            model_name='assignedplayer',
            name='rarity',
            field=models.CharField(choices=[('common', 'Common'), ('uncommon', 'Uncommon'), ('rare', 'Rare'), ('ultra_rare', 'Ultra Rare'), ('legendary', 'Legendary')], default='common', max_length=10),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='bronze',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='common',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Country'),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='diamond',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='game_position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='gold',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='legendary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='platinum',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='rare',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='real_popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='silver',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='ultra_rare',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='uncommon',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerbucket',
            name='usable_popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playerbucket',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
        migrations.DeleteModel(
            name='PlayersTeams',
        ),
    ]

```

## File: `core/migrations/0099_update_models.py`
- **File Size:** 1386 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add leaderboard functionality to user model

```
# Generated by Django 2.2 on 2024-02-09 02:53

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0098_update_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardpacktype',
            old_name='common_guarantee',
            new_name='tier1_guaranteed',
        ),
        migrations.RenameField(
            model_name='cardpacktype',
            old_name='legendary_guarantee',
            new_name='tier2_guaranteed',
        ),
        migrations.RenameField(
            model_name='cardpacktype',
            old_name='rare_guarantee',
            new_name='tier3_guaranteed',
        ),
        migrations.RenameField(
            model_name='cardpacktype',
            old_name='ultra_rare_guarantee',
            new_name='tier4_guaranteed',
        ),
        migrations.RenameField(
            model_name='cardpacktype',
            old_name='uncommon_guarantee',
            new_name='tier5_guaranteed',
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardpacktype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0100_update_models.py`
- **File Size:** 3583 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Delete item purchase tracker migration file

```
# Generated by Django 2.2 on 2024-02-09 15:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0099_update_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('page_url', models.TextField(blank=True, null=True)),
                ('purchase_img_url', models.TextField(blank=True, null=True)),
                ('contract_abbr', models.TextField()),
                ('contract_address', models.TextField()),
                ('token_id', models.TextField(blank=True, null=True)),
                ('stripe_price_id', models.TextField(blank=True, null=True)),
                ('min_quantity', models.IntegerField(blank=True, null=True)),
                ('default_quantity', models.IntegerField(blank=True, null=True)),
                ('max_quantity', models.IntegerField(blank=True, null=True)),
                ('whitelist_required', models.BooleanField(default=False)),
                ('start_date_at', models.DateTimeField()),
                ('close_date_at', models.DateTimeField()),
                ('bonus_quantity', django.contrib.postgres.fields.jsonb.JSONField()),
                ('type', models.IntegerField(choices=[(1, 'CreditToken'), (2, 'CardPack')], default=1)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='PurchaseTracker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('contract', models.TextField()),
                ('token_id', models.TextField()),
                ('delivered', models.BooleanField(default=False)),
                ('purchased_at', models.DateTimeField(blank=True, null=True)),
                ('blockchain_uuid', models.TextField(blank=True, null=True)),
                ('payment_platform_uuid', models.TextField(blank=True, null=True)),
                ('blockchain_order_status', models.IntegerField(choices=[(0, 'Mint not started'), (1, 'Mint in progress'), (2, 'Mint Failed'), (3, 'Mint Succeeded'), (4, 'Mint Timeout')], default=0)),
                ('payment_platform_status', models.IntegerField(choices=[(0, 'Processing'), (1, 'Failed'), (2, 'Completed'), (3, 'Expired')], default=0)),
                ('payment_platform_type', models.IntegerField(choices=[(1, 'Stripe')], default=1)),
                ('cancel_url', models.TextField(blank=True, null=True)),
                ('success_url', models.TextField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser')),
            ],
            options={
                'db_table': 'purchase_trackers',
            },
        ),
    ]

```

## File: `core/migrations/0101_update_models.py`
- **File Size:** 928 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add fields to CustomUser model

```
# Generated by Django 2.2 on 2024-02-16 13:37

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0100_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password_hash',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='token_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0102_update_models.py`
- **File Size:** 413 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add fields to CustomUser model

```
# Generated by Django 2.2 on 2024-02-16 14:49

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0101_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verification_token',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

```

## File: `core/migrations/0103_update_models.py`
- **File Size:** 416 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add fields to CustomUser model

```
# Generated by Django 2.2 on 2024-02-20 14:43

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0102_update_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='verification_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

```

## File: `core/migrations/0104_add_new_model.py`
- **File Size:** 3327 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 add credits

```
# Generated by Django 2.2 on 2024-02-22 13:27

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0103_update_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('contract', models.TextField(blank=True, null=True)),
                ('token_id', models.TextField(blank=True, null=True)),
                ('delivered', models.BooleanField(default=False)),
                ('purchased_at', models.DateTimeField(blank=True, null=True)),
                ('blockchain_uuid', models.TextField(blank=True, null=True)),
                ('payment_platform_uuid', models.TextField(blank=True, null=True)),
                ('blockchain_order_status', models.IntegerField(choices=[(0, 'Mint not started'), (1, 'Mint in progress'), (2, 'Mint Failed'), (3, 'Mint Succeeded'), (4, 'Mint Timeout')], default=0)),
                ('payment_platform_status', models.IntegerField(choices=[(0, 'Processing'), (1, 'Failed'), (2, 'Completed'), (3, 'Expired')], default=0)),
                ('payment_platform_type', models.IntegerField(choices=[(1, 'Stripe'), (2, 'INTERNAL')], default=1)),
                ('cancel_url', models.TextField(blank=True, null=True)),
                ('success_url', models.TextField(blank=True, null=True)),
                ('payment_platform_url', models.TextField(blank=True, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='manual_subscription',
        ),
        migrations.AddField(
            model_name='transactions',
            name='blockchain_uuid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='object_type',
            field=models.CharField(choices=[('v', 'virtual'), ('c', 'crypto'), ('n', 'nft')], default='v', max_length=1),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='PurchaseTracker',
        ),
        migrations.AddField(
            model_name='transactions',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Order'),
        ),
    ]

```

## File: `core/migrations/0105_update_db_trigger.py`
- **File Size:** 1037 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 add credits

```
# Generated by Django 2.2 on 2024-02-22 13:34

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0104_add_new_model'),
    ]

    operations = [
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION update_user_balance()
  RETURNS TRIGGER AS $$
DECLARE
    v_rec record;
BEGIN 
    select *
      into v_rec
      from users
     where id = NEW.user_id
       for update;
    
    IF NEW.object_type = 'v' THEN
        UPDATE users
        SET balance = balance + NEW.amount
        WHERE id = NEW.user_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION update_user_balance();"""
        ),
        migrations.RunSQL(
            """
CREATE OR REPLACE TRIGGER trg_update_user_balance
AFTER INSERT ON transactions
FOR EACH ROW
WHEN (NEW.object_type = 'v')
EXECUTE PROCEDURE update_user_balance();
            """,
            """DROP TRIGGER trg_update_user_balance ON transactions;"""
        ),

    ]

```

## File: `core/migrations/0106_update_fields.py`
- **File Size:** 926 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1481 add credits

```
# Generated by Django 2.2 on 2024-02-27 08:28

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0105_update_db_trigger'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='transactions',
            name='quantity',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='WithdrawRequest',
        ),
    ]

```

## File: `core/migrations/0107_update_feed_models.py`
- **File Size:** 2958 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** to keep correlativity on migrations

```
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0106_update_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='ortec_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='opta_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='competitionedition',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='competitionphase',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='selectionteamplayer',
            name='selection_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='match',
            name='edition',
            field=models.ForeignKey(null=True, on_delete=models.deletion.DO_NOTHING, to='core.CompetitionEdition'),
        ),
    ]

```

## File: `core/migrations/0108_update_feed_models.py`
- **File Size:** 551 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixes for syncing and enhacements on parsing Adds changes on fields, makesno sense having unique and event id fields as integer, since the provider could offer uuid, or strings as ids, we have to forsee that

```
# Generated by Django 2.2 on 2024-03-27 22:20

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0107_update_feed_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optafeeditem',
            name='unique_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='optafeeditem',
            name='event_id',
            field=models.CharField(max_length=50),
        ),
    ]

```

## File: `core/migrations/0109_matchleaderboard_transaction.py`
- **File Size:** 508 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1517 add rewards for leaderboard entries

```
# Generated by Django 2.2 on 2024-04-04 08:43

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0108_update_feed_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchleaderboard',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Transactions'),
        ),
    ]

```

## File: `core/migrations/0110_chatmessage_chatroom.py`
- **File Size:** 2350 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** more table fixes

```
# Generated by Django 2.2 on 2024-04-09 21:36

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0109_matchleaderboard_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('members', models.ManyToManyField(related_name='chat_rooms', to='core.CustomUser')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'chat_rooms',
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.ChatRoom')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'chat_messages',
            },
        ),
        migrations.RunSQL("""
    CREATE OR REPLACE FUNCTION set_updated_at() RETURNS trigger AS $update_group_new$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
    $update_group_new$ LANGUAGE plpgsql;
    """),
    migrations.RunSQL("""
    CREATE OR REPLACE TRIGGER chat_room_updated_at
        BEFORE UPDATE ON chat_rooms FOR EACH ROW EXECUTE FUNCTION set_updated_at();
    """),
        migrations.RunSQL("""
    INSERT INTO chat_rooms (id, name, description, created_at, updated_at) VALUES
        ('{}','laliga', 'LaLiga Chat Room', now(), now());"""
        .replace('{}', str(uuid.uuid4()))),
    ]

```

## File: `core/migrations/0111_chatroommember.py`
- **File Size:** 1367 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** rebased migration from model

```
# Generated by Django 2.2 on 2024-04-11 21:34

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0110_chatmessage_chatroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='members',
        ),
        migrations.CreateModel(
            name='ChatRoomMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muted', models.BooleanField(default=False)),
                ('banned', models.BooleanField(default=False)),
                ('banned_at', models.DateTimeField(blank=True, null=True)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ChatRoom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'chat_room_members',
                'unique_together': {('room', 'user')},
            },
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(through='core.ChatRoomMember', to='core.CustomUser'),
        ),
    ]
```

## File: `core/migrations/0112_update_import_ids.py`
- **File Size:** 1878 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** increase the import_id's size

```
# Generated by Django 2.2 on 2024-04-17 11:59

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0111_chatroommember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='competitionedition',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='competitionphase',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]

```

## File: `core/migrations/0113_update_position_choices.py`
- **File Size:** 1380 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixes for selection team players position choices in tables

```
# Generated by Django 2.2 on 2024-04-17 19:12

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0112_update_import_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Wing Back'), ('d', 'Defender'), ('m', 'Defensive Midfielder'), ('m', 'Midfielder'), ('m', 'Attacking Midfielder'), ('f', 'Striker'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='seasonteamplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Wing Back'), ('d', 'Defender'), ('m', 'Defensive Midfielder'), ('m', 'Midfielder'), ('m', 'Attacking Midfielder'), ('f', 'Striker'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='selectionteamplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Wing Back'), ('d', 'Defender'), ('m', 'Defensive Midfielder'), ('m', 'Midfielder'), ('m', 'Attacking Midfielder'), ('f', 'Striker'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
    ]

```

## File: `core/migrations/0114_chatroommember_mod.py`
- **File Size:** 392 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add chat room mod flag for membership of a channel

```
# Generated by Django 2.2 on 2024-04-19 22:29

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0113_update_position_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroommember',
            name='mod',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0115_match_week.py`
- **File Size:** 375 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adds week field to match so we can use that to filter by GW

```
# Generated by Django 2.2 on 2024-04-25 15:21

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0114_chatroommember_mod'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='week',
            field=models.IntegerField(default=0),
        ),
    ]

```

## File: `core/migrations/0116_competition_config.py`
- **File Size:** 1344 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adds filter for the competition config

```
# Generated by Django 2.2 on 2024-05-07 15:34

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0115_match_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=128, null=True, unique=True)),
                ('name', models.TextField()),
                ('filter', models.TextField()),
                ('enabled', models.BooleanField(default=False)),
                ('related_competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Competition')),
            ],
            options={
                'db_table': 'competition_config',
            },
        ),
        migrations.AddField(
            model_name='competition',
            name='config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CompetitionConfig'),
        ),
    ]

```

## File: `core/migrations/0117_sports_and_pwoerups.py`
- **File Size:** 1613 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix for migration of sports and powerups

```
# Generated by Django 2.2 on 2024-05-14 12:47

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0116_competition_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sports',
            },
        ),
        migrations.AddField(
            model_name='powerup',
            name='cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='powerup',
            name='type',
            field=models.IntegerField(choices=[(1, 'event'), (2, 'game')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
        migrations.AddField(
            model_name='powerup',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
    ]

```

## File: `core/migrations/0118_player_normalized_name.py`
- **File Size:** 397 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** normalized name up

```
# Generated by Django 2.2 on 2024-05-15 11:18

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0117_sports_and_pwoerups'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='normalized_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0119_normalized_names.py`
- **File Size:** 705 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Fill the normalized names

```
from django.db import migrations

def fill_normalized_name(apps, schema_editor):
    Player = apps.get_model('core', 'Player')
    db_alias = schema_editor.connection.alias
    players = Player.objects.using(db_alias).all()
    for player in players:
        if player.nick_name and not any(char + '.' in player.nick_name for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            player.normalized_name = player.nick_name
        else:
            player.normalized_name = player.full_name
        player.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_player_normalized_name'), 
    ]

    operations = [
        migrations.RunPython(fill_normalized_name),
    ]

```

## File: `core/migrations/0120_boosts_initial.py`
- **File Size:** 5061 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** powerup conditions and actions fix

```
# Generated by Django 2.1.7 on 2020-12-04 16:37

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0119_normalized_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerup',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        # enable UUID generation in postgresql!
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'),
        # drop not null from updated_at and created_at will have now() as default
        migrations.RunSQL('''
            ALTER TABLE sports
                ALTER COLUMN created_at SET DEFAULT CURRENT_TIMESTAMP;
            ALTER TABLE sports
                ALTER COLUMN updated_at DROP NOT NULL;
        '''),
        # set cost as 0 by default in the powerups table
        migrations.RunSQL('''
            ALTER TABLE powerups
                ALTER COLUMN cost SET DEFAULT 0;
            ALTER TABLE powerups
                ALTER COLUMN enabled SET DEFAULT false;
        '''),
        # set ordering 10 (closest to highest as data would suggest) as default
        migrations.RunSQL('''
            ALTER TABLE powerup_actions
                ALTER COLUMN ordering SET DEFAULT 10;
        '''),
        # insert sport "Soccer" (futbol) and powerups
        migrations.RunSQL(
            '''
BEGIN;
DO $$
DECLARE
    sportID             UUID;
    typeGameEvent       INT := 1;
    typeGameSpecial     INT := 2; -- apply special rules
    maxPowerupID        INT;
    maxPowerupActionID  INT;
BEGIN
    SELECT uuid_generate_v4() INTO sportID;
    INSERT INTO sports(id, name, description) VALUES
        (sportID, 'Soccer', 'King of sports. Real name: Fútbol or Football');
    UPDATE actions SET sport_id = sportID; -- assume current actions are just soccer ones
    UPDATE powerups SET sport_id = sportID; -- assume current powerups are just soccer ones
    SELECT max(id) FROM powerups INTO maxPowerupID;
    PERFORM setval('powerups_id_seq', maxPowerupID);
    INSERT INTO powerups(sport_id, name, description, duration, multiplier, type) VALUES
    (sportID, 'Sharpshooter Pro', '2x points for positive shooting actions', 1200, 2, typeGameEvent), -- Shooting
    (sportID, 'Sharpshooter Elite', '2.5x points for positive shooting actions', 600, 2.5, typeGameEvent), -- Shooting
    (sportID, 'Sharpshooter Ultra', '3x points for positive shooting actions', 300, 3, typeGameEvent), -- Shooting
    (sportID, 'Playmaker Pro', '2x points for positive passing actions', 1200, 2, typeGameEvent), -- Passing
    (sportID, 'Playmaker Elite', '2.5x points for positive passing actions', 600, 2.5, typeGameEvent), -- Passing
    (sportID, 'Playmaker Ultra', '3x points for positive passing actions', 300, 3, typeGameEvent), -- Passing
    (sportID, 'Shield', 'Ignore negative points', 300, 1, typeGameSpecial), -- All events
    (sportID, 'Controller Pro', '2x points for positive dribbling actions', 1200, 2, typeGameEvent), -- Dribbling
    (sportID, 'Controller Elite', '2.5x points for positive dribbling actions', 600, 2.5, typeGameEvent), -- Dribbling
    (sportID, 'Controller Ultra', '3x points for positive dribbling actions', 300, 3, typeGameEvent), -- Dribbling
    (sportID, 'Guardian Pro', '2x points for positive goalkeeper actions', 1200, 2, typeGameEvent), -- goalkeeper
    (sportID, 'Guardian Elite', '2.5x points for positive goalkeeper actions', 600, 2.5, typeGameEvent), -- goalkeeper
    (sportID, 'Guardian Ultra', '3x points for positive goalkeeper actions', 300, 3, typeGameEvent), -- goalkeeper
    (sportID, 'Substitution', 'Swap out one of your players for another', 0, 0, typeGameSpecial), -- Special allow substitutions in game
    (sportID, 'Reverse', 'All negative points are treated as positive', 60, 1, typeGameSpecial); -- All events
    SELECT max(id) FROM powerup_actions INTO maxPowerupActionID;
    PERFORM setval('powerup_actions_id_seq', maxPowerupActionID);
    INSERT INTO powerup_actions(powerup_id, action_id)
    SELECT p.id, a.id FROM powerups p, actions a
        WHERE p.name ilike 'Sharpshooter%' and a.name ilike '%shot%' and score > 0;
    INSERT INTO powerup_actions(powerup_id, action_id)
    SELECT p.id, a.id FROM powerups p, actions a
            WHERE p.name ilike 'Playmaker%' and a.name ilike '%pass%' and score > 0;
    INSERT INTO powerup_actions(powerup_id, action_id)
    SELECT p.id, a.id FROM powerups p, actions a
            WHERE p.name ilike 'Controller%' and a.name ilike 'Dribble%' and score > 0;
    INSERT INTO powerup_actions(powerup_id, action_id)
    SELECT p.id, a.id FROM powerups p, actions a
            WHERE p.name ilike 'Guardian%' and a.description ilike 'keep%' and score > 0;
    UPDATE powerups SET enabled = TRUE;
END $$;
            ''',
            '''
            DELETE FROM powerup_actions WHERE powerup_id IN (select id FROM powerups WHERE id > 7);
            DELETE FROM powerups WHERE id > 7;
            setval('powerup_id_seq', 7);
            '''),
    ]

```

## File: `core/migrations/0121_auto_20240521_1825.py`
- **File Size:** 885 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1656 make new rewards

```
# Generated by Django 2.2 on 2024-05-21 18:25

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0120_boosts_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchreward',
            name='max_position',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='min_position',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='matchreward',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='matchreward',
            unique_together={('match', 'min_position', 'max_position')},
        ),
    ]

```

## File: `core/migrations/0122_datafeedsimmodel.py`
- **File Size:** 1152 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** rebased and reorganized the migration for this feature

```
# Generated by Django 2.2 on 2024-05-23 23:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0121_auto_20240521_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFeedSimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(blank=True, max_length=50, null=True)),
                ('json_events', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'data_feed_sim',
            },
        ),
    ]

```

## File: `core/migrations/0123_eventthrottler.py`
- **File Size:** 882 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** throttling events the feature will be configurable

```
# Generated by Django 2.2 on 2024-05-24 02:38

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0122_datafeedsimmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventThrottler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(max_length=32)),
                ('event_type', models.CharField(db_column='type', max_length=32)),
                ('data', models.TextField(blank=True)),
                ('processing', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_throttler',
            },
        ),
    ]

```

## File: `core/migrations/0124_powerup_conditions.py`
- **File Size:** 909 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix for powerup conditions and actions

```
# Generated by Django 2.2 on 2024-05-29 19:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0123_eventthrottler'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerup',
            name='conditions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True),
        ),
        migrations.RunSQL(
            '''UPDATE powerups
               SET conditions = '[{ "name": "shield"}]'
               WHERE name ilike 'Shield';
               UPDATE powerups
               SET conditions = '[{ "name": "substitution"}]'
               WHERE name ilike 'Substitution';
               UPDATE powerups
               SET conditions = '[{ "name": "reverse"}]'
               WHERE name ilike 'Reverse';'''
        )
    ]

```

## File: `core/migrations/0125_powerup_actions.py`
- **File Size:** 475 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix for powerup conditions and actions

```
# Generated by Django 2.2 on 2024-05-29 19:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0124_powerup_conditions'),
    ]

    operations = [
        migrations.RunSQL(
            '''
INSERT INTO powerup_actions(powerup_id, action_id)
    SELECT p.id, a.id FROM powerups p, actions a
WHERE p.name ilike 'shield' or p.name ilike 'reverse';'''
        )
    ]

```

## File: `core/migrations/0126_update_models.py`
- **File Size:** 410 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Migrations added

```
# Generated by Django 2.2 on 2024-05-31 15:25

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0125_powerup_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='firebase_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

```

## File: `core/migrations/0127_add_sport_relation_to_match_and_game.py`
- **File Size:** 677 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add migration

```
# Generated by Django 2.2 on 2024-06-03 21:36

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0126_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
        migrations.AddField(
            model_name='match',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
    ]

```

## File: `core/migrations/0128_ads_sport_to_competition_and_config.py`
- **File Size:** 719 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add sport to competition to be defined from start in the configuration

```
# Generated by Django 2.2 on 2024-06-03 22:57

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0127_add_sport_relation_to_match_and_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
        migrations.AddField(
            model_name='competitionconfig',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
    ]

```

## File: `core/migrations/0129_update_models.py`
- **File Size:** 524 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Migrate the new user schema

```
# Generated by Django 2.2 on 2024-06-04 17:30

import django.contrib.postgres.fields
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0128_ads_sport_to_competition_and_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='finished_games',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, size=None),
        ),
    ]

```

## File: `core/migrations/0130_update_models.py`
- **File Size:** 396 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** change user schema

```
# Generated by Django 2.2 on 2024-06-04 19:12

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0129_update_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='finished_games',
            field=models.TextField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0131_update_models.py`
- **File Size:** 377 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add notified to games

```
# Generated by Django 2.2 on 2024-06-10 13:10

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0130_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0132_update_models.py`
- **File Size:** 517 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Adding Category and icon to the Actions

```
# Generated by Django 2.2 on 2024-06-10 14:57

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0131_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='icon',
            field=models.TextField(null=True),
        ),
    ]

```

## File: `core/migrations/0133_chatroom_match.py`
- **File Size:** 509 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** reorganize migration files to accomodate latest `main` branch changes (2)

```
# Generated by Django 2.2 on 2024-06-10 15:39

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0132_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='chat_rooms', to='core.Match'),
        ),
    ]

```

## File: `core/migrations/0134_chatroom_import_id.py`
- **File Size:** 405 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix migration for chat_rooms adding import id to fall into the pattern for update_or_create (it doesnt hurt)

```
# Generated by Django 2.2 on 2024-06-10 16:58

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0133_chatroom_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='import_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]

```

## File: `core/migrations/0135_match_enabled.py`
- **File Size:** 381 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** set enabled flag for matches

```
# Generated by Django 2.2 on 2024-06-12 01:28

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0134_chatroom_import_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]

```

## File: `core/migrations/0136_ppg_materialized_views.py`
- **File Size:** 2266 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix ppg calculation also added for future reference how to count red/yellow cards

```
# Generated by Django 2.2 on 2024-05-29 19:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0135_match_enabled'),
    ]

    operations = [
        migrations.RunSQL(
            '''
-- Create a Materialized View for Points Per Game (PPG) by player
DROP MATERIALIZED VIEW IF EXISTS player_ppg;
CREATE MATERIALIZED VIEW IF NOT EXISTS player_ppg AS
SELECT
    p.id,
    p.import_id,
    p.full_name,
    SUM(me.points) / COUNT(me.match_id) AS ppg,  -- Calculate Points Per Game (PPG)
    -- CASE WHEN SUM(me.points) / COUNT(me.match_id) < 0 THEN 0 ELSE SUM(me.points) / COUNT(me.match_id) END AS ppg,  -- Calculate Points Per Game (PPG)
    SUM(CASE WHEN me.type = 45 THEN 1 ELSE 0 END) AS total_goals  -- Counting goals
    -- SUM(CASE WHEN me.type = 58 OR me.type = 59 THEN 1 ELSE 0 END) AS total_yellow_cards,  -- Counting yellow_cards
    -- SUM(CASE WHEN me.type = 60 THEN 1 ELSE 0 END) AS total_red_cards  -- Counting red_cards
FROM
    match_events me
JOIN players p ON p.id = me.player_id
WHERE
    points IS NOT NULL  -- Consider only events with non-null points
GROUP BY
    p.id
ORDER BY
    ppg DESC;
REFRESH MATERIALIZED VIEW player_ppg;

-- Create a function to refresh the materialized view
CREATE OR REPLACE FUNCTION refresh_player_ppg_view()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if the new status is 'e' and it is different from the old status
    IF NEW.status = 'e' AND OLD.status IS DISTINCT FROM NEW.status THEN
        -- Refresh the materialized view
        PERFORM pg_sleep(2);  -- Add a slight delay to ensure all related changes are committed
        REFRESH MATERIALIZED VIEW player_ppg;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger on the matches table to call the function when the status changes to 'e'
CREATE OR REPLACE TRIGGER match_end_refresh_ppg
AFTER UPDATE OF status ON matches
FOR EACH ROW
WHEN (NEW.status = 'e' AND OLD.status IS DISTINCT FROM NEW.status)
EXECUTE FUNCTION refresh_player_ppg_view();
''',
'''
DROP MATERIALIZED VIEW IF EXISTS player_ppg;
DROP FUNCTION IF EXISTS refresh_player_ppg_view;
DROP TRIGGER IF EXISTS match_end_refresh_ppg ON matches;
''',
        )
    ]

```

## File: `core/migrations/0137_auto_20240621_1913.py`
- **File Size:** 386 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix opta version

```
# Generated by Django 2.2 on 2024-06-21 19:13

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0136_ppg_materialized_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optafeeditemversion',
            name='version',
            field=models.TextField(),
        ),
    ]

```

## File: `core/migrations/0138_product_producttransactions.py`
- **File Size:** 2279 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1777 & PS-1778 WIP (#126)

```
# Generated by Django 2.2 on 2024-07-01 22:51

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0137_auto_20240621_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('apple_product_id', models.CharField(blank=True, max_length=255, null=True)),
                ('google_product_id', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('active', models.BooleanField(default=True)),
                ('product_type', models.CharField(blank=True, choices=[('consumable', 'Consumable'), ('nonconsumable', 'Non-Consumable'), ('subscription', 'Subscription'), ('nft', 'NFT')], default='consumable', max_length=255, null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductTransactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Product')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Transactions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser')),
            ],
            options={
                'db_table': 'product_transactions',
            },
        ),
    ]

```

## File: `core/migrations/0139_update_models.py`
- **File Size:** 429 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding session_id

```
# Generated by Django 2.2 on 2024-07-04 21:48

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0138_product_producttransactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sequence_session_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0140_product_transaction_flow.py`
- **File Size:** 1169 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add flow for product purchases (#130)

```
# Generated by Django 2.2 on 2024-07-09 20:18

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0139_update_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttransactions',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.deletion.DO_NOTHING, to='core.Transactions'),
        ),
        migrations.AddField(
            model_name='producttransactions',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producttransactions',
            name='confirmed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producttransactions',
            name='initiated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producttransactions',
            name='initiated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0141_producttransactions_external_transaction_id.py`
- **File Size:** 439 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Adds external transaction ID to transactions (#131)

```
# Generated by Django 2.2 on 2024-07-09 21:54

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0140_product_transaction_flow'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransactions',
            name='external_transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0142_product_name_to_product_id.py`
- **File Size:** 670 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** User must be nullable to initiate process...  (#133)

```
# Generated by Django 2.2 on 2024-07-09 22:26

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0141_producttransactions_external_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_id',
        ),
        migrations.AlterField(
            model_name='producttransactions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
    ]

```

## File: `core/migrations/0143_nftbucket.py`
- **File Size:** 4502 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** table changes

```
# Generated by Django 2.2 on 2024-07-10 15:04

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0142_product_name_to_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NftBucket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('team_id', models.UUIDField(blank=True, default=None, null=True)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('game_position', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('common_claiming', models.FloatField(blank=True, default=0.0, null=True)),
                ('common_defence', models.FloatField(blank=True, default=0.0, null=True)),
                ('common_distribution', models.FloatField(blank=True, default=0.0, null=True)),
                ('common_dribbling', models.FloatField(blank=True, default=0.0, null=True)),
                ('common_passing', models.FloatField(blank=True, default=0.0, null=True)),
                ('common_shooting', models.FloatField(blank=True, default=0.0, null=True)),
                ('common_stopping', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_claiming', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_defence', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_distribution', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_dribbling', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_passing', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_shooting', models.FloatField(blank=True, default=0.0, null=True)),
                ('legendary_stopping', models.FloatField(blank=True, default=0.0, null=True)),
                ('nationality', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('rare_claiming', models.FloatField(blank=True, default=0.0, null=True)),
                ('rare_defence', models.FloatField(blank=True, default=0.0, null=True)),
                ('rare_distribution', models.FloatField(blank=True, default=0.0, null=True)),
                ('rare_dribbling', models.FloatField(blank=True, default=0.0, null=True)),
                ('rare_passing', models.FloatField(blank=True, default=0.0, null=True)),
                ('rare_shooting', models.FloatField(blank=True, default=0.0, null=True)),
                ('rare_stopping', models.FloatField(blank=True, default=0.0, null=True)),
                ('star_rating', models.FloatField(default=0.0)),
                ('ultra_rare_claiming', models.FloatField(blank=True, default=0.0, null=True)),
                ('ultra_rare_defence', models.FloatField(blank=True, default=0.0, null=True)),
                ('ultra_rare_distribution', models.FloatField(blank=True, default=0.0, null=True)),
                ('ultra_rare_dribbling', models.FloatField(blank=True, default=0.0, null=True)),
                ('ultra_rare_passing', models.FloatField(blank=True, default=0.0, null=True)),
                ('ultra_rare_shooting', models.FloatField(blank=True, default=0.0, null=True)),
                ('ultra_rare_stopping', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_claiming', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_defence', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_distribution', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_dribbling', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_passing', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_shooting', models.FloatField(blank=True, default=0.0, null=True)),
                ('uncommon_stopping', models.FloatField(blank=True, default=0.0, null=True)),
            ],
            options={
                'db_table': 'nft_bucket',
            },
        ),
    ]

```

## File: `core/migrations/0144_auto_20240712_1925.py`
- **File Size:** 4199 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** card packs and player assignation

```
# Generated by Django 2.2 on 2024-07-12 19:25

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0143_nftbucket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedplayer',
            name='player',
        ),
        migrations.RemoveField(
            model_name='cardpacktype',
            name='tier1_guaranteed',
        ),
        migrations.RemoveField(
            model_name='cardpacktype',
            name='tier2_guaranteed',
        ),
        migrations.RemoveField(
            model_name='cardpacktype',
            name='tier3_guaranteed',
        ),
        migrations.RemoveField(
            model_name='cardpacktype',
            name='tier4_guaranteed',
        ),
        migrations.RemoveField(
            model_name='cardpacktype',
            name='tier5_guaranteed',
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='tier1',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='tier2',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='tier3',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='tier4',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='tier5',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='common_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='common_metadata',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='legendary_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='legendary_metadata',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='rare_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='rare_metadata',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='ultra_rare_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='ultra_rare_metadata',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='uncommon_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='uncommon_metadata',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0145_assignedplayer_player_nft.py`
- **File Size:** 513 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** card packs and player assignation

```
# Generated by Django 2.2 on 2024-07-13 17:35

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0144_auto_20240712_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedplayer',
            name='player_nft',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.NftBucket'),
        ),
    ]

```

## File: `core/migrations/0146_rename_products_to_store_products.py`
- **File Size:** 731 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Fix for naming of IAP flow (#140)

```
# Generated by Django 2.2 on 2024-07-16 16:25

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0145_assignedplayer_player_nft'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='StoreProduct',
        ),
        migrations.RenameModel(
            old_name='ProductTransactions',
            new_name='StoreProductTransactions',
        ),
        migrations.AlterModelTable(
            name='storeproduct',
            table='store_products',
        ),
        migrations.AlterModelTable(
            name='storeproducttransactions',
            table='store_product_transactions',
        ),
    ]

```

## File: `core/migrations/0147_rename_product_id_to_store_product_id.py`
- **File Size:** 393 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Fix for naming of IAP flow (#140)

```
# Generated by Django 2.2 on 2024-07-16 16:25

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0146_rename_products_to_store_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeproduct',
            old_name='product_id',
            new_name='store_product_id',
        ),
    ]

```

## File: `core/migrations/0148_assignedplayer_nft_id.py`
- **File Size:** 444 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add the nft id

```
# Generated by Django 2.2 on 2024-07-17 14:04

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0147_rename_product_id_to_store_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedplayer',
            name='nft_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0149_auto_20240717_2247.py`
- **File Size:** 575 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding revealed to assigned card pack schema

```
# Generated by Django 2.2 on 2024-07-17 22:47

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0148_assignedplayer_nft_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedcardpack',
            name='revealed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assignedcardpack',
            name='revealed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0150_remove_assignedplayer_rarity.py`
- **File Size:** 331 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding new schema to the nft assigned players and card packs

```
# Generated by Django 2.2 on 2024-07-18 02:45

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0149_auto_20240717_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedplayer',
            name='rarity',
        ),
    ]

```

## File: `core/migrations/0151_remove_assignedplayer_user.py`
- **File Size:** 339 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** remove user from assigned player

```
# Generated by Django 2.2 on 2024-07-18 02:50

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0150_remove_assignedplayer_rarity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedplayer',
            name='user',
        ),
    ]

```

## File: `core/migrations/0152_assignedcardpack_card_ids.py`
- **File Size:** 579 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add the minted card ids to the

```
# Generated by Django 2.2 on 2024-07-18 03:04

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0151_remove_assignedplayer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedcardpack',
            name='card_ids',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]

```

## File: `core/migrations/0153_auto_20240719_1958.py`
- **File Size:** 6003 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** added shared task

```
# Generated by Django 2.2 on 2024-07-17 19:58

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0152_assignedcardpack_card_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('tier', models.IntegerField()),
                ('percentage', models.FloatField(default=0.01)),
            ],
            options={
                'db_table': 'divisions',
            },
        ),
        migrations.CreateModel(
            name='GameWeek',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('scored_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('s', 'New'), ('l', 'Live'), ('f', 'Not_processed'), ('c', 'Concluded')], default='s', max_length=1)),
                ('leaderboards', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.MatchLeaderboard')),
            ],
            options={
                'db_table': 'game_weeks',
            },
        ),
        migrations.CreateModel(
            name='UserGameWeekHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('week_division_position', models.IntegerField(default=0)),
                ('week_division_tier', models.IntegerField(blank=True, null=True)),
                ('week_points', models.IntegerField(default=0)),
                ('week_coins', models.IntegerField(default=0)),
                ('new_division_tier', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('s', 'Safe'), ('p', 'Promoted'), ('d', 'Demoted')], default='s', max_length=1)),
                ('game_week', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.GameWeek')),
                ('new_division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='new_divisions', to='core.Division')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser')),
                ('week_division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Division')),
            ],
            options={
                'db_table': 'user_game_week_histories',
            },
        ),
        migrations.CreateModel(
            name='UserDivision',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Division')),
                ('game_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.GameWeek')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'user_divisions',
                'unique_together': {('user', 'division', 'game_week')},
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='divisions',
            field=models.ManyToManyField(through='core.UserDivision', to='core.Division'),
        ),
        migrations.AddField(
            model_name='matchleaderboard',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Division'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.GameWeek'),
        ),
        migrations.CreateModel(
            name='DivisionReward',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('min_position', models.IntegerField(default=1)),
                ('max_position', models.IntegerField(blank=True, null=True)),
                ('amount', models.FloatField()),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Division')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.GameWeek')),
            ],
            options={
                'db_table': 'division_rewards',
                'unique_together': {('week', 'division', 'min_position', 'max_position')},
            },
        ),
    ]

```

## File: `core/migrations/0154_auto_20240718_1218.py`
- **File Size:** 1339 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** added shared task

```
# Generated by Django 2.2 on 2024-07-18 12:18

from django.db import migrations

def insert_division_data(apps, schema_editor):
    Division = apps.get_model('core', 'Division')
    divisions = [
        {'name': "Division 10", 'tier': 10, 'percentage': 0.08},
        {'name': "Division 9", 'tier': 9, 'percentage': 0.10},
        {'name': "Division 8", 'tier': 8, 'percentage': 0.15},
        {'name': "Division 7", 'tier': 7, 'percentage': 0.19},
        {'name': "Division 6", 'tier': 6, 'percentage': 0.15},
        {'name': "Division 5", 'tier': 5, 'percentage': 0.12},
        {'name': "Division 4", 'tier': 4, 'percentage': 0.09},
        {'name': "Division 3", 'tier': 3, 'percentage': 0.07},
        {'name': "Division 2", 'tier': 2, 'percentage': 0.04},
        {'name': "Division 1", 'tier': 1, 'percentage': 0.01},
    ]

    for division in divisions:
        Division.objects.create(name=division['name'], tier=division['tier'], percentage=division['percentage'])

def delete_division_data(apps, schema_editor):
    Division = apps.get_model('core', 'Division')
    Division.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0153_auto_20240719_1958'),
    ]

    operations = [
        migrations.RunPython(insert_division_data, reverse_code=delete_division_data),
    ]

```

## File: `core/migrations/0155_gamepick_assigned_player.py`
- **File Size:** 526 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding the nft id to the game pick

```
# Generated by Django 2.2 on 2024-07-23 15:31

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0154_auto_20240718_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepick',
            name='assigned_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_player', to='core.AssignedPlayer'),
        ),
    ]

```

## File: `core/migrations/0156_assignedplayer_rarity.py`
- **File Size:** 431 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding rarity to the admin

```
# Generated by Django 2.2 on 2024-07-23 15:44

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0155_gamepick_assigned_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedplayer',
            name='rarity',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0157_auto_20240723_1804.py`
- **File Size:** 820 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix division users

```
# Generated by Django 2.2 on 2024-07-23 18:04

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0156_assignedplayer_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameweek',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season'),
        ),
        migrations.AddField(
            model_name='season',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0158_add_trigger.py`
- **File Size:** 1401 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix division leaderboard

```
# Generated by Django 2.2 on 2024-07-24 07:33

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0157_auto_20240723_1804'),
    ]

    operations = [
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION insert_match_leaderboard_record() RETURNS TRIGGER
   LANGUAGE plpgsql
   AS $$
   DECLARE
        division_id UUID;
   BEGIN
        -- Fetch the most recent division_id for the user
        SELECT ud.division_id
        INTO division_id
        FROM user_divisions ud
        WHERE ud.user_id = NEW.user_id
        ORDER BY ud.created_at DESC
        LIMIT 1;
        
        -- Insert into match_leaderboard with division_id
        INSERT INTO match_leaderboard (match_id, game_id, user_id, score, position, division_id)
        VALUES (NEW.match_id, NEW.id, NEW.user_id, NULL, NULL, division_id);
        
        RETURN NEW;
    END;
    $$;
""",
            """DROP FUNCTION insert_match_leaderboard_record();"""
        ),

        migrations.RunSQL(
            """
DROP TRIGGER IF EXISTS trg_insert_match_leaderboard_record ON games;
            
CREATE TRIGGER trg_insert_match_leaderboard_record
AFTER INSERT ON games
FOR EACH ROW EXECUTE PROCEDURE insert_match_leaderboard_record();
            """,
            """DROP TRIGGER IF EXISTS trg_insert_match_leaderboard_record ON games;"""
        ),
    ]

```

## File: `core/migrations/0159_auto_20240725_1518.py`
- **File Size:** 1437 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix division leaderboard

```
# Generated by Django 2.2 on 2024-07-25 15:18

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0158_add_trigger'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSeason',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=128, null=True, unique=True)),
                ('name', models.TextField()),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'game_seasons',
            },
        ),
        migrations.RemoveField(
            model_name='season',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='season',
            name='start_at',
        ),
        migrations.AlterField(
            model_name='gameweek',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.GameSeason'),
        ),
    ]

```

## File: `core/migrations/0160_assignedcardpack_transaction_id.py`
- **File Size:** 511 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding migrations

```
# Generated by Django 2.2 on 2024-07-26 14:59

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0159_auto_20240725_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedcardpack',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Transactions'),
        ),
    ]

```

## File: `core/migrations/0161_storeproducttransactions_origin_store.py`
- **File Size:** 440 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add origin store information which was the application store that was the item bought from (#152)

```
# Generated by Django 2.2 on 2024-07-26 18:10

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0160_assignedcardpack_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproducttransactions',
            name='origin_store',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0162_auto_20240730_1312.py`
- **File Size:** 1337 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Adding limits to packs

```
# Generated by Django 2.2 on 2024-07-30 13:12

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0161_storeproducttransactions_origin_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpacktype',
            name='pack_limits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='common_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='legendary_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='rare_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='ultra_rare_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='nftbucket',
            name='uncommon_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

```

## File: `core/migrations/0163_cardpacktype_card_pack_code.py`
- **File Size:** 405 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Card pack codes for card pack types (#156)

```
# Generated by Django 2.2 on 2024-07-30 15:38

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0162_auto_20240730_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpacktype',
            name='card_pack_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0164_add_season_start_end.py`
- **File Size:** 565 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Fix for start and end seasons (#154)

```
# Generated by Django 2.2 on 2024-07-29 13:21

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0163_cardpacktype_card_pack_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0165_nftbucket_players_group.py`
- **File Size:** 427 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding group type to the nft bucket

```
# Generated by Django 2.2 on 2024-07-31 14:34

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0164_add_season_start_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftbucket',
            name='players_group',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0166_nftbucket_opta_id.py`
- **File Size:** 424 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** import ids to nft bucket

```
# Generated by Django 2.2 on 2024-07-31 15:35

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0165_nftbucket_players_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftbucket',
            name='opta_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0167_auto_20240802_1405.py`
- **File Size:** 889 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add promotion, relegation ranges

```
# Generated by Django 2.2 on 2024-08-02 14:05

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0166_nftbucket_opta_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='promotion_max_range',
            field=models.FloatField(default=0.3),
        ),
        migrations.AddField(
            model_name='division',
            name='promotion_min_range',
            field=models.FloatField(default=0.2),
        ),
        migrations.AddField(
            model_name='division',
            name='relegation_max_range',
            field=models.FloatField(default=0.3),
        ),
        migrations.AddField(
            model_name='division',
            name='relegation_min_range',
            field=models.FloatField(default=0.2),
        ),
    ]

```

## File: `core/migrations/0168_auto_20240802_2242.py`
- **File Size:** 381 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Fix for name of the transaction field with the store assigned cardpack (#158)

```
# Generated by Django 2.2 on 2024-08-02 22:42

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0167_auto_20240802_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignedcardpack',
            old_name='transaction_id',
            new_name='transaction',
        ),
    ]

```

## File: `core/migrations/0169_auto_20240802_2350.py`
- **File Size:** 644 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** change transaction_id to store_transaction_id (#159)

```
# Generated by Django 2.2 on 2024-08-02 23:50

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0168_auto_20240802_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedcardpack',
            name='transaction',
        ),
        migrations.AddField(
            model_name='assignedcardpack',
            name='store_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.StoreProductTransactions'),
        ),
    ]

```

## File: `core/migrations/0170_auto_20240806_1411.py`
- **File Size:** 590 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add avarage rank and counter played matches

```
# Generated by Django 2.2 on 2024-08-06 14:11

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0169_auto_20240802_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergameweekhistory',
            name='week_average_rank',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usergameweekhistory',
            name='weekly_matches_played',
            field=models.IntegerField(default=0),
        ),
    ]

```

## File: `core/migrations/0171_auto_20240806_1857.py`
- **File Size:** 399 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix week_matches_played

```
# Generated by Django 2.2 on 2024-08-06 18:57

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0170_auto_20240806_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usergameweekhistory',
            old_name='weekly_matches_played',
            new_name='week_matches_played',
        ),
    ]

```

## File: `core/migrations/0172_auto_20240809_1632.py`
- **File Size:** 430 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add unique wallet address to user

```
# Generated by Django 2.2 on 2024-08-09 16:32

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0171_auto_20240806_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]

```

## File: `core/migrations/0173_appinbox.py`
- **File Size:** 1123 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add the App Inbox table

```
# Generated by Django 2.2 on 2024-08-13 01:40

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0172_auto_20240809_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInbox',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'app_inbox',
            },
        ),
    ]

```

## File: `core/migrations/0174_appinbox_user_id.py`
- **File Size:** 380 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add user to the app inbox

```
# Generated by Django 2.2 on 2024-08-13 01:48

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0173_appinbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinbox',
            name='user_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]

```

## File: `core/migrations/0175_auto_20240813_0157.py`
- **File Size:** 446 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add user to the app inbox

```
# Generated by Django 2.2 on 2024-08-13 01:57

import core.models
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0174_appinbox_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinbox',
            name='user_id',
            field=models.UUIDField(blank=True, null=True, verbose_name=core.models.CustomUser),
        ),
    ]

```

## File: `core/migrations/0176_auto_20240813_1633.py`
- **File Size:** 748 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Cahnging the app inbox model

```
# Generated by Django 2.2 on 2024-08-13 16:33

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0175_auto_20240813_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appinbox',
            name='user_id',
        ),
        migrations.AddField(
            model_name='appinbox',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appinbox',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser'),
        ),
    ]

```

## File: `core/migrations/0177_auto_20240815_1507.py`
- **File Size:** 705 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add fields to game events

```
# Generated by Django 2.2 on 2024-08-15 15:07

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0176_auto_20240813_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameevent',
            name='boost_multiplier',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='gameevent',
            name='nft_image',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='gameevent',
            name='nft_multiplier',
            field=models.FloatField(default=1.0),
        ),
    ]

```

## File: `core/migrations/0178_assignedcardpack_refunded.py`
- **File Size:** 394 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add refunded logic to avoid nft mints and look for transaction id if not then clear the carpdack

```
# Generated by Django 2.2 on 2024-08-19 15:52

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0177_auto_20240815_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedcardpack',
            name='refunded',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0179_auto_20240827_1851.py`
- **File Size:** 3250 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix division reward migration

```
# Generated by Django 2.2 on 2024-08-27 18:51

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0178_assignedcardpack_refunded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('credits', models.FloatField(default=0)),
                ('game_token', models.FloatField(default=0)),
                ('lapt_token', models.FloatField(default=0)),
                ('event_tickets', models.IntegerField(default=0)),
                ('ball', models.IntegerField(default=0)),
                ('signed_ball', models.IntegerField(default=0)),
                ('shirt', models.IntegerField(default=0)),
                ('signed_shirt', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'rewards',
            },
        ),
        migrations.RemoveField(
            model_name='divisionreward',
            name='amount',
        ),
        migrations.AddField(
            model_name='matchreward',
            name='balls',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='event',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='game',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='lapt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='shirts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='signed_balls',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='signed_shirts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactions',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='object_type',
            field=models.CharField(choices=[('v', 'virtual'), ('c', 'crypto'), ('n', 'nft'), ('g', 'game'), ('l', 'lapt'), ('e', 'event_ticket'), ('m', 'merch'), ('b', 'ball'), ('a', 'signed_ball'), ('s', 'shirt'), ('h', 'signed_shirt')], default='v', max_length=1),
        ),
        migrations.AddField(
            model_name='divisionreward',
            name='reward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Rewards'),
        ),
    ]

```

## File: `core/migrations/0180_gameweekdivision.py`
- **File Size:** 974 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix migration ref

```
# Generated by Django 2.2 on 2024-08-28 19:59

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0179_auto_20240827_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameWeekDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('promotion_count', models.FloatField()),
                ('relegation_count', models.FloatField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Division')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.GameWeek')),
            ],
            options={
                'db_table': 'game_week_divisions',
            },
        ),
    ]

```

## File: `core/migrations/0181_auto_20240903_1225.py`
- **File Size:** 407 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add the migrations

```
# Generated by Django 2.2 on 2024-09-03 12:25

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0180_gameweekdivision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

```

## File: `core/migrations/0182_auto_20240903_2211.py`
- **File Size:** 812 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding rewards to app inbox

```
# Generated by Django 2.2 on 2024-09-03 22:11

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0181_auto_20240903_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinbox',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appinbox',
            name='clamed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appinbox',
            name='reward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Rewards'),
        ),
    ]

```

## File: `core/migrations/0183_auto_20240905_1623.py`
- **File Size:** 1215 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add fields to user, transactions and app inbox / change abi

```
# Generated by Django 2.2 on 2024-09-05 16:23

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0182_auto_20240903_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinbox',
            name='clear',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appinbox',
            name='game_week_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.GameWeek'),
        ),
        migrations.AddField(
            model_name='appinbox',
            name='match_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Match'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='real_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]

```

## File: `core/migrations/0184_action_nft_category.py`
- **File Size:** 625 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** added nft-category to action

```
# Generated by Django 2.2 on 2024-09-20 13:45

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0183_auto_20240905_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='nft_category',
            field=models.TextField(blank=True, choices=[('distribution', 'distribution'), ('shooting', 'shooting'), ('passing', 'passing'), ('dribbling', 'dribbling'), ('defence', 'defence'), ('disciplinary', 'disciplinary'), ('stopping', 'stopping'), ('claiming', 'claiming')], null=True),
        ),
    ]

```

## File: `core/migrations/0185_auto_20240925_1343.py`
- **File Size:** 1650 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Adding pack rewards to divisions and match structure

```
# Generated by Django 2.2 on 2024-09-25 13:43

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0184_action_nft_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchreward',
            name='kickoff_pack_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='kickoff_pack_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='kickoff_pack_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rewards',
            name='kickoff_pack_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rewards',
            name='kickoff_pack_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rewards',
            name='kickoff_pack_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='object_type',
            field=models.CharField(choices=[('v', 'virtual'), ('c', 'crypto'), ('n', 'nft'), ('g', 'game'), ('l', 'lapt'), ('e', 'event_ticket'), ('m', 'merch'), ('b', 'ball'), ('a', 'signed_ball'), ('s', 'shirt'), ('h', 'signed_shirt'), ('1', 'kickoff_pack_1'), ('2', 'kickoff_pack_2'), ('3', 'kickoff_pack_3')], default='v', max_length=1),
        ),
    ]

```

## File: `core/migrations/0186_appinbox_game.py`
- **File Size:** 482 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** adding game_id to the app inbox

```
# Generated by Django 2.2 on 2024-09-27 14:49

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0185_auto_20240925_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinbox',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Game'),
        ),
    ]

```

## File: `core/migrations/0187_auto_20241010_1600.py`
- **File Size:** 833 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new cardpack guarantees

```
# Generated by Django 2.2 on 2024-10-10 16:00

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0186_appinbox_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpacktype',
            name='rarities',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='cardpacktype',
            name='star_ratings',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]

```

## File: `core/migrations/0188_customuser_referral_bonus_used.py`
- **File Size:** 422 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** added referral_bonus_used field

```
# Generated by Django 2.2 on 2024-10-13 18:41

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0187_auto_20241010_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='referral_bonus_used',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

```

## File: `core/migrations/0189_auto_20241014_1412.py`
- **File Size:** 1727 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Add new packs

```
# Generated by Django 2.2 on 2024-10-14 14:12

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0188_customuser_referral_bonus_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchreward',
            name='season_pack_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='season_pack_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchreward',
            name='season_pack_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rewards',
            name='season_pack_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rewards',
            name='season_pack_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rewards',
            name='season_pack_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='object_type',
            field=models.CharField(choices=[('v', 'virtual'), ('c', 'crypto'), ('n', 'nft'), ('g', 'game'), ('l', 'lapt'), ('e', 'event_ticket'), ('m', 'merch'), ('b', 'ball'), ('a', 'signed_ball'), ('s', 'shirt'), ('h', 'signed_shirt'), ('1', 'kickoff_pack_1'), ('2', 'kickoff_pack_2'), ('3', 'kickoff_pack_3'), ('4', 'season_pack_1'), ('5', 'season_pack_2'), ('6', 'season_pack_3')], default='v', max_length=1),
        ),
    ]

```

## File: `core/migrations/0190_pushnotification.py`
- **File Size:** 1267 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** New notifications models

```
# Generated by Django 2.2 on 2024-10-16 15:21

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0189_auto_20241014_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('match', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'push_notifications',
            },
        ),
    ]

```

## File: `core/migrations/0191_cardpacktype_collection.py`
- **File Size:** 411 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** notification limit and cardpack collection field

```
# Generated by Django 2.2 on 2024-10-16 19:22

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0190_pushnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpacktype',
            name='collection',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

```

## File: `core/migrations/0192_badges_banner_frames_userbadges_userbanners_userframes.py`
- **File Size:** 4824 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix migrations

```
# Generated by Django 2.2 on 2024-10-22 18:26

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0191_cardpacktype_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('points', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'badges',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('points', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'banners',
            },
        ),
        migrations.CreateModel(
            name='Frames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('points', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'frames',
            },
        ),
        migrations.CreateModel(
            name='UserFrames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Frames')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_frames',
            },
        ),
        migrations.CreateModel(
            name='UserBanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Banner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_banners',
            },
        ),
        migrations.CreateModel(
            name='UserBadges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Badges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_badges',
            },
        ),
    ]

```

## File: `core/migrations/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `core/models.py`
- **File Size:** 93363 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** selected to badges, banners and frames

```
import math
import os
import traceback
import uuid
from datetime import timedelta
from functools import lru_cache
from math import floor, ceil
from typing import Optional

from django.conf import settings
from django.db import models, transaction, connection, IntegrityError
from django.db.models import DO_NOTHING, Q
from django.utils import timezone
from django.db.models import Avg
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.serializers.json import DjangoJSONEncoder

from core import const
from core.const import TIER_CHOICES, TIER_NONE
from util.calc import get_rank_dict

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ImportModel(BaseModel):
    import_id = models.CharField(unique=True, null=True, max_length=15)

    class Meta:
        abstract = True

class V2ImportModel(BaseModel):
    import_id = models.CharField(unique=True, null=True, max_length=128)

    class Meta:
        abstract = True

class CustomUser(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=True, blank=True)
    password_hash = models.TextField(null=True, blank=True)
    email_verified = models.BooleanField(null=False, default=False)
    token_expiration = models.DateTimeField(null=True, blank=True)
    verification_token = models.CharField(null=True, blank=True, max_length=100)
    name = models.CharField(max_length=255, unique=True)
    firebase_id = models.CharField(max_length=50, null=True, blank=True)
    avatar_url = models.TextField(null=True, blank=True)
    balance = models.FloatField(default=0)
    paypal_email = models.CharField(null=True, blank=True, max_length=255)
    verified = models.BooleanField(null=False, default=False)
    referral_code = models.CharField(null=True, blank=True, max_length=10, unique=True)
    referrer = models.ForeignKey('CustomUser', null=True, on_delete=DO_NOTHING, blank=True)
    referral_bonus_used = models.BooleanField(null=True, blank=True, default=False)
    bonus_powerups = models.IntegerField(null=False, default=0, blank=True)
    follower_count = models.IntegerField(null=True, blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    games_played = models.IntegerField(null=True, blank=True)
    avg_points = models.IntegerField(null=True, blank=True)
    avg_rank = models.IntegerField(null=True, blank=True)
    avg_rank_percent = models.IntegerField(null=True, blank=True)
    name_changed = models.BooleanField(null=False, default=False)
    last_name_change = models.DateTimeField(null=True, blank=False)
    moderator = models.BooleanField(null=False, default=False)
    premium = models.BooleanField(null=False, default=False)
    influencer = models.BooleanField(null=False, default=False)
    subscription = models.ForeignKey('Subscription', null=True, blank=True, on_delete=DO_NOTHING)
    subscription_tier = models.IntegerField(null=False, blank=False, choices=TIER_CHOICES, default=TIER_NONE)
    wallet_address = models.CharField(null=True, blank=True, max_length=255, unique=True)
    finished_games = models.TextField(null=True, blank=True)
    divisions = models.ManyToManyField('Division', through='UserDivision')
    sequence_session_id = models.CharField(null=True, blank=True, max_length=255)
    real_name = models.CharField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        # empty name
        if not self.name:
            # get next sequence value
            self.name = 'Guest#{}'.format(self.get_next_user_index())
        super(CustomUser, self).save(*args, **kwargs)

    @staticmethod
    def get_next_user_index():
        query = """select nextval('user_guest_index');"""
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        return res[0]

    def is_authenticated(self):
        return True

    def calculate_stats(self):
        sql = """
select round(avg(match_leaderboard.position)) avg_rank,
       round(avg(match_leaderboard.score)) avg_points,
       ceil(avg(100 * match_leaderboard.position /
       (select count(*) from match_leaderboard ml2 where ml2.match_id = match_leaderboard.match_id))),
       count(1) games_played
  from match_leaderboard,
       games
 where match_leaderboard.game_id = games.id
   and games.user_id = %s
 group by games.user_id
        """

        with connection.cursor() as c:
            c.execute(sql, [self.pk])
            row = c.fetchone()

            if not row:
                return

            self.avg_rank = row[0]
            self.avg_points = row[1]
            self.avg_rank_percent = row[2]
            self.games_played = row[3]
            self.save(update_fields=['avg_rank', 'avg_points', 'avg_rank_percent', 'games_played'])

    def calculate_avg_rank(self):
        rank = MatchLeaderboard.objects.exclude(position__isnull=True). \
            filter(game__user=self).aggregate(Avg('position'))
        self.avg_rank = round(rank)
        self.save(update_fields=['avg_points'])

    def calculate_avg_rank_percent(self):
        query = """
select ml.position / (select count(*) from match_leaderboard ml2 where ml2.match_id = ml.match_id)
  from match_leaderboard ml
 where ml.user_id"""
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        self.avg_rank_percent = math.ceil(res[0] * 100)
        self.save(update_fields=['avg_rank_percent'])

    def update_premium(self):
        has_premium, subscription_tier = False, TIER_NONE
        try:
            # find manual subscription first
            ms = ManualSubscription.objects.filter(user=self, expires_at__gt=timezone.now()).get()
            has_premium = True
            subscription_tier = ms.tier
        except ManualSubscription.DoesNotExist:
            if self.subscription is not None and self.subscription.active:
                has_premium = True
                subscription_tier = self.subscription.tier

        if self.premium != has_premium or self.subscription_tier != subscription_tier:
            self.premium = has_premium
            self.subscription_tier = subscription_tier
            self.save(update_fields=['premium', 'subscription_tier', 'updated_at'])

    def subscribe_to_leaderboard(self, leaderboard):
        UserLeaderboardSubscription.objects.get_or_create(user=self, leaderboard=leaderboard)

    def unsubscribe_from_leaderboard(self, leaderboard):
        UserLeaderboardSubscription.objects.filter(user=self, leaderboard=leaderboard).delete()

    def get_subscribed_leaderboards(self):
        return Leaderboard.objects.filter(user_subscriptions__user=self)

    def division_in_game_week(self, game_week):
        return Division.objects.filter(
            Q(userdivision__user=self) & Q(userdivision__game_week=game_week)
        ).distinct().first()

    def last_division(self):
        return Division.objects.filter(
            Q(userdivision__user=self)
        ).order_by('-userdivision__join_date').first()

    def __str__(self):
        return '{} ({})'.format(self.name, self.pk)

    class Meta:
        db_table = 'users'

class Transactions(BaseModel):
    VIRTUAL = 'v'  # virtual currency
    CRYPTO = 'c'  # crypto currency
    NFT = 'n'  # NFT token
    GAME = 'g'  # game currency
    LAPT = 'l'  # Lapt token
    EVENT_TICKET = 'e'  # Event ticket
    MERCH = 'm'  # Merchandise
    BALL = 'b'  # Ball
    SIGNED_BALL = 'a'  # Signed Ball
    SHIRT = 's'  # Shirt
    SIGNED_SHIRT = 'h'  # Signed Shirt
    KICKOFF_PACK_1 = '1'  # Kickoff Pack 1
    KICKOFF_PACK_2 = '2'  # Kickoff Pack 1
    KICKOFF_PACK_3 = '3'  # Kickoff Pack 1
    SEASON_PACK_1 = '4'  # Season Pack 1
    SEASON_PACK_2 = '5'  # Season Pack 2
    SEASON_PACK_3 = '6'  # Season Pack 3

    OBJECT_TYPE = (
        (VIRTUAL, 'virtual'),
        (CRYPTO, 'crypto'),
        (NFT, 'nft'),
        (GAME, 'game'),
        (LAPT, 'lapt'),
        (EVENT_TICKET, 'event_ticket'),
        (MERCH, 'merch'),
        (BALL, 'ball'),
        (SIGNED_BALL, 'signed_ball'),
        (SHIRT, 'shirt'),
        (SIGNED_SHIRT, 'signed_shirt'),
        (KICKOFF_PACK_1, 'kickoff_pack_1'),
        (KICKOFF_PACK_2, 'kickoff_pack_2'),
        (KICKOFF_PACK_3, 'kickoff_pack_3'),
        (SEASON_PACK_1, 'season_pack_1'),
        (SEASON_PACK_2, 'season_pack_2'),
        (SEASON_PACK_3, 'season_pack_3'),
    )
    user = models.ForeignKey(CustomUser, on_delete=DO_NOTHING)
    amount = models.FloatField(default=0)
    quantity = models.BigIntegerField(null=False, blank=False, default=0)
    object_type = models.CharField(choices=OBJECT_TYPE, max_length=1, default=VIRTUAL)
    blockchain_uuid = models.TextField(null=True, blank=True)
    order = models.ForeignKey('Order', null=True, blank=True, on_delete=DO_NOTHING)
    match = models.ForeignKey('Match', null=True, blank=True, on_delete=DO_NOTHING)
    week = models.ForeignKey('GameWeek', null=True, blank=True, on_delete=DO_NOTHING)
    text = models.TextField(null=True, blank=True)
    delivered = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    class Meta:
        db_table = 'transactions'

class OptaFeed(models.Model):
    STATUS_RECEIVED = 1
    STATUS_PROCESSING = 2
    STATUS_PROCESSED = 3
    STATUS_ERROR = 4

    STATUSES = (
        (STATUS_RECEIVED, 'Received'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_PROCESSED, 'Processed'),
        (STATUS_ERROR, 'Error'),
    )

    FEED_TYPE_F1 = 'F1'
    FEED_TYPE_F24 = 'F24'
    FEED_TYPE_F40 = 'F40'

    FEED_TYPES = (
        (FEED_TYPE_F1, 'F1'),
        (FEED_TYPE_F24, 'F24'),
        (FEED_TYPE_F40, 'F40'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    processing_started = models.DateTimeField(null=True)
    processing_ended = models.DateTimeField(null=True)
    feed_object_id = models.CharField(unique=True, max_length=50)
    feed_hash = models.TextField(null=True)
    feed_type = models.CharField(choices=FEED_TYPES, max_length=3)
    status = models.IntegerField(choices=STATUSES, default=STATUS_RECEIVED)
    headers = models.TextField()
    match = models.ForeignKey('Match', null=True, on_delete=DO_NOTHING)

    class Meta:
        db_table = 'opta_feeds'

class OptaFeedItem(BaseModel):
    match = models.ForeignKey('Match', on_delete=DO_NOTHING)
    unique_id = models.CharField(max_length=50)
    event_id = models.CharField(max_length=50)
    current_version = models.ForeignKey('OptaFeedItemVersion', null=True, on_delete=DO_NOTHING)

    class Meta:
        db_table = 'opta_feed_items'
        unique_together = ('match', 'unique_id', 'event_id',)

class OptaFeedItemVersion(BaseModel):
    ACTIVE = 1
    NO_DIFF = 2
    PARTIAL_CANCEL = 3
    FULL_CANCEL = 4

    STATUSES = (
        (ACTIVE, 'Active'),
        (NO_DIFF, 'No Diff'),
        (PARTIAL_CANCEL, 'Partial Cancel'),
        (FULL_CANCEL, 'Full Cancel'),
    )

    item = models.ForeignKey('OptaFeedItem', on_delete=DO_NOTHING)
    status = models.IntegerField(choices=STATUSES)
    version = models.TextField()
    last_modified_at = models.DateTimeField()

    class Meta:
        db_table = 'opta_feed_item_versions'

class Country(V2ImportModel):
    name = models.TextField()
    iso = models.CharField(max_length=10, null=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.iso)

    class Meta:
        db_table = 'countries'

class Region(V2ImportModel):
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'

class Sport(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        db_table = 'sports'

class Team(V2ImportModel):
    name = models.TextField(blank=True)
    short_name = models.TextField(null=True, blank=True)
    abbr = models.CharField(max_length=5, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=DO_NOTHING)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=DO_NOTHING)
    crest_url = models.TextField(null=True, blank=True)
    ortec_selection_id = models.CharField(max_length=30, null=True, blank=True)
    opta_selection_id = models.CharField(max_length=30, null=True, blank=True)

    def get_display_name(self):
        if self.short_name:
            return self.short_name
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teams'

class Season(V2ImportModel):
    name = models.TextField()
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    # @classmethod
    # def current_season(cls):
    #     try:
    #         return cls.objects.filter(import_id=2024).get()
    #     except Season.DoesNotExist:
    #         return cls.objects.create(
    #             import_id=2024,
    #             name="2024"
    #         )

    class Meta:
        db_table = 'seasons'

class GameSeason(V2ImportModel):
    name = models.TextField()
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'game_seasons'

class CompetitionConfig(V2ImportModel):
    name = models.TextField()
    filter = models.TextField()  # in case of opta, is comeptitionCode
    enabled = models.BooleanField(default=False)
    related_competition = models.ForeignKey('Competition', null=True, on_delete=DO_NOTHING)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competition_config'

class Competition(V2ImportModel):
    name = models.TextField()
    code = models.CharField(max_length=50)
    short_name = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=True)
    config = models.ForeignKey('CompetitionConfig', null=True, on_delete=DO_NOTHING)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    # editions = HAVE RELATED EDITIONS HERE

    def get_display_name(self):
        if self.short_name:
            return self.short_name
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competitions'

class CompetitionEdition(V2ImportModel):
    name = models.TextField()
    competition = models.ForeignKey('Competition', on_delete=DO_NOTHING)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'competition_editions'

class CompetitionPhase(V2ImportModel):
    name = models.TextField()
    competition_edition = models.ForeignKey('CompetitionEdition', on_delete=DO_NOTHING)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'competition_phases'

class SeasonCompetitionMember(BaseModel):
    competition = models.ForeignKey(Competition, null=False, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    season = models.ForeignKey(Season, null=False, on_delete=DO_NOTHING)

    class Meta:
        unique_together = ('competition', 'team', 'season')
        db_table = 'season_competition_members'

class Player(V2ImportModel):
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    full_name = models.TextField(null=True, blank=True)
    nick_name = models.TextField(null=True, blank=True)
    avg_score = models.FloatField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    normalized_name = models.TextField(null=True, blank=True)
    soccer_wiki_player = models.ForeignKey('soccer_wiki.SoccerWikiPlayer', null=True, blank=True, on_delete=DO_NOTHING)

    def calculate_normalized_name(self):
        # Calculate full_name
        full_name = ('' if not self.first_name else self.first_name) + ' ' + \
                    ('' if not self.last_name else self.last_name)

        # Set the normalized_name based on nick_name or use full_name if nick_name contains abbreviation
        if self.nick_name and not any(char + '.' in self.nick_name for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            return self.nick_name
        else:
            return full_name.strip()

    def update_avg_score(self):
        self.avg_score = self.calculate_avg_score()
        self.save(update_fields=['avg_score'])

    def calculate_avg_score(self):
        # select match players for this player
        total_time, total_score, match_cnt = 0, 0, 0

        mp_qs = MatchPlayer.objects.filter(player=self, match__match_time__gt=timezone.now() - timedelta(days=180)). \
            exclude(Q(played_seconds__isnull=True) | Q(score__isnull=True)). \
            order_by('-match__match_time')

        for mp in mp_qs[:50]:
            if mp.played_seconds:
                total_time += mp.played_seconds
                total_score += mp.score
                match_cnt += 1

                # reach required amount of points
                if total_time >= (450 * 60):
                    # calculate avg score, and then normalize it to 90 min
                    avg_score = total_score / match_cnt
                    norm_avg_score = avg_score / ((total_time / match_cnt) / (90 * 60))

                    return round(norm_avg_score, 1)

        # goal is not reached
        return None

    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return ""

    def save(self, *args, **kwargs):
            # Calculate and set the full_name if not already set
            if not self.full_name:
                self.full_name = ('' if not self.first_name else self.first_name) + ' ' + \
                                ('' if not self.last_name else self.last_name)

            # Set the normalized_name
            self.normalized_name = self.calculate_normalized_name()

            super(Player, self).save(*args, **kwargs)

    class Meta:
        db_table = 'players'

class SeasonTeamPlayer(BaseModel):
    season = models.ForeignKey(Season, null=False, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.CharField(choices=const.POSITIONS, max_length=1, null=True)
    jersey_number = models.IntegerField(null=True)

    class Meta:
        unique_together = ('player', 'team', 'season')
        index_together = [
            ('player', 'team', 'season'),
        ]
        db_table = 'season_team_players'

class SelectionTeamPlayer(BaseModel):
    selection_id = models.CharField(max_length=30, null=False, blank=False)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.CharField(choices=const.POSITIONS, max_length=1, null=True)
    jersey_number = models.IntegerField(null=True)

    class Meta:
        unique_together = ('selection_id', 'player',)
        index_together = ('selection_id', 'player',)
        db_table = 'selection_team_players'

class MatchDay(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'match_days'

class Match(V2ImportModel):
    MATCH_TYPE_UNKNOWN = 0
    MATCH_TYPE_FREE = 1
    MATCH_TYPE_CASH = 2
    MATCH_TYPE_CASH_PLUS = 3

    MATCH_TYPES = (
        (MATCH_TYPE_UNKNOWN, 'Unknown'),
        (MATCH_TYPE_FREE, 'Free'),
        (MATCH_TYPE_CASH, 'Cash'),
        (MATCH_TYPE_CASH_PLUS, 'Cash Plus'),
    )

    competition = models.ForeignKey(Competition, null=False, on_delete=DO_NOTHING)
    edition = models.ForeignKey(CompetitionEdition, null=True, on_delete=DO_NOTHING)
    season = models.ForeignKey(Season, null=False, on_delete=DO_NOTHING)
    status = models.CharField(choices=const.MATCH_STATUSES, null=False, default=const.MATCH_STATUS_WAITING, max_length=1)
    period = models.CharField(choices=const.MATCH_PERIODS, null=False, default=const.MATCH_PERIOD_PREGAME, max_length=3)
    match_type = models.IntegerField(choices=MATCH_TYPES, default=MATCH_TYPE_UNKNOWN, db_index=True)
    has_lineups = models.BooleanField(default=False)
    home_team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING, related_name='home_team')
    away_team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING, related_name='away_team')
    home_team_selection_id = models.CharField(max_length=30, null=True, blank=True)
    away_team_selection_id = models.CharField(max_length=30, null=True, blank=True)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    last_processed_id = models.CharField(null=True, blank=True, max_length=15)
    match_time = models.DateTimeField(null=False)
    match_end = models.DateTimeField(null=True, blank=True)
    f_start = models.DateTimeField(null=True, blank=True)
    f_end = models.DateTimeField(null=True, blank=True)
    s_start = models.DateTimeField(null=True, blank=True)
    s_end = models.DateTimeField(null=True, blank=True)
    x1_start = models.DateTimeField(null=True, blank=True)
    x1_end = models.DateTimeField(null=True, blank=True)
    x2_start = models.DateTimeField(null=True, blank=True)
    x2_end = models.DateTimeField(null=True, blank=True)
    p_start = models.DateTimeField(null=True, blank=True)
    p_end = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    simulation_from_match = models.ForeignKey('self', null=True, blank=True, on_delete=DO_NOTHING)
    rewarded = models.BooleanField(null=False, blank=True, default=False)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    match_day = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.CASCADE, related_name='matches')
    week = models.IntegerField(default=0)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    enabled = models.BooleanField(default=True)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        super(Match, self).save(*args, **kwargs)
        self.set_up_default_rewards()

    def set_up_default_rewards(self):
        if not MatchReward.objects.filter(match=self).exists():
            rewards_instances = [
                MatchReward(min_position=1, max_position=1, amount=600, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0,match=self),
                MatchReward(min_position=2, max_position=2, amount=300, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=3, max_position=3, amount=200, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=4, max_position=10, amount=100, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=11, max_position=20, amount=50, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=21, max_position=None, amount=30, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
            ]
            MatchReward.objects.bulk_create(rewards_instances)

    def create_simulation(self, duration):
        events = MatchEvent.objects.filter(match=self).order_by('match_event_id')

        base_inc = duration.total_seconds() / len(events) if len(events) > 0 else 0

        with transaction.atomic():
            now = timezone.now()
            simulation = Match.objects.create(
                competition=self.competition,
                season=self.season,
                home_team=self.home_team,
                away_team=self.away_team,
                match_time=now,
                simulation_from_match=self,
                match_type=Match.MATCH_TYPE_FREE,
                import_id='simulation-' + str(uuid.uuid4()) + "-" + self.import_id,
                home_team_selection_id=self.home_team.import_id,
                away_team_selection_id=self.away_team.import_id,
                sport_id=self.sport_id
            )

            # init match players
            simulation.sync_match_players(True)

            delay_time = timedelta(seconds=60)

            # insert simulation plan
            for i in range(len(events)):
                # calculate new timestamp
                new_timestamp = now + delay_time + timedelta(seconds=base_inc * i)
                MatchEventSimulation.objects.create(
                    match_event=events[i],
                    match=simulation,
                    timestamp=new_timestamp,
                )

        return simulation

    def get_team_id_by_selection_id(self, selection_id):
        if str(selection_id) == str(self.home_team_selection_id):
            return self.home_team_id
        elif str(selection_id) == str(self.away_team_selection_id):
            return self.away_team_id
        else:
            raise Exception("cannot find team {}, home_team is {} - {}, away_team is {} - {}.".format(
                selection_id,
                self.home_team_selection_id,
                self.home_team_id,
                self.away_team_selection_id,
                self.away_team_id,
            ))

    def insert_missing_match_players(self):
        team_players = SelectionTeamPlayer.objects.select_related('player').filter(
            Q(selection_id=self.home_team_selection_id) | Q(selection_id=self.away_team_selection_id)
        )
        for tp in team_players:
            team_id = self.get_team_id_by_selection_id(tp.selection_id)
            try:
                mp = MatchPlayer.objects.filter(
                    match_id=self.id,
                    player_id=tp.player.id,
                    team_id=team_id,
                ).get()
                mp.position = tp.position
                mp.jersey_number = tp.jersey_number
                mp.save(update_fields=['position', 'jersey_number'])
            except MatchPlayer.DoesNotExist:
                try:
                    MatchPlayer.objects.create(
                        match_id=self.pk,
                        player_id=tp.player.id,
                        team_id=team_id,
                        position=tp.position,
                        jersey_number=tp.jersey_number,
                        from_lineups=False
                    )
                except IntegrityError:
                    print(f"[ERR] [insert_missing_match_players] cannot create match player: {traceback.format_exc}")
                    pass

    def update_match_players_score(self, sync_avg_score=False):
        match_players = MatchPlayer.objects.select_related('player').filter(match=self)

        if sync_avg_score:
            # update avg scores for all players
            for mp in match_players:
                mp.player.update_avg_score()

        for mp in match_players:
            # propagate value from player
            mp.avg_score = mp.player.avg_score
            mp.save(update_fields=['avg_score'])

    def update_match_players_star_flag(self):
        match_players = MatchPlayer.objects.filter(match=self)
        score_ranks = get_rank_dict([mp.avg_score for mp in match_players if mp.avg_score])

        for mp in match_players:
            rank = score_ranks.get(mp.avg_score, 0)

            # only top N of players are star players
            is_star = rank <= settings.STAR_PLAYERS_TOP if rank > 0 else False

            # propagate value from player
            mp.is_star = is_star
            mp.save(update_fields=['is_star'])

    def sync_match_players(self, sync_avg_score=False):
        with transaction.atomic():
            # lock match
            m = Match.objects.select_for_update().get(pk=self.pk)

            # ignore matches in other than 'waiting' and 'unknown' states
            if m.status not in (const.MATCH_STATUS_WAITING, const.MATCH_STATUS_UNKNOWN, const.MATCH_STATUS_EMPTY):
                return

            should_update_star = True

            # we shouldn't update `is_star` flag if less than 3 days left
            # and is_star flag is already set
            if (m.match_time - timedelta(days=3)) < timezone.now() and \
                    MatchPlayer.objects.filter(match=m.pk, is_star=True).count() > 0:
                should_update_star = False

            self.insert_missing_match_players()
            self.update_match_players_score(sync_avg_score)

            if should_update_star:
                self.update_match_players_star_flag()

    def is_opta_selection_from_match(self, value):
        return self.is_opta_home_selection_from_match(value) or self.is_opta_away_selection_from_match(value)

    def is_opta_home_selection_from_match(self, value):
        return str(value) == self.home_team_selection_id

    def is_opta_away_selection_from_match(self, value):
        return str(value) == self.away_team_selection_id

    def get_import_id(self) -> str:
        if self.simulation_from_match is not None:
            return self.simulation_from_match.get_import_id()
        return self.import_id

    def __str__(self):
        return f"{'[SIM] ' if self.simulation_from_match else ''}{self.home_team} vs {self.away_team} on {self.match_time.strftime('%Y-%m-%d %H:%M:%S')} - import_id: {self.get_import_id()} - id: {self.id}"

    class Meta:
        db_table = 'matches'
        verbose_name_plural = 'Matches'

class MatchReward(models.Model):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    position = models.IntegerField(null=True, blank=True)  # deprecated
    min_position = models.IntegerField(default=1)
    max_position = models.IntegerField(null=True, blank=True)
    amount = models.FloatField()
    game = models.FloatField(default=0)
    lapt = models.FloatField(default=0)
    event = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)  # For merchandise
    signed_balls = models.IntegerField(default=0)  # For merchandise
    shirts = models.IntegerField(default=0)  # For merchandise
    signed_shirts = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_1 = models.IntegerField(default=0)
    kickoff_pack_2 = models.IntegerField(default=0)
    kickoff_pack_3 = models.IntegerField(default=0)
    season_pack_1 = models.IntegerField(default=0)
    season_pack_2 = models.IntegerField(default=0)
    season_pack_3 = models.IntegerField(default=0)

    class Meta:
        db_table = 'match_rewards'
        unique_together = ('match', 'min_position', 'max_position')

class MatchEvent(models.Model):
    ACTIVE = 1
    CANCELLED = 2
    IGNORED = 3

    STATUSES = (
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
        (IGNORED, 'Ignored'),
    )

    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(null=False)
    team = models.ForeignKey(Team, null=True, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=True, on_delete=DO_NOTHING)
    type = models.IntegerField(null=False)
    points = models.FloatField(null=True)
    payload = models.TextField(null=True)
    minute = models.IntegerField(null=False)
    second = models.IntegerField(null=False)
    x = models.FloatField(null=False, default=0)
    y = models.FloatField(null=False, default=0)
    match_event_id = models.IntegerField(null=False)
    provider_id = models.CharField(max_length=30)
    opta_feed_item_version = models.ForeignKey(OptaFeedItemVersion, null=True, on_delete=DO_NOTHING)
    status = models.IntegerField(choices=STATUSES, default=ACTIVE)
    period = models.IntegerField(default=None, null=True, blank=True)
    has_real_timestamp = models.BooleanField(default=False)

    class Meta:
        db_table = 'match_events'
        unique_together = ('match', 'match_event_id')

class MatchEventSimulation(models.Model):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    match_event = models.ForeignKey(MatchEvent, null=False, on_delete=DO_NOTHING)
    timestamp = models.DateTimeField(null=False, db_index=True)
    simulated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'match_event_simulations'
        unique_together = ('match', 'match_event')

class MatchPlayer(BaseModel):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.CharField(choices=const.POSITIONS, max_length=1, null=True)
    jersey_number = models.IntegerField(null=True)
    from_lineups = models.BooleanField(default=False)
    is_star = models.BooleanField(default=False)
    score = models.FloatField(null=True)
    played_seconds = models.IntegerField(null=True)
    avg_score = models.FloatField(null=True)

    class Meta:
        db_table = 'match_players'
        unique_together = ('match', 'player',)

class MatchHeadline(models.Model):
    SCREEN_TYPE_LOBBY = 1
    SCREEN_TYPE_GAMEPLAY = 2
    SCREEN_TYPE_FULLTIME = 3

    SCREEN_TYPES = (
        (SCREEN_TYPE_LOBBY, 'lobby'),
        (SCREEN_TYPE_GAMEPLAY, 'gameplay'),
        (SCREEN_TYPE_FULLTIME, 'fulltime'),
    )

    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.TextField()
    type = models.CharField(max_length=30)
    screen_type = models.IntegerField(choices=SCREEN_TYPES)
    image_type = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'match_headlines'

class Game(BaseModel):
    STATUS_WAITING = 'w'
    STATUS_GAMEPLAY = 'g'
    STATUS_FINISHED = 'f'

    STATUS_CHOICES = (
        (STATUS_WAITING, 'w'),
        (STATUS_GAMEPLAY, 'g'),
        (STATUS_FINISHED, 'f'),
    )

    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING)
    status = models.CharField(max_length=1, default=STATUS_WAITING)
    version = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    premium = models.BooleanField(default=False)
    subscription_tier = models.IntegerField(null=False, blank=False, choices=TIER_CHOICES, default=TIER_NONE)
    num = models.IntegerField(null=True, blank=True)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    notified = models.BooleanField(default=False)

    class Meta:
        db_table = 'games'
        unique_together = (('match', 'user'), ('user', 'num'))

class GamePick(BaseModel):
    ended_at = models.DateTimeField(null=True)
    game = models.ForeignKey(Game, null=False, on_delete=DO_NOTHING, related_name='picks')
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.IntegerField(null=False)
    version = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    ended_minute = models.IntegerField(null=True)
    ended_second = models.IntegerField(null=True)
    user_swapped = models.BooleanField(default=True)
    assigned_player = models.ForeignKey('AssignedPlayer', null=True, on_delete=DO_NOTHING, related_name='assigned_player')

    class Meta:
        db_table = 'game_picks'

class GameEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game, null=False, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    game_pick = models.ForeignKey(GamePick, null=False, on_delete=DO_NOTHING)
    powerup = models.ForeignKey('GamePowerUp', null=True, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    minute = models.IntegerField(null=False)
    second = models.IntegerField(null=False)
    type = models.IntegerField(null=False)
    score = models.FloatField(default=0)
    initial_score = models.FloatField(default=0)
    match_event = models.ForeignKey(MatchEvent, null=True, on_delete=DO_NOTHING)
    nft_multiplier = models.FloatField(default=1.0)
    boost_multiplier = models.FloatField(default=1.0)
    nft_image = models.TextField(null=True)

    class Meta:
        db_table = 'game_events'

class GamePowerUp(BaseModel):
    ended_at = models.DateTimeField(null=True)
    powerup = models.ForeignKey('PowerUp', on_delete=DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=DO_NOTHING)
    position = models.IntegerField()
    duration = models.IntegerField()
    multiplier = models.FloatField()
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    bonus = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'game_powerups'

class LeaderboardType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'leaderboard_types'

class Division(BaseModel):
    name = models.CharField(max_length=255)
    tier = models.IntegerField()
    percentage = models.FloatField(default=0.01)
    relegation_min_range = models.FloatField(default=0.2)
    relegation_max_range = models.FloatField(default=0.3)
    promotion_min_range = models.FloatField(default=0.2)
    promotion_max_range = models.FloatField(default=0.3)

    def __str__(self):
        return f"Division {self.tier}"

    class Meta:
        db_table = 'divisions'

class MatchLeaderboard(models.Model):
    match = models.ForeignKey(Match, on_delete=DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=DO_NOTHING)
    score = models.FloatField(null=True)
    position = models.IntegerField(null=True)
    division = models.ForeignKey(Division, null=True, blank=True, on_delete=models.DO_NOTHING)
    leaderboard_type = models.ForeignKey(LeaderboardType, null=True, blank=True, on_delete=models.DO_NOTHING)
    transaction = models.ForeignKey('Transactions', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'match_leaderboard'

class MatchEventProcessor(models.Model):
    TYPE_POINTS = 1
    TYPE_SYSTEM = 2

    TYPES = (
        (TYPE_POINTS, 'points'),
        (TYPE_SYSTEM, 'system'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    type = models.IntegerField(choices=TYPES)
    last_processed_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'match_event_processors'
        unique_together = ('match', 'type',)

class Action(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    score = models.FloatField(null=False)
    ordering = models.IntegerField()
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    category = models.TextField(null=True)
    nft_category = models.TextField(null=True, blank=True, choices=const.NFT_CATEGORIES)
    icon = models.TextField(null=True)

    @staticmethod
    @lru_cache()
    def get_name_by_id(action_id):
        try:
            action = Action.objects.get(pk=action_id)
            return action.name
        except Action.DoesNotExist:
            return ""

    @staticmethod
    @lru_cache()
    def get_score_by_id(action_id):
        try:
            action = Action.objects.get(pk=action_id)
            return action.score
        except Action.DoesNotExist:
            return 0

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'actions'

class PowerUp(models.Model):
    TYPE_EVENT = 1
    TYPE_GAME = 2
    TYPES = (
        (TYPE_EVENT, 'event'),
        (TYPE_GAME, 'game'), # Means that it's applied to the whole game/match
    )
    name = models.TextField(null=False)
    description = models.TextField(null=True)
    icon_url = models.TextField(null=True)
    duration = models.IntegerField(null=False, help_text='duration in seconds')
    multiplier = models.FloatField(null=False)
    cost = models.FloatField(null=False, default=0.0)
    type = models.IntegerField(choices=TYPES, null=True, default=TYPE_EVENT)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    enabled = models.BooleanField(null=False, blank=False, default=False)
    conditions = JSONField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powerups'

class PowerUpAction(models.Model):
    action = models.ForeignKey(Action, null=False, on_delete=DO_NOTHING)
    powerup = models.ForeignKey(PowerUp, null=False, on_delete=DO_NOTHING)
    ordering = models.IntegerField()

    class Meta:
        db_table = 'powerup_actions'

class MatchNotification(BaseModel):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    user = models.ForeignKey(CustomUser, null=True, on_delete=DO_NOTHING)
    type = models.IntegerField()

    class Meta:
        db_table = 'match_notifications'

class Follower(models.Model):
    from_user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING, related_name='followers')
    to_user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING, related_name='followings')

    class Meta:
        db_table = 'followers'
        unique_together = ('from_user', 'to_user',)

class BanPenalty(models.Model):
    user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING, related_name='penalties')
    start_time = models.DateTimeField(null=False, blank=False, default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True, help_text='Empty end time means permanent ban')
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.end_time:
            return 'Ban at period {} - {}'.format(self.start_time, self.end_time)
        else:
            return 'Permanent ban from {}'.format(self.start_time)

    class Meta:
        db_table = 'ban_penalties'

class Subscription(models.Model):
    user_id = models.TextField(null=False, blank=False, unique=True)
    last_billing_update = models.DateTimeField(null=False, blank=False)
    raw_data = models.TextField(null=False, blank=False)
    expiration_time = models.DateTimeField(null=False, blank=False)
    active = models.BooleanField(null=False, blank=False)
    tier = models.IntegerField(null=True, blank=False, choices=TIER_CHOICES)

    class Meta:
        db_table = 'subscriptions'

class SubscriptionHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    subscription = models.ForeignKey(Subscription, null=False, blank=False, on_delete=DO_NOTHING)
    last_billing_update = models.DateTimeField(null=False, blank=False)
    raw_data = models.TextField(null=False, blank=False)
    expiration_time = models.DateTimeField(null=False, blank=False)
    active = models.BooleanField(null=False, blank=False)

    class Meta:
        db_table = 'subscription_history'

class SubscriptionRequest(models.Model):
    user_id = models.TextField(null=False, blank=False)
    last_billing_update = models.DateTimeField(null=False, blank=False)
    app_user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=DO_NOTHING)

    class Meta:
        db_table = 'subscription_requests'

class ManualSubscription(BaseModel):
    user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=DO_NOTHING)
    tier = models.IntegerField(choices=TIER_CHOICES)
    expires_at = models.DateTimeField(null=False, blank=False)

    class Meta:
        db_table = 'manual_subscriptions'

class Item(models.Model):
    CREDIT_TOKEN = 1
    CARDPACK = 2

    TYPES = (
        (CREDIT_TOKEN, 'CreditToken'),
        (CARDPACK, 'CardPack'),
    )

    price = models.FloatField(default=0)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    page_url = models.TextField(null=True, blank=True)
    purchase_img_url = models.TextField(null=True, blank=True)
    contract_abbr = models.TextField(null=False, blank=False)
    contract_address = models.TextField(null=False, blank=False)
    token_id = models.TextField(null=True, blank=True)
    stripe_price_id = models.TextField(null=True, blank=True)
    min_quantity = models.IntegerField(null=True, blank=True)
    default_quantity = models.IntegerField(null=True, blank=True)
    max_quantity = models.IntegerField(null=True, blank=True)
    whitelist_required = models.BooleanField(default=False)
    start_date_at = models.DateTimeField(null=False, blank=False)
    close_date_at = models.DateTimeField(null=False, blank=False)
    bonus_quantity = JSONField()
    type = models.IntegerField(choices=TYPES, default=CREDIT_TOKEN)

    class Meta:
        db_table = 'items'

class Order(BaseModel):
    PROCESSING = 0
    FAILED = 1
    COMPLETED = 2
    EXPIRED = 3

    MINT_NOT_STARTED = 0
    MINT_IN_PROGRESS = 1
    MINT_FAILED = 2
    MINT_SUCCEEDED = 3
    MINT_TIMEOUT = 4

    # payment_platform_types
    STRIPE = 1
    INTERNAL = 2

    STATUSES = (
        (PROCESSING, 'Processing'),
        (FAILED, 'Failed'),
        (COMPLETED, 'Completed'),
        (EXPIRED, 'Expired'),
    )

    BC_STATUSES = (
        (MINT_NOT_STARTED, 'Mint not started'),
        (MINT_IN_PROGRESS, 'Mint in progress'),
        (MINT_FAILED, 'Mint Failed'),
        (MINT_SUCCEEDED, 'Mint Succeeded'),
        (MINT_TIMEOUT, 'Mint Timeout'),
    )

    TYPES = (
        (STRIPE, 'Stripe'),
        (INTERNAL, 'INTERNAL')
    )

    user = models.ForeignKey('CustomUser', null=False, on_delete=DO_NOTHING)
    item = models.ForeignKey('Item', null=True, on_delete=DO_NOTHING)
    quantity = models.BigIntegerField(null=False, blank=False, default=0)
    amount = models.FloatField(default=0)
    contract = models.TextField(null=True, blank=True)
    token_id = models.TextField(null=True, blank=True)
    delivered = models.BooleanField(null=False, blank=False, default=False)
    purchased_at = models.DateTimeField(null=True, blank=True)
    blockchain_uuid = models.TextField(null=True, blank=True)

    payment_platform_uuid = models.TextField(null=True, blank=True)
    blockchain_order_status = models.IntegerField(choices=BC_STATUSES, default=MINT_NOT_STARTED)
    payment_platform_status = models.IntegerField(choices=STATUSES, default=PROCESSING)
    payment_platform_type = models.IntegerField(choices=TYPES, default=STRIPE)

    cancel_url = models.TextField(null=True, blank=True)
    success_url = models.TextField(null=True, blank=True)
    payment_platform_url = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'orders'

class CardPackType(BaseModel):
    name = models.CharField(max_length=255)
    card_pack_code = models.CharField(max_length=255, null=True) # has to be equal to the card_pack_code in card_pack
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    tier1 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier2 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier3 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier4 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier5 = JSONField(default=list, encoder=DjangoJSONEncoder)
    pack_limits = models.IntegerField(null=True, blank=True)
    star_ratings = JSONField(default=list, encoder=DjangoJSONEncoder,null=True, blank=True)
    rarities = JSONField(default=list, encoder=DjangoJSONEncoder,null=True, blank=True)
    collection = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'card_pack_types'

class AssignedCardPack(BaseModel):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    card_pack_type = models.ForeignKey('CardPackType', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)
    revealed_at = models.DateTimeField(null=True, blank=True)
    revealed = models.BooleanField(default=False)
    card_ids = JSONField(default=list, encoder=DjangoJSONEncoder, null=True, blank=True)
    store_transaction = models.ForeignKey('StoreProductTransactions', on_delete=models.DO_NOTHING, null=True, blank=True)
    refunded = models.BooleanField(default=False)

    class Meta:
        db_table = 'assigned_card_packs'

class PlayerBucket(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    game_position = models.CharField(max_length=255, null=True, blank=True)
    real_popularity = models.IntegerField(default=0)
    usable_popularity = models.IntegerField(default=0)
    bronze = models.BooleanField(null=True, blank=True)
    silver = models.BooleanField(null=True, blank=True)
    gold = models.BooleanField(null=True, blank=True)
    platinum = models.BooleanField(null=True, blank=True)
    diamond = models.BooleanField(null=True, blank=True)
    common = models.IntegerField(default=0)
    uncommon = models.IntegerField(default=0)
    rare = models.IntegerField(default=0)
    ultra_rare = models.IntegerField(default=0)
    legendary = models.IntegerField(default=0)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'player_bucket'

class AssignedPlayer(BaseModel):
    player_nft = models.ForeignKey('NftBucket', on_delete=models.CASCADE, null=True, blank=True, default=None)
    nft_id = models.CharField(max_length=255, null=True, blank=True, default=None)
    rarity = models.CharField(max_length=255, null=True, blank=True, default=None)

    class Meta:
        db_table = 'assigned_players'

class Leaderboard(BaseModel):
    TYPE_CHOICES = [
        ('season', 'Season'),
        ('country', 'Country'),
        ('team', 'Team'),
        ('matchday', 'Matchday'),
        # Add new types here
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True, related_name='leaderboards')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='leaderboards')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='leaderboards')  # New field

    class Meta:
        db_table = 'leaderboards'

class UserLeaderboardSubscription(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    leaderboard = models.ForeignKey(Leaderboard, on_delete=models.CASCADE)
    subscription_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_leaderboard_subscriptions'
        unique_together = ('user', 'leaderboard')

class ChatRoom(V2ImportModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(CustomUser, through='ChatRoomMember')
    match = models.ForeignKey(Match, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='chat_rooms')

    class Meta:
        db_table = 'chat_rooms'

class ChatMessage(BaseModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        db_table = 'chat_messages'

class ChatRoomMember(models.Model):
    room = models.OneToOneField(ChatRoom, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    muted = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    banned_at = models.DateTimeField(null=True, blank=True)
    mod = models.BooleanField(default=False)

    class Meta:
        db_table = 'chat_room_members'
        unique_together = ('room', 'user')

class DataFeedSimModel(models.Model):
    match = models.ForeignKey(Match, null=True, blank=True, on_delete=DO_NOTHING)
    import_id = models.CharField(max_length=50, null=True, blank=True)
    json_events = JSONField(blank=True, null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'data_feed_sim'

class EventThrottler(models.Model):
    exchange = models.CharField(max_length=32, null=False, blank=False)
    event_type = models.CharField(max_length=32, null=False, blank=False, db_column='type')
    data = models.TextField(null=False, blank=True)
    processing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'event_throttler'

class StoreProduct(BaseModel):
    PRODUCT_TYPES = [
        ('consumable', 'Consumable'),
        ('nonconsumable', 'Non-Consumable'),
        ('subscription', 'Subscription'),
        ('nft', 'NFT'),
    ]
    store_product_id = models.CharField(max_length=255)
    apple_product_id = models.CharField(max_length=255, null=True, blank=True)
    google_product_id = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')
    active = models.BooleanField(default=True)
    product_type = models.CharField(max_length=255, null=True, blank=True, default=PRODUCT_TYPES[0][0], choices=PRODUCT_TYPES)
    class Meta:
        db_table = 'store_products'

class StoreProductTransactions(BaseModel):
    transaction = models.ForeignKey(Transactions, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True)
    product = models.ForeignKey(StoreProduct, on_delete=models.PROTECT)
    external_transaction_id = models.CharField(max_length=255, null=True, blank=True)
    initiated = models.BooleanField(default=False)
    initiated_at = models.DateTimeField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    origin_store = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'store_product_transactions'

class NftBucket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    team_id = models.UUIDField(null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)
    game_position = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    common_claiming = models.FloatField(null=True, blank=True, default=0.0)
    common_defence = models.FloatField(null=True, blank=True, default=0.0)
    common_distribution = models.FloatField(null=True, blank=True, default=0.0)
    common_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    common_passing = models.FloatField(null=True, blank=True, default=0.0)
    common_shooting = models.FloatField(null=True, blank=True, default=0.0)
    common_stopping = models.FloatField(null=True, blank=True, default=0.0)
    legendary_claiming = models.FloatField(null=True, blank=True, default=0.0)
    legendary_defence = models.FloatField(null=True, blank=True, default=0.0)
    legendary_distribution = models.FloatField(null=True, blank=True, default=0.0)
    legendary_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    legendary_passing = models.FloatField(null=True, blank=True, default=0.0)
    legendary_shooting = models.FloatField(null=True, blank=True, default=0.0)
    legendary_stopping = models.FloatField(null=True, blank=True, default=0.0)
    nationality = models.CharField(max_length=255, null=True, blank=True, default='')
    rare_claiming = models.FloatField(null=True, blank=True, default=0.0)
    rare_defence = models.FloatField(null=True, blank=True, default=0.0)
    rare_distribution = models.FloatField(null=True, blank=True, default=0.0)
    rare_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    rare_passing = models.FloatField(null=True, blank=True, default=0.0)
    rare_shooting = models.FloatField(null=True, blank=True, default=0.0)
    rare_stopping = models.FloatField(null=True, blank=True, default=0.0)
    star_rating = models.FloatField(default=0.0)
    ultra_rare_claiming = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_defence = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_distribution = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_passing = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_shooting = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_stopping = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_claiming = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_defence = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_distribution = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_passing = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_shooting = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_stopping = models.FloatField(null=True, blank=True, default=0.0)
    common_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    common_image = models.CharField(max_length=255, null=True, blank=True, default='')
    uncommon_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    uncommon_image = models.CharField(max_length=255, null=True, blank=True, default='')
    legendary_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    legendary_image = models.CharField(max_length=255, null=True, blank=True, default='')
    rare_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    rare_image = models.CharField(max_length=255, null=True, blank=True, default='')
    ultra_rare_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    ultra_rare_image = models.CharField(max_length=255, null=True, blank=True, default='')
    common_limit = models.IntegerField(null=True, blank=True, default=0)
    uncommon_limit = models.IntegerField(null=True, blank=True, default=0)
    rare_limit = models.IntegerField(null=True, blank=True, default=0)
    ultra_rare_limit = models.IntegerField(null=True, blank=True, default=0)
    legendary_limit = models.IntegerField(null=True, blank=True, default=0)
    players_group = models.CharField(max_length=255, null=True, blank=True, default='')
    opta_id = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'nft_bucket'

class GameWeek(BaseModel):
    SCHEDULED = 's'  # Game week is planned but hasn't started yet
    LIVE = 'l'  # Game week is currently ongoing
    FINISHED = 'f'  # Game week has ended but not yet processed
    CLOSED = 'c'  # Game week has been processed and concluded

    STATUSES = (
        (SCHEDULED, 'New'),
        (LIVE, 'Live'),
        (FINISHED, 'Not_processed'),
        (CLOSED, 'Concluded'),
    )

    name = models.CharField(max_length=255)
    start_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)
    scored_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUSES, null=False, default=SCHEDULED, max_length=1)
    leaderboards = models.ForeignKey('MatchLeaderboard', null=True, blank=True, on_delete=models.DO_NOTHING)
    season = models.ForeignKey('GameSeason', null=True, blank=True, on_delete=models.DO_NOTHING)

    def already_ended(self):
        return timezone.now() > self.end_at

    @transaction.atomic()
    def save(self, *args, **kwargs):
        super(GameWeek, self).save(*args, **kwargs)

        self.set_up_default_rewards()

    def set_up_default_rewards(self):
        if not DivisionReward.objects.filter(week=self).exists():
            divisions = Division.objects.all()
            for division in divisions:
                self.set_up_division_rewards(division)
            # genesis
            self.set_up_division_rewards(None)

    def set_up_division_rewards(self, division: Optional[Division]):
        reward_configurations = {
            1: [
                    (1,1, {'credits': 1575, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 875, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 600, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 375, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                2: [
                    (1,1, {'credits': 1425, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 775, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 525, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 325, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                3: [
                    (1,1, {'credits': 1275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 700, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 475, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                4: [
                    (1,1, {'credits': 1150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 625, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 425, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 175, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                5: [
                    (1,1, {'credits': 1025, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 550, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 375, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 175, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                6: [
                    (1,1, {'credits': 925, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 500, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 325, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                7: [
                    (1,1, {'credits': 825, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 450, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 175, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                8: [
                    (1,1, {'credits': 750, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 400, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                9: [
                    (1,1, {'credits': 675, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 350, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 50, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                10: [
                    (1,1, {'credits': 600, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 300, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                0: [
                    (1,1, {'credits': 600, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 300, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
        }

        tier = division.tier if division is not None else 0
        positions = reward_configurations.get(tier, [])

        qs = DivisionReward.objects
        if division is None:
            qs = qs.filter(week=self, division__isnull=True)
        else:
            qs = qs.filter(week=self, division=division)
        existing_rewards = qs.values_list('min_position', 'max_position')

        rewards_instances = []
        for min_position, max_position, reward_data in positions:
            if (min_position, max_position) not in existing_rewards:
                reward = Rewards.objects.create(
                    name=f"Division {tier} Position {min_position} to {max_position}",
                    **reward_data
                )
                rewards_instances.append(DivisionReward(
                    min_position=min_position,
                    max_position=max_position,
                    reward=reward,
                    week=self,
                    division=division
                ))

        if rewards_instances:
            DivisionReward.objects.bulk_create(rewards_instances)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'game_weeks'

class UserGameWeekHistory(BaseModel):
    SAFE = 's'
    PROMOTED = 'p'
    DEMOTED = 'd'

    STATUSES = (
        (SAFE, 'Safe'),
        (PROMOTED, 'Promoted'),
        (DEMOTED, 'Demoted'),
    )

    user = models.ForeignKey('CustomUser', on_delete=DO_NOTHING)
    game_week = models.ForeignKey('GameWeek', on_delete=DO_NOTHING)
    week_division = models.ForeignKey('Division', on_delete=DO_NOTHING, null=True, blank=True)
    week_division_position = models.IntegerField(default=0)
    week_division_tier = models.IntegerField(null=True, blank=True)
    week_points = models.IntegerField(default=0)
    week_coins = models.IntegerField(default=0)
    new_division = models.ForeignKey('Division', on_delete=DO_NOTHING, null=True, blank=True, related_name='new_divisions')
    new_division_tier = models.IntegerField(null=True, blank=True)
    week_average_rank = models.FloatField(null=True, blank=True)
    week_matches_played = models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES, null=False, default=SAFE, max_length=1)

    def __str__(self):
        return f"User history for week {self.game_week.name}, {self.user.name}({self.user.id})"
    class Meta:
        db_table = 'user_game_week_histories'

class UserDivision(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    game_week = models.ForeignKey(GameWeek, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_or_initiate(cls, user_id, division_id, game_week_id, points):
        try:
            user_division = cls.objects.get(
                user_id=user_id,
                division_id=division_id,
                game_week_id=game_week_id,
            )
            user_division.points = points
            user_division.join_date = timezone.now()
        except cls.DoesNotExist:
            user_division = cls(
                user_id=user_id,
                division_id=division_id,
                game_week_id=game_week_id,
                join_date=timezone.now()
            )
        return user_division

    def __str__(self):
        return f"User Division for week: {self.game_week.name}, tier:{self.division.tier} {self.user.name}({self.user.id})"

    class Meta:
        unique_together = ('user', 'division', 'game_week')
        db_table = 'user_divisions'

class DivisionReward(BaseModel):
    week = models.ForeignKey(GameWeek, null=False, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)
    min_position = models.IntegerField(default=1)
    max_position = models.IntegerField(null=True, blank=True)
    reward = models.ForeignKey('Rewards', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'division_rewards'
        unique_together = ('week', 'division', 'min_position', 'max_position')

class AppInbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)  # Example values: 'Active', 'Inactive'
    priority = models.CharField(max_length=50)  # Example values: 'Low', 'Medium', 'High'
    category = models.CharField(max_length=50)  # Example categories: 'Update', 'Reward'
    image_url = models.URLField(null=True, blank=True)
    link_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)  # New field to track if the notification is read
    claimed = models.BooleanField(default=False)  # New field to track if the notification is claimed
    clamed_at = models.DateTimeField(null=True, blank=True)  # New field to track when the notification is claimed
    reward = models.ForeignKey('Rewards', null=True, blank=True, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, null=True, blank=True, on_delete=models.CASCADE)
    game_week_id = models.ForeignKey(GameWeek, null=True, blank=True, on_delete=models.CASCADE)
    clear = models.BooleanField(default=False)  # New field to track if the notification is cleared
    game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_inbox'

    def __str__(self):
        return self.title

class GameWeekDivision(models.Model):
    week = models.ForeignKey(GameWeek, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    promotion_count = models.FloatField()
    relegation_count = models.FloatField()

    class Meta:
        db_table = 'game_week_divisions'
    
class Rewards(BaseModel):
    name = models.CharField(max_length=255)
    credits = models.FloatField(default=0)  # For virtual currency
    game_token = models.FloatField(default=0)  # For cryptocurrency
    lapt_token = models.FloatField(default=0)  # For first token
    event_tickets = models.IntegerField(default=0)  # For event tickets
    ball = models.IntegerField(default=0)  # For merchandise
    signed_ball = models.IntegerField(default=0)  # For merchandise
    shirt = models.IntegerField(default=0)  # For merchandise
    signed_shirt = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_1 = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_2 = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_3 = models.IntegerField(default=0)  # For merchandise
    season_pack_1 = models.IntegerField(default=0)  # For merchandise
    season_pack_2 = models.IntegerField(default=0)  # For merchandise
    season_pack_3 = models.IntegerField(default=0)  # For merchandise

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rewards'

class PushNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, max_length=255,null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    payload = JSONField(null=True, blank=True)
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification to {self.user} - {self.title}"
    
    class Meta:
        db_table = 'push_notifications'

class Badges(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.URLField()
    points = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'badges'
        

class UserBadges(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badges, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Badge {self.badge.name} to {self.user.name}"
    
    class Meta:
        db_table = 'user_badges'
        
class Frames(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.URLField()
    points = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'frames'
        
class UserFrames(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    frame = models.ForeignKey(Frames, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Frame {self.frame.name} to {self.user.name}"
    
    class Meta:
        db_table = 'user_frames'
        
class Banner(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.URLField()
    points = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'banners'
        
class UserBanners(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Banner {self.banner.name} to {self.user.name}"
    
    class Meta:
        db_table = 'user_banners'
```

## File: `core/notifications.py`
- **File Size:** 4857 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** task that assigned the default badges, banners and frames to users

```
from datetime import timedelta, timezone
from typing import List

from celery import shared_task
from django.db.models import Q
from util.events import create_amqp_event
from django.conf import settings
from core.models import Badges, Banner, CustomUser, Frames, GameWeek, PushNotification, UserBadges, UserBanners, UserFrames
import mixpanel

mixpanel_client = mixpanel.Mixpanel('be4f6d7541a1930dcec47b443dc1a86f')

def count_user_notifications_last_hour(user):
    one_hour_ago = timezone.now() - timedelta(hours=1)
    return PushNotification.objects.filter(user=user, sent_at__gte=one_hour_ago).count()

from django.utils import timezone

def send_push(user, title, message, url=None):
    # Prepare the event data
    event_data = {
        "user_id": str(user.id),  # Ensure UUID is converted to string
        "title": title,
        "message": message,
        "push_token": user.firebase_id,
    }

    # Count the number of notifications sent to the user in the last hour
    notification_count = count_user_notifications_last_hour(user)

    if url is not None:
        event_data["url"] = url

    if notification_count < 3:
        # Create a PushNotification record in the database
        PushNotification.objects.create(
            user=user,
            title=title,
            message=message,
            payload=event_data,
            sent_at=timezone.now()
        )

        # Send the push notification event (via AMQP)
        create_amqp_event(
            settings.RMQ_FCM_EXCHANGE,
            "push_notification",
            event_data,
        )

        # Mixpanel event properties
        event_props = {
            "event_name":  "Push Notification",
            "title":       title,
            "description": message,
            "distinct_id": str(user.id),  # Ensure UUID is converted to string
            "type":        "sent",
            "username":    user.name,
        }

        # Track the push notification event in Mixpanel
        try:
            mixpanel_client.track(str(user.id), "Push Notification Sent to User", event_props)
        except Exception as e:
            # Log the error for debugging if Mixpanel tracking fails
            print(f"Mixpanel event tracking failed: {e}")
    else:
        print(f"Not sending push notification to {user.name}. Limit of 3 notifications per hour reached.")

@shared_task
def send_push_to_users(user_ids, week_id):
    users = CustomUser.objects.filter(
        Q(id__in=user_ids) & Q(firebase_id__startswith="Expo")
    )
    title = 'Your game week concluded'
    message = 'Tap to here to see summary'
    url = f"/divisions/summary/{week_id}"

    print(f"push push: {title}, {message}, {url}")
    for user in filter_repeated_users(users):
        try:
            send_push(user, title, message, url)
            print(f"pushed: {user.id} {title}, {message}, {url}")
        except Exception as e:
            print(f"Failed to send notification to {user.id}: {e}")

@shared_task
def send_push_to_user(user_id, title, message):
    user = CustomUser.objects.get(id=user_id)
    if user.firebase_id and user.firebase_id.startswith("Expo"):
        send_push(user, title, message)

@shared_task
def send_push_to_all(title, message):
    users = CustomUser.objects.filter(firebase_id__startswith="Expo")
    for user in filter_repeated_users(users):
        send_push(user, title, message)

def filter_repeated_users(users: List[CustomUser]) -> List[CustomUser]:
    sorted_users = sorted(users, reverse=True, key=lambda user: user.updated_at)
    already_present = set()

    result = []
    for user in sorted_users:
        if user.firebase_id not in already_present:
            already_present.add(user.firebase_id)
            result.append(user)

    return result

@shared_task
def assign_default_items_to_users():
    # Fetch default badges, frames, and banners
    default_badges = Badges.objects.filter(type='default')
    default_frames = Frames.objects.filter(type='default')
    default_banners = Banner.objects.filter(type='default')

    # Fetch all users
    users = CustomUser.objects.all()

    # Assign default badges to users
    for user in users:
        for badge in default_badges:
            if not UserBadges.objects.filter(user=user, badge=badge).exists():
                UserBadges.objects.create(user=user, badge=badge)

    # Assign default frames to users
    for user in users:
        for frame in default_frames:
            if not UserFrames.objects.filter(user=user, frame=frame).exists():
                UserFrames.objects.create(user=user, frame=frame)

    # Assign default banners to users
    for user in users:
        for banner in default_banners:
            if not UserBanners.objects.filter(user=user, banner=banner).exists():
                UserBanners.objects.create(user=user, banner=banner)
```

## File: `core/renderers.py`
- **File Size:** 114 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    charset = 'utf-8'

```

## File: `core/serializers.py`
- **File Size:** 1863 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** set tz force if it's not set

```
import json

import pytz
from rest_framework import serializers

from core import const
from core.models import CustomUser, Match, Team, Player, Game, GamePick, MatchEvent, GameEvent, Competition, \
    Action, GamePowerUp, MatchReward, MatchPlayer, MatchHeadline
from datetime import datetime

class StringListField(serializers.ListField):
    child = serializers.CharField()

class UUIDListField(serializers.ListField):
    child = serializers.UUIDField()

class UpdateUserAvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField(required=True)

class CurrentUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'balance', 'paypal_email', 'avatar_url',)

class CustomTimeField(serializers.Field):
    def to_representation(self, value):
        if isinstance(value, str):
            try:
                dt_obj = datetime.fromisoformat(value)
            except ValueError:
                return value
        else:
            dt_obj = value
        if dt_obj.tzinfo is None:
            dt_obj = dt_obj.replace(tzinfo=pytz.UTC)
        formatted_time = dt_obj.isoformat()

        return formatted_time

class MatchEventSerializer(serializers.ModelSerializer):
    created_at = CustomTimeField()
    timestamp = CustomTimeField()

    class Meta:
        model = MatchEvent
        fields = ('id', 'match_id', 'created_at', 'timestamp', 'team_id',
                  'player_id', 'type', 'points', 'payload', 'minute',
                  'second', 'x', 'y', 'match_event_id', 'provider_id', 'opta_feed_item_version_id', 'status')

class RevenueCatSyncSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    last_billing_update = serializers.DateTimeField(required=True)
    sync = serializers.BooleanField(required=False)

```

## File: `core/sync.py`
- **File Size:** 2234 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** changes to normalized names. Bulk the entries

```
import logging
import uuid

import requests
from django.conf import settings
from django.db import transaction

from core.models import Team, Player
from util import gce

def update_avg_score():
    players_qs = Player.objects.all()[:9999999]
    len_players = len(players_qs)

    count = 0
    for player in players_qs:
        player.avg_score = player.calculate_avg_score()
        player.save(update_fields=['avg_score'])
        count += 1
        if count % 100 == 0:
            print('processed {} out of {} records'.format(count, len_players))

def sync_missing_team_crests():
    for team in Team.objects.filter(crest_url__isnull=True):
        import_id = team.import_id.replace('t', '')
        image_url = 'https://ufl-crests.s3.amazonaws.com/{}.png'.format(import_id)
        res = requests.get(image_url)
        if res.status_code != 200:
            logging.error("cannot get image by url {}".format(image_url))
            continue

        new_filename = str(uuid.uuid4()) + ".png"

        # upload image to gce
        bucket = settings.GCE_TEAM_CRESTS_BUCKET
        try:
            gce.upload_file(bucket, new_filename, res.content, res.headers['content-type'])
            new_image_url = gce.get_file_url(bucket, new_filename)
        except Exception:
            logging.exception("cannot upload file to gce")
            continue

        # update in db
        team.crest_url = new_image_url
        team.save(update_fields=['crest_url'])

        logging.info("team {} synced".format(team.pk))

def normalize_and_check_all_names():
    with transaction.atomic():
        players = Player.objects.iterator()  # for large dataset
        to_update = []

        for player in players:
            current_normalized_name = player.normalized_name
            new_normalized_name = player.calculate_normalized_name()
            if new_normalized_name != current_normalized_name:
                player.normalized_name = new_normalized_name
                to_update.append(player)

        # Bulk update all changed records
        if to_update:
            Player.objects.bulk_update(to_update, ['normalized_name'])
        
        print(f"Updated {len(to_update)} players with new normalized names.")
```

## File: `core/tasks.py`
- **File Size:** 5745 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** task that assigned the default badges, banners and frames to users

```
from datetime import timedelta
from celery.task import task
from celery import shared_task
from django.db import connection
from django.utils import timezone
from core.models import Match, CustomUser
from core.views_inner import process_simulations
# from ortec.sync import sync_competitions, sync_registrations, sync_all_teams, sync_matches
from opta.sync import sync_competitions, sync_all_teams, sync_matches, process_event_throttling
from revenue_cat.sync import process_subscription_requests, expire_subscriptions
from soccer_wiki.sync import sync_players, upload_soccer_wiki_photos
from core.sync import normalize_and_check_all_names
from blockchain_web3.sync import update_order_statuses
from blockchain_web3.tasks import process_mint_nfts_for_expired_cardpacks, process_pending_cardpack_transactions, process_pending_crypto_transactions
import time
from util.events import create_amqp_event
from core.models import CustomUser, GameWeek
from divisions.sync import conclude_game_week, calculate_promotion_and_relegation
from core.notifications import assign_default_items_to_users

@task
def task_sync_competitions(competition_code = None):
    sync_competitions(competition_code)

@task
def task_sync_teams():
    sync_all_teams()

@task
def task_sync_matches(match_time_delta=12, skip_sync_delay = False, competition_code = None):
    sync_matches(match_time_delta, skip_sync_delay, competition_code)

@task
def task_sync_match_players():
    # get upcoming matches for next 3-21 days
    start = timezone.now().today()
    end = start + timedelta(days=21)
    qs = Match.objects.filter(match_time__gte=start, match_time__lt=end).select_related('competition')
    for m in qs:
        if m.competition.enabled: # make sure competition s enabled to sync
            m.sync_match_players(True)

@task
def task_process_simulations():
    process_simulations(None)

def sync_extension(name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("create extension " + name)
    except Exception:
        pass

def make_soccer_wiki_matches():
    sync_extension("unaccent")
    sync_extension("pg_trgm")
    sql = """
    DO $$
    DECLARE
      v_player record;
      v_wiki_player record;
      v_found integer := 0;
      v_not_found integer := 0;
    BEGIN
      PERFORM set_limit(0.3);

      FOR v_player IN SELECT * FROM players WHERE soccer_wiki_player_id is null
      LOOP
        BEGIN
          SELECT swp.*
            INTO STRICT v_wiki_player
            FROM soccer_wiki_players swp
           WHERE (swp.first_name||' '||swp.second_name) % (v_player.first_name||' '||v_player.last_name)
           ORDER BY (swp.first_name||' '||swp.second_name) <-> (v_player.first_name||' '||v_player.last_name) ASC,
                    swp.import_id DESC
           LIMIT 1;

          v_found := v_found + 1;

          UPDATE players
             SET soccer_wiki_player_id = v_wiki_player.id
           WHERE id = v_player.id;
        EXCEPTION
          WHEN no_data_found THEN
            -- RAISE EXCEPTION 'Cannot find soccer_wiki players for (%)', v_player.id;
            v_not_found := v_not_found + 1;
        END;
      END LOOP;
      RAISE NOTICE 'FOUND (%) VS NOT FOUND (%)', v_found, v_not_found;
    END$$;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)

@task
def task_update_user_stats():
    for user in CustomUser.objects.all()[:999999]:
        user.calculate_stats()

def update_image_url_from_soccer_wiki_players():
    sql = """
update players
   set image_url = soccer_wiki_players.internal_image_url
  from soccer_wiki_players
 where players.soccer_wiki_player_id = soccer_wiki_players.id
   and players.image_url is null
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)

def clear_image_url_for_empty_soccer_wiki_players():
    sql = """
update players
   set image_url = null
 where soccer_wiki_player_id is null
"""
    with connection.cursor() as cursor:
        cursor.execute(sql)

@task
def task_sync_soccer_wiki():
    make_soccer_wiki_matches()
    update_image_url_from_soccer_wiki_players()
    clear_image_url_for_empty_soccer_wiki_players()

@task
def task_download_soccer_wiki():
    print("Downloading soccer wiki")
    sync_players()
    upload_soccer_wiki_photos()
    print("Done downloading soccer wiki")

@task
def task_process_subscription_requests():
    process_subscription_requests()

@task
def task_expire_subscriptions():
    expire_subscriptions()

@task
def task_update_order_statuses():
    return
    # update_order_statuses()

@task
def task_run_event_throttling():
    process_event_throttling()

@task
def task_normalize_and_check_all_names():
    normalize_and_check_all_names()

@task
def task_conclude_game_week():
    ended_game_weeks = GameWeek.objects.filter(end_at__lte=timezone.now(), status=GameWeek.LIVE)
    for week in ended_game_weeks:
        conclude_game_week(week)

@task
def task_calculate_promotion_and_relegation():
    live_weeks = GameWeek.objects.filter(status=GameWeek.LIVE)
    for week in live_weeks:
        calculate_promotion_and_relegation(week)

@task
def task_sync_matches_via_sdapi(match_time_delta=12, skip_sync_delay = False, competition_code = None, force_SDAPI: bool = True):
    sync_matches(match_time_delta, skip_sync_delay, competition_code, force_SDAPI)

@task
def mint_nfts_for_expired_cardpacks():
    process_mint_nfts_for_expired_cardpacks()
    
@task
def mint_process_pending_crypto_transactions():
    process_pending_crypto_transactions()
    
@task
def mint_process_pending_cardpack_transactions():
    process_pending_cardpack_transactions()
    
@task
def assign_default_items_to_users_task():
    assign_default_items_to_users()
```

## File: `core/templates/admin/core/customuser/change_list.html`
- **File Size:** 213 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixes for notifications screen, links and actions

```
{% extends "admin/change_list.html" %}

{% block object-tools %}
    {{ block.super }}
    <li>
        <a class="addlink" href="{% url 'admin:send-notification' %}">Send Notification</a>
    </li>
{% endblock %}

```

## File: `core/templates/admin/custom_task_form.html`
- **File Size:** 224 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Admin event feed simulator

```
{% extends "admin/base_site.html" %}
{% block content %}
<h1>Run JSON Task</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="button">Run Task</button>
</form>
{% endblock %}

```

## File: `core/templates/assign_card_pack.html`
- **File Size:** 1199 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** improve the admin for assigning cardpacks

```
{% extends "admin/base_site.html" %}
{% load static %}

{% block content %}
<div class="content">
    <div class="card">
        <div class="card-header">
            <h1>Assign Card Pack to User</h1>
        </div>
        <div class="card-body">
            {% if form.errors %}
                <div class="errors">
                    <p>Please correct the following errors:</p>
                    <ul>
                        {% for field in form %}
                            {% for error in field.errors %}
                                <li><strong>{{ field.label }}:</strong> {{ error }}</li>
                            {% endfor %}
                        {% endfor %}
                    </ul>
                </div>
            {% endif %}
            <form method="post" novalidate>
                {% csrf_token %}
                {{ form.as_p }}
                <div class="form-row">
                    <button type="submit" class="button button-primary">Assign Card Pack</button>
                    <a href="{% url 'admin:core_assignedcardpack_changelist' %}" class="button">Cancel</a>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

```

## File: `core/templates/match_change.html`
- **File Size:** 1090 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** PS-1656 make new rewards

```
{% extends 'admin/change_form.html' %}

{% block after_field_sets %}
    {{ block.super }}
    <h3>Example:</h3>
    <ul>
        <li><b>Min Position:</b> 1, <b>Max Position:</b> 1, <b>Amount:</b> 5 (params for first position on leaderboard)</li>
        <li><b>Min Position:</b> 2, <b>Max Position:</b> 2, <b>Amount:</b> 4 (params for second position on leaderboard)</li>
        <li><b>Min Position:</b> 3, <b>Max Position:</b> 3, <b>Amount:</b> 3 (params for third position on leaderboard)</li>
        <li><b>Min Position:</b> 4, <b>Max Position:</b> 7, <b>Amount:</b> 2 (params for fourth to seventh positions on leaderboard)</li>
        <li><b>Min Position:</b> 8, <b>Max Position:</b> (Leave blank), <b>Amount:</b> 1 (params for eighth to last positions on leaderboard)</li>
    </ul>
{% endblock %}

{% block submit_buttons_bottom %}
    {{ block.super }}
    <div class="submit-row">
        <input type="submit" value="Start 10 min sim" name="_start-short-simulation">
        <input type="submit" value="Start 90 min sim" name="_start-long-simulation">
    </div>
{% endblock %}
```

## File: `core/templates/notifications.html`
- **File Size:** 886 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Merge branch 'feature/send-push-notifications' of github.com:gameon-app-inc/laliga-matchfantasy-admin into feature/send-push-notifications

```
{% extends "admin/base_site.html" %}

{% block content %}
<div class="module">
    <h1>Send Notification</h1>
    <form method="post">
        {% csrf_token %}
        <div class="form-row">
            {{ form.title.errors }}
            <label for="id_title">Title:</label>
            {{ form.title }}
        </div>
        <div class="form-row">
            {{ form.message.errors }}
            <label for="id_message">Message:</label>
            {{ form.message }}
        </div>
        <div class="form-row">
            {{ form.user_ids.errors }}
            <label for="id_user_ids">User IDs (comma-separated):</label>
            {{ form.user_ids }}
        </div>
        <div class="form-row">
            <button type="submit">Send Notifications</button>
            <button onclick="window.history.back()">Back</button>
        </div>
    </form>
</div>
{% endblock %}

```

## File: `core/templates/send_inbox_message.html`
- **File Size:** 3041 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** app inbox to admin

```
{% extends "admin/base_site.html" %}

{% block content %}
<div class="content">
    <h1>Send Inbox Message</h1>
    <form method="post">
        {% csrf_token %}
        <fieldset class="module aligned">
            <div class="form-row">
                <label for="id_title">Title:</label>
                <input type="text" name="title" value="{{ form.title.value }}" maxlength="255" id="id_title">
            </div>
            <div class="form-row">
                <label for="id_description">Description:</label>
                <textarea name="description" cols="40" rows="10" id="id_description">{{ form.description.value }}</textarea>
            </div>
            <div class="form-row">
                <label for="id_user_ids">User IDs (comma-separated):</label>
                <input type="text" name="user_ids" value="{{ form.user_ids.value }}" id="id_user_ids">
                <p class="help">{{ form.user_ids.help_text }}</p>
            </div>
            <div class="form-row">
                <label for="id_status">Status:</label>
                <select name="status" id="id_status">
                    {% for choice in form.status.field.choices %}
                        <option value="{{ choice.0 }}" {% if form.status.value == choice.0 %}selected{% endif %}>
                            {{ choice.1 }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="form-row">
                <label for="id_priority">Priority:</label>
                <select name="priority" id="id_priority">
                    {% for choice in form.priority.field.choices %}
                        <option value="{{ choice.0 }}" {% if form.priority.value == choice.0 %}selected{% endif %}>
                            {{ choice.1 }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="form-row">
                <label for="id_category">Category:</label>
                <select name="category" id="id_category">
                    {% for choice in form.category.field.choices %}
                        <option value="{{ choice.0 }}" {% if form.category.value == choice.0 %}selected{% endif %}>
                            {{ choice.1 }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="form-row">
                <label for="id_image_url">Image URL:</label>
                <input type="url" name="image_url" value="{{ form.image_url.value }}" id="id_image_url">
            </div>
            <div class="form-row">
                <label for="id_link_url">Link URL:</label>
                <input type="url" name="link_url" value="{{ form.link_url.value }}" id="id_link_url">
            </div>
        </fieldset>
        <div class="submit-row">
            <button type="submit" class="default">Send Inbox Message</button>
        </div>
    </form>
</div>
{% endblock %}

```

## File: `core/templates/terms.html`
- **File Size:** 47706 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">ol{margin:0;padding:0}table td,table th{padding:0}.c1{color:#333333;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:10pt;font-family:"Times New Roman";font-style:normal}.c8{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c4{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:10pt;font-family:"Times New Roman";font-style:normal}.c0{background-color:#ffffff;padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c3{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c5{padding-top:0pt;padding-bottom:8pt;line-height:1.070000019940463;orphans:2;widows:2;text-align:left}.c6{border-top-width:0pt;border-top-style:solid;border-bottom-width:0pt;border-bottom-style:solid}.c10{font-size:10pt;font-family:"Times New Roman";color:#333333;font-weight:400}.c7{font-size:10pt;font-family:"Times New Roman";color:#333333;font-weight:700}.c9{background-color:#ffffff;max-width:451.4pt;padding:72pt 72pt 72pt 72pt}.c2{height:11pt}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}</style></head><body class="c9"><p class="c3"><span class="c1">FANCLASH TERMS OF USE </span></p><p class="c3"><span class="c4">&nbsp;</span></p><p class="c0"><span class="c1">1. &nbsp; GENERAL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">These Terms of Use (hereinafter referred to as &ldquo;Terms of Use&rdquo;) comprise the Terms of Use of your use of the FanClash services (the &ldquo;Services&rdquo;) provided by Inplay Labs Ltd (&ldquo;Inplay&rdquo;) on the App FanClash (the &ldquo;App&rdquo;). They constitute your agreement with us and apply to the exclusion of any other terms that you seek to impose or incorporate or which are implied by trade, custom, practice or course of dealing. </span></p><p class="c0 c2"><span class="c1"></span></p><p class="c0"><span class="c1">By visiting the App and/or by registering and/or using the Services, you agree to be, and are, bound by these Terms of Use.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">These General Terms of Use were last updated on 1 April 2021. All previous Terms of Use are not applicable.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">2. &nbsp; AGREEING TO THE TERMS OF USE</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">2.1. By registering an account with FanClash and accepting FanClash terms, you will enter into a legally binding agreement which incorporates these Terms of Use.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">2.2. You should read and will be bound by the full Terms of Use when using our Services.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">3. &nbsp; PARTIES &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">3.1. The Terms of Use are a binding legal agreement between you and Inplay Labs Ltd.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">3.2. References in the Terms of Use to &ldquo;FanClash&rdquo;, &quot;us&quot;, &quot;our&quot; or &quot;we&quot; are references to Inplay Labs Ltd.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">3.3. References to &quot;you&quot; and &quot;your&quot; in the Terms of Use are to you as the end user of the Services.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">4. &nbsp; CHANGES TO THE TERMS OF USE &nbsp;</span></p><p class="c0"><span class="c1">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></p><p class="c0"><span class="c1">4.1. The Terms of Use govern your use of the Services and supersede any and all prior agreements between you and us in respect of the same.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">4.2. We may need to change the Terms of Use from time to time (including to comply with applicable law or a change in our regulatory requirements). </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">4.3. No customer services representative has the power to amend these Terms of Use.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">5. &nbsp; REGISTERING AN ACCOUNT</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c10">5.1. To use our Services, you need to register an account with us (</span><span class="c7">&quot;Account&quot;</span><span class="c1">). When you open your Account, you will be asked to confirm you are at least 18 years of age, provide your email, enter a password and username. You shall ensure that the details provided by you at registration are accurate and kept up to date. For further information about our collection and use of your personal information, please refer to our Privacy Policy.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">5.2. You can only register one (1) Account with us. Should we find that you have opened multiple or duplicate Accounts, without limiting any other rights or remedies available to us, we will close all but one (1) Account.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">5.3. You must provide us with accurate information in relation to your Account. It is your responsibility to inform us of any changes to your personal details which may impact on the use of your Account.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">5.4. We reserve the right to refuse to open an Account for any reason. We will notify you of our decision as soon as reasonably possible after you have applied to open an Account.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">5.5. Any play via your Account must be for your own benefit and not for the benefit of any third party unless otherwise agreed by us in advance.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6. &nbsp; INFORMATION WE COLLECT ABOUT YOU</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.1. We process information about you in accordance with our Privacy Policy.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.2. Our Privacy Policy forms part of these Terms of Use and contains details on the types of information we collect and what we do with that information.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.3. ELIGIBILITY</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.4. You must be 18 (eighteen) years of age or older and to use the Service. </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.5. Access to our Service may not be legal for residents of, or persons located in, certain countries. We do not intend that the Service be used by persons in countries in which such activities are illegal. Our Service does not constitute an offer, solicitation or invitation by us for the use of our service in any jurisdiction in which such activities are prohibited by law.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.6. It is your responsibility to determine the law that applies in the location in which you are present and to ensure that you are acting legally in that jurisdiction by using our Service. We accept no liability if your use of our Service is in contravention of the laws of the country in which you are located.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.7. If we have reasonable information to believe that you are accessing the services in a country in which the use of the services is not legal, we shall be entitled to immediately suspend or close your Account.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.8. VERIFICATION</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.9. We reserve the right to ask for proof of age and address from you and may suspend your Account until you provide the requested documents.</span></p><p class="c0"><span class="c4">&nbsp;</span></p><p class="c0"><span class="c1">6.10. &nbsp; &nbsp; &nbsp; By accepting the Terms of Use, you authorise us to conduct any identification, credit or other verification checks that we may require, either for our own purposes or as required by a regulatory body. You agree to provide us with any information we may need in relation to such checks.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.11. &nbsp; &nbsp; &nbsp; We may supply the information that you have given us to authorised credit reference agencies, who will check the details we provide against any databases (public or private) to which they have access and will keep a record of that check. </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.12. &nbsp; &nbsp; &nbsp; We reserve the right to not award prizes to customers until account information has been verified or verification procedures have been performed. </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">6.13. &nbsp; &nbsp; &nbsp; As well as the other checks we may undertake, you may be required to provide proof of identity or address to assist us with verification. If requested by us, you will need to send us a copy of your passport, driver&#39;s licence, national identity card, birth certificate, other official document or utility bill, etc for these purposes.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">7. &nbsp; USERNAME AND PASSWORD</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">7.1. When you register with us, you will be able to choose a Username and Password for your Account. You may change your Username and Password. </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">7.2. Your Username is the screen name which makes you readily identifiable to other users and your registered email will be required to log into FanClash.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">7.3. You may not in any circumstances nominate or allow any person to be an authorised user of your Account. It is your responsibility to ensure that you do not reveal your login details to anyone else. We shall be entitled to assume that all predictions placed when your login details have been entered correctly are valid and made by you, whether or not such transactions were authorised by you. We shall not be liable for any claims in the event that you disclose your login details to anyone else or where your negligence or deliberate act has contributed to such third party access to your Account.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">7.4. It is your sole responsibility to maintain the confidentiality and security of your Account information and login details. If young persons are sharing or have access to your devices, you may wish to install parental control software. You should change your Password/Pin on a regular basis via the link on our App. You should notify us of any unauthorised use of your Account as soon as you suspect it or otherwise become aware of it.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">8. &nbsp; WINNINGS</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">8.1. Subject to these Terms of Use, we will credit your Paypal wallet with your winnings as soon as practical once a contest has completed.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">8.2. Winnings will usually be paid without you needing to make a claim. If you believe that you have not received any winnings due to you then you should notify us as soon as possible and provide evidence for your claim. No claim for winnings may be made more than six months after the date on which the relevant contest took place.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">8.3. We reserve the right to suspend the service in the event of the occurrence of an event outside our control (see Events Outside our Control). We will endeavour to pay you any winnings due to you as soon as the relevant event outside our control has ceased.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">8.4. &nbsp; &nbsp; &nbsp; &nbsp; If we credit winnings in error, we reserve the right to, at any time, reverse the transaction.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9. USE OF THE SERVICE</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9.1. &nbsp; &nbsp; &nbsp;We use Ortec to provide data on which the game scoring and player performance is based. This data and all other information displayed on the App is made available to you for your general information and non-commercial use only. You acknowledge that the provision of such data (and therefore the making available of the App) is always subject to any arrangements, restrictions or prohibitions imposed by any sports body (including any league, association or authority), any team, official or other participant in any match or event, or of any rights holder, agency or other person involved in the control, management or exploitation of any rights to or in respect of any match or event. Any decision, order, act or omission made by such person is outside of our control and therefore, to the extent it affects our ability to make the whole or any part of the App available to you for your use in accordance with these terms, you acknowledge that we shall not be liable to you for any such failure or delay.</span></p><p class="c0 c2"><span class="c1"></span></p><p class="c0 c6"><span class="c1">The App is available &lsquo;as is&rsquo; and &lsquo;as available&rsquo;. This means:</span></p><p class="c0 c6 c2"><span class="c1"></span></p><p class="c0 c6"><span class="c1">(a) we do not warrant or guarantee that the App will always be available or uninterrupted. We may suspend or withdraw or restrict the availability of all or any part of the App for business and operational reasons. We will try to give you reasonable notice of any suspension or withdrawal, but will not be liable to you in the event no such notice is provided;</span></p><p class="c0 c6"><span class="c1">(b) we do not guarantee that the App will be secure or free from bugs and viruses; and</span></p><p class="c0 c2 c6"><span class="c1"></span></p><p class="c0 c6"><span class="c1">(c) neither Opta, us or any third party provides any warranty or guarantee as to the accuracy, timeliness, performance, completeness or suitability of the App, including any data provided on the App. You hereby acknowledge that the App may contain inaccuracies or errors and that we expressly exclude liability for any such inaccuracies or errors.</span></p><p class="c0 c6 c2"><span class="c1"></span></p><p class="c0 c6"><span class="c1">We reserve the right to change the App without notice, including the features, functionality, services and content available on the App, from time to time to reflect changes to our products, our users&#39; needs and our business priorities.</span></p><p class="c0 c6 c2"><span class="c1"></span></p><p class="c0 c6"><span class="c1">From time to time updates to the App may be issued through the App Store. Depending on the update, you may not be able to use the App until you have downloaded the latest version of the App and accepted any new terms.</span></p><p class="c0 c6 c2"><span class="c1"></span></p><p class="c0 c6"><span class="c1">You will be assumed to have obtained permission from the owner of the mobile telephone or handheld device that is controlled, but not owned, by you (Device) to download and use a copy of the App onto the Device. This person may be charged by his service provider for internet access on the Device. You accept responsibility in accordance with these terms for the use of the App on any Device, whether or not it is owned by you.</span></p><p class="c0 c6 c2"><span class="c1"></span></p><p class="c0 c6"><span class="c1">The App may contain links to third party websites. Such third party websites are not under our control, and we are not responsible for and do not endorse their content or their privacy policies (if any).</span></p><p class="c0 c2"><span class="c1"></span></p><p class="c0"><span class="c1">&nbsp;9.2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You must not misuse our App by knowingly introducing viruses, trojans, worms, logic bombs or other material which is malicious or technologically harmful. You must not attempt to gain unauthorised access to: our app; the servers on which our apps are stored; or, any server, computer or database connected to our Apps. We will report any such breach to the relevant law enforcement authorities and we will cooperate with those authorities by disclosing your identity to them.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9.3. &nbsp; &nbsp; &nbsp; You agree that you will not use the Service in any way that may lead to the encouragement, procurement or carrying out of any criminal or unlawful activity, or cause distress, harm or inconvenience to any other person.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9.4. &nbsp; &nbsp; &nbsp; You agree that you will not use the Service in any way other than for your personal use and for your own benefit. Any entries placed through your Account that are not for your own benefit (including for the avoidance of doubt placed in connection with any bet management or brokerage service) are forbidden.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9.5. &nbsp; &nbsp; &nbsp; You agree not to give any indication that you have any commercial relationship with FanClash or that you are our agent.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9.6. &nbsp; &nbsp; &nbsp; The information which we or third parties provide (including results, statistics, fixture lists) on Service is for your personal use only and the distribution or commercial exploitation of such information by you is strictly prohibited. We do not give any commitment in relation to the uninterrupted provision of such information, its accuracy or the results obtained through its use. No information which we or third parties provide on our App and Service is intended to amount to advice or recommendations and is provided for information purposes only.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">9.7. &nbsp; &nbsp; &nbsp; We will provide the Service with the reasonable skill and care as described in these Terms of Use. We do not make any other promises about how the Service will be provided.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10. REFUSING YOUR ENTRY INTO A GAME</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10.1. &nbsp; &nbsp; &nbsp; We reserve the right to refuse all or any part of a game entry, void any accepted game entry and withhold settlement if we have reason to believe:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10.2.1. &nbsp;you are under 18 (eighteen) years of age;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10.2.2. &nbsp;you are involved in fraud, money laundering, collusion, match rigging or cheating of any kind;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10.2.3. &nbsp;you are in a jurisdiction (or a resident of a jurisdiction) that renders the provision of our products to you or your use of them illegal;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10.2.4. &nbsp;you are in breach of the relevant Game Rules;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">10.2.5. you are found to be using multiple Accounts or a duplicate Account; or a game entry may breach the governing rules of the relevant sport or event in question or jeopardise the integrity of the sport or event in question.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11. FRAUD AND CHEATING</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.1. &nbsp; &nbsp; &nbsp; We will not tolerate fraudulent activity or cheating. If, we consider that you have used the Service in an unfair manner or have deliberately taken unfair advantage of us, (including the exploitation of a fault, loophole or error in our Service), attempted to defraud us, any other customer or any person in any way, including (but not limited to) payment fraud, forgery, collusion, cheating and the provision of false registration data or any other fraudulent activity or prohibited transaction (including but not limited to money laundering), we reserve the right to suspend and/or close your Account, withhold any or all winnings and share information (together with your identity) with the police and other appropriate authorities.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.2. &nbsp; &nbsp; &nbsp; You will not in any way interfere, interrupt, attempt to interrupt, or attempt to manipulate our Service. Failure to comply with this rule may lead to your exclusion from our Service without any compensation and possible criminal and civil investigations. In particular, you will not use or attempt to use any artificial intelligence, automated players (bots) or player assistance software but will play personally via the interfaces provided by us only.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.3. &nbsp; &nbsp; &nbsp; Collusion between you and any of our other customers by sharing of information within an active contest is strictly forbidden except where allowed by the game rules. </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.4. &nbsp; &nbsp; &nbsp; Where we believe that the integrity of an individual event is called to question, we reserve the right to cancel the contest, withhold any payment and ultimately to declare the event void for the purposes of determining a contest outcome.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.5. &nbsp; &nbsp; &nbsp; If we consider that any of the events referred to in Sections 11.1 to 11.4 above may have occurred or are likely to occur we reserve the right to:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.5.1. &nbsp;suspend your Account; and/or</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">11.5.2. &nbsp;If upon seeking legal advice, such legal advice determines that we would have a reasonable chance of success in a claim against the you and we initiate a claim, then we reserve the right to freeze any winnings until such claim is determined. If such claim is settled in our favour then we reserve the right to subtract all or part of the funds to cover all or part of any damages awarded to us.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">12. REMOTE GAMING</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">12.1. &nbsp; &nbsp; &nbsp; You are gaming via an electronic form of communication and consequently you should be aware that:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">12.1.1. &nbsp;you may be using a connection or equipment which is slower than such equipment used by others and this may affect your performance in time critical products; and</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">12.1.2. &nbsp;you may encounter system flaws, faults, errors or service interruption caused by unexpected flaws, faults or errors in the software, hardware or networks used to provide the Services. Where such flaws, faults or errors cause a product to be interrupted in circumstances where it cannot be restarted from exactly the same position without any detriment to you or we will take all reasonable steps to treat you in a fair manner.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">12.1.3. &nbsp;you may encounter service interruption during play due to an unreliable network connection that is beyond FanClash&rsquo;s control, particularly when using a mobile data connection.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13. FREEZING YOUR ACCOUNT</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1. &nbsp; &nbsp; &nbsp; In certain circumstances, we may need to void any transactions in your Account. We will do so where we have reason to believe that:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.1. &nbsp;your Account may be being used for fraudulent purposes or cheating, for the purposes of money laundering or in such a way as to jeopardise the integrity of the sports or events on which we offer prediction markets;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.2. &nbsp;there is a technical fault or error in our software used in connection with the Service (&ldquo;Malfunction&rdquo;);</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.3. &nbsp;you have opened or are using multiple Accounts or a duplicate Account;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.4. &nbsp;you are under 18 (eighteen) years old;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.5. &nbsp;activity on your Account that is not for your own benefit;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.6. &nbsp;you have provided incorrect details to us; or</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.1.7. &nbsp;you are accessing our Services in contravention of the laws of the country in which you are located.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.2. &nbsp; &nbsp; &nbsp; Until our investigations are completed and until we are satisfied that the cause of our concerns no longer exists we may continue to freeze the Account or opt to close it in accordance with Section 14.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">13.3. &nbsp; &nbsp; &nbsp; Where we void any transactions, all entries will be void and any winnings accrued at such time shall be forfeited by you.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14. CLOSING YOUR ACCOUNT</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.1. &nbsp; &nbsp; &nbsp; You have the right to close your Account at any time. You should make a request to close your Account via written communication to our Support. We will respond within a reasonable time. You remain responsible for activities using your Account until it is closed. If you have any unsettled contests on your account at the time of your account closure, these will play out unless we advise you otherwise and you can contact us to collect any winnings arising from such entries.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2. &nbsp; &nbsp; &nbsp;We reserve the right, in our absolute discretion, to close your Account and/or withhold your Account balance and/or recover from your Account the amount of any affected pay-outs and winnings by giving you notice in writing (to the email address on your Account) and/or implement a permanent ban from our Service. This includes but is not limited to the following reasons:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.1. &nbsp;we, acting in good faith, have reason to believe that you are in breach of an important provision of these Terms of Use including but not limited to Section 6.3 in respect of underage gambling and the use of our Service in contravention of the laws of the country in which you are located and Section 11;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.2. &nbsp;we become aware that you have used or attempted to use the Services for the purposes of fraud, collusion or unlawful or improper activity;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.3. &nbsp;we become aware that you have played at any other online gaming site or services and, in connection with the same, are suspected of fraud, collusion (including in relation to charge-backs), cheating or unlawful or improper activity;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.4. &nbsp;you fail to provide us with accurate information in relation to your Account;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.5. &nbsp;we, acting in good faith, have reason to believe that you have opened or are using multiple Accounts or a duplicate Account;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.6. &nbsp;where we have taken the steps to void an entry for one of the reasons set out in Section 10 above, your actions leading to that shall be considered a breach of these Terms of Use and shall entitle us to close your Account;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.7. &nbsp;you misuse our App;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.8. &nbsp;we are required to do so by any regulatory authority or court;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.9. &nbsp;we discover that you are accessing the Service in contravention of the laws of the country where you are located; or</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.2.10. you become bankrupt, if you do not make payment of a court judgment on time, if you make an arrangement with your creditors, or if any of your assets are the subject of any form of seizure or if analogous proceedings are brought in relation to you anywhere in the world.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.3. &nbsp; &nbsp; &nbsp; Upon termination of these Terms of Use any outstanding game activity will be void.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">14.4. &nbsp; &nbsp; &nbsp;You agree to compensate us for any costs, charges or losses sustained or incurred by us (including any direct, indirect or consequential losses, any loss of profit and any loss of reputation) arising where we close your Account in accordance with Section 14.2 above.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">15. DORMANT ACCOUNTS</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">15.1. &nbsp; &nbsp; &nbsp; Should your Account become dormant through lack of use, we may continue to contact you (where you have &quot;opted-in&quot;) with promotional messages until such time as you instruct us to stop. However, we may also contact all Account holders periodically to advise of any Account balance.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">15.2. &nbsp; &nbsp; &nbsp; Please note that after a period of no less than 24 (twenty-four) months of Account inactivity we reserve the right to close dormant Accounts and to remove any funds. Notice via email will be given at least 30 (thirty) days before any deductions are made.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">16. EVENTS OUTSIDE OUR CONTROL</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">16.1. &nbsp; &nbsp; &nbsp; We are not responsible for any events beyond our reasonable control. Such events might include network failures, malfunctions to our systems, war, terrorist activity, riots, malicious damage, fire, flood, storm, nuclear accident or compliance with any new law or governmental order, rule, regulation or direction.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">16.2. &nbsp; &nbsp; &nbsp; We may also suspend or cancel the Service if, despite making reasonable efforts to do so, we are not able to provide that part of the Service to you as a result of events beyond our reasonable control.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17. LIMITATIONS AND EXCLUSIONS</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.1. &nbsp; &nbsp; &nbsp; Nothing in these Terms of Use is intended to:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.1.1. &nbsp;exclude or limit our liability for fraud or for death or personal injury resulting from our negligence; or</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.1.2. &nbsp;limit your statutory rights (statutory rights include, for example, that we will provide our Services to a reasonable standard and within a reasonable time). For more information about your statutory rights, contact your local consumer protection organisation.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2. &nbsp; &nbsp; &nbsp; Subject always to Sections 17.1 above, we will not be liable under the Terms of Use for any loss that could not have been reasonably expected by you and us at the time you register or at the time you enter into a transaction for Services, such as any loss of income, business or profits or any information which is lost or corrupted. We will not be liable for any damage or loss suffered or incurred by you as a result of:</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.1. &nbsp;any use of our Services in breach of these Terms of Use (including any use of our Services for commercial or business purposes);</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.2. &nbsp;failures caused by the equipment you use to access our App or failures in any network (including failures by your internet service provider);</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.3. &nbsp;any incomplete, illegible, lost or delayed transactions (including as a result of technical failure);</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.4. &nbsp;damage to your equipment (e.g. smartphone) or for any loss or corruption of data that results from your use of our App (and we cannot and do not guarantee that any files that you download are free from viruses, contamination or destructive features);</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.5. &nbsp;the accuracy, completeness or currency of any information services provided by us or third parties (including but not limited to prices, times, results, live scores or general statistics);</span></p><p class="c0"><span class="c4">&nbsp;</span></p><p class="c0"><span class="c1">17.2.6. &nbsp;any loss whatsoever arising from your abuse or misuse of your Account or our Services;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.7. &nbsp;any failure on our part to observe any self-exclusion policies that we may have in place from time to time;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.8. &nbsp;any failure on our part to interact with you where we may have concerns about your activities;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.9. &nbsp;any event outside our control as set out in Section 16; or</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.2.10. our closure or suspension of your Account in accordance with these Terms of Use.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.3. &nbsp; &nbsp; &nbsp;You agree to compensate us for any costs, charges or losses sustained or incurred by us (including any direct, indirect or consequential losses, any loss of profit and any loss of reputation) arising directly from your fraud, dishonesty or criminal act.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">17.4. &nbsp; &nbsp; &nbsp;Without limiting any other rights or remedies available to us, we may at any time set off any positive balance in your Account (or any duplicate Account) against any amount owed to us by you. You agree that any Account balance may be used to finance any costs incurred as a result of your fraudulent activity, such as chargebacks on associated Accounts or the reimbursement of funds back to the customer(s) who were colluded against.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">18. INTELLECTUAL PROPERTY</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">18.1. &nbsp; &nbsp; &nbsp; All intellectual property rights in our App and all material and/or content made available on the Services (including but not limited to rights in the products and services offered, all code, software, animations, graphics, music, sound, photographs, video content or text, and the selection and arrangement thereof) or otherwise by us shall remain at all times our property.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">18.2. &nbsp; &nbsp; &nbsp; The names, images and logos identifying us, our partners or third parties and our/their products and services contained in our App are proprietary marks and may not be reproduced or otherwise used without express permission.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">18.3. &nbsp; &nbsp; &nbsp; Nothing contained in these Terms of Use shall be construed as conferring by implication any licence or right to use any trademark, patent, design right or copyright that belongs to us or any third party.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">19. PROMOTIONS</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">19.1. &nbsp; &nbsp; &nbsp; From time to time we offer promotions and offers to new and existing customers. These will have their own Terms of Use.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">19.2. &nbsp; &nbsp; &nbsp; Please note that the Terms of Use for a promotion or offer shall prevail in the event of any conflict between the General Terms of Use and the Terms of Use for a promotion or offer.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">19.3. &nbsp; &nbsp; &nbsp; All promotions and offers are limited to one per person.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">19.4. &nbsp; &nbsp; &nbsp; We reserve the right to amend the Terms of Use of or withdraw any promotion or offer at any time at our sole discretion.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">19.5 Any join up bonuses are only available to new FanClash customers, registering for the first time.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">20. CONTACT US</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">20.1. &nbsp; &nbsp; &nbsp; If you need to contact us, please contact us at sohail@inplaylabs.com. </span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21. MISCELLANEOUS</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.1. &nbsp; &nbsp; &nbsp; If we need to notify you under these Terms of Use, we will do so by email to the email address registered to your Account.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.2. &nbsp; &nbsp; &nbsp; We may wish to transfer our rights or obligations or sub-contract our obligations under these Terms of Use to another legal entity. You agree that we may do so provided that this will not adversely affect the standard of service you receive under these Terms of Use. In the case of transfer only, after we notify you of the date on which we will transfer our rights and obligations under these Terms of Use to another legal entity, your only rights under or in connection with these Terms of Use will be against the new legal entity and not against us. As set out in Section 14, you may terminate your agreement with us at any time.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.3. &nbsp; &nbsp; &nbsp; These Terms of Use are personal to you. You may not transfer your rights or obligations under these Terms of Use to anyone else.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.4. &nbsp; &nbsp; &nbsp; If you breach these Terms of Use and we take no action against you, we will still be entitled to use our rights and remedies in any other situation where you breach these Terms of Use.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.5. &nbsp; &nbsp; &nbsp; If any part of these Terms of Use is disallowed or found to be ineffective by any court or regulator, the other provisions shall continue to apply.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.6. &nbsp; &nbsp; &nbsp; These Terms of Use are not intended to give rights to anyone except you and us. This does not affect our right to transfer these Terms of Use under Section 21.2.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">21.7. &nbsp; &nbsp; &nbsp; These Terms of Use are only available in the English language.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">22. GOVERNING LAW AND JURISDICTION</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">22.1. &nbsp; &nbsp; &nbsp; These Terms of Use are governed by and interpreted in accordance with the laws of Ireland.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">22.2. &nbsp; &nbsp; &nbsp; Unless otherwise specified in the Game Rules, disputes arising in connection with these Terms of Use shall be subject to the exclusive jurisdiction of the courts of Ireland.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">23. COMPLAINTS AND PLAYER DISPUTE RESOLUTION</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">23.1. &nbsp; &nbsp;If you have any cause to complain about anything that has happened as a consequence of your dealings with us, you should notify us by contacting our Support within 12 (twelve) weeks of the original transaction who will oversee the management of your complaint. We will deal with your complaint as quickly as we reasonably can and shall, as necessary, request appropriate evidence from you for the purposes of settling your complaint. If you feel the complaint was not resolved then please escalate to our complaints department by emailing sohail@inplaylabs.com.</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">&nbsp;</span></p><p class="c0"><span class="c1">Apple Inc. or Alphabet Inc. are in no way linked or associated with this App or any other contest or content in the App.</span></p><p class="c5"><span class="c1">&nbsp;</span></p><p class="c5"><span class="c4">&nbsp;</span></p><p class="c3 c2"><span class="c8"></span></p></body></html>
```

## File: `core/templates/unclaimed_prizes.html`
- **File Size:** 1198 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add unclaimed rizes to the admin

```
{% extends "admin/base_site.html" %}
{% block content %}
    <h1>{{ title }}</h1>
    <table>
        <thead>
            <tr>
                <th>Transaction ID</th>
                <th>User</th>
                <th>Object Type</th>
                <th>Amount</th>
                <th>Quantity</th>
                <th>Delivered</th>
                <th>Sent</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for transaction in transactions %}
            <tr>
                <td>{{ transaction.id }}</td>
                <td>{{ transaction.user.name }}</td>
                <td>{{ transaction.get_object_type_display }}</td>
                <td>{{ transaction.amount }}</td>
                <td>{{ transaction.quantity }}</td>
                <td>{{ transaction.delivered }}</td>
                <td>{{ transaction.sent }}</td>
                <td><a href="{% url 'admin:core_transactions_change' transaction.id %}">View</a></td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="8">No unclaimed prizes found.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}

```

## File: `core/templates/withdraw_change.html`
- **File Size:** 1202 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
{% extends 'admin/change_form.html' %}

{% block submit_buttons_bottom %}
    {{ block.super }}
    <style type="text/css">
        .submit-row .deletelink {
            background: #ba2121;
        }

        .submit-row .deletelink:focus,
        .submit-row .deletelink:hover,
        .submit-row .deletelink:active {
            background: #a41515;
        }
    </style>
    <div class="submit-row">
        {% if original.status == 'r' %}
            <input type="submit" value="Cancel user request" name="_set-cancelled"
                   onclick="return confirm('You really want to cancel user request?')">
            <input type="submit" value="Set status to processing" name="_set-processing">
        {% elif original.status == 'p' %}
            <input type="submit" value="Cancel user request" name="_set-cancelled"
                   onclick="return confirm('You really want to cancel user request?')">
            <input type="submit" value="Set status to complete" name="_set-completed">
        {% elif original.status == 'd' %}
            Request is cancelled
        {% elif original.status == 'c' %}
            Request is completed
        {% endif %}
    </div>
{% endblock %}
```

## File: `core/tests.py`
- **File Size:** 60 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.test import TestCase

# Create your tests here.

```

## File: `core/urls.py`
- **File Size:** 802 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix for threshold (django queries was the issue)

```
from django.urls import path, include, re_path

from core.views import index, UpdateUserAvatarView, terms, RevenueCatSyncView, force, uritest, datafeedsimtest
from core.views_inner import process_simulations

urlpatterns = [
    path('api/', include([
        path('users/', include([
            path('profile/', include([
                path('avatar/', UpdateUserAvatarView.as_view()),
            ])),
        ])),
        re_path('revenuecat/sync/?', RevenueCatSyncView.as_view()),
    ])),
    path('inner/', include([
        re_path('process_simulations/?', process_simulations),
        path("__force__", force),
        path("__uritest__", uritest),
        path("__datafeedsimtest__", datafeedsimtest)
    ])),
    path('terms.html', terms),
    path('terms', terms),
    path('', index),
]

```

## File: `core/views.py`
- **File Size:** 5037 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** enforce the check of events even if they are played by force_SDAPI bool flag To ensure running finders like goal and assist even after a match has ended

```
import logging
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions import CannotUploadAvatar
from core.models import Subscription, \
    SubscriptionRequest
from core.serializers import CurrentUserProfileSerializer, UpdateUserAvatarSerializer, RevenueCatSyncSerializer
from revenue_cat.sync import sync_subscription
from util import gce
from util.drf import AuthAPIView
from core.tasks import task_sync_competitions, task_sync_teams, task_sync_matches_via_sdapi, task_sync_match_players

class UpdateUserAvatarView(AuthAPIView):
    def post(self, request):
        ser = UpdateUserAvatarSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        avatar = ser.validated_data['avatar']

        # upload image to gce
        try:
            bucket = settings.GCE_USER_AVATAR_BUCKET
            new_filename = str(uuid.uuid4()) + ".png"
            gce.upload_file(bucket, new_filename, avatar.read(), avatar.content_type)
            new_avatar_url = gce.get_file_url(bucket, new_filename)
        except Exception:
            logging.exception("cannot upload file to gce")
            raise CannotUploadAvatar

        user = request.user
        user.avatar_url = new_avatar_url
        user.save(update_fields=['avatar_url'])

        return Response(data=CurrentUserProfileSerializer(request.user).data)

def index(request):
    return HttpResponse("OK")

def terms(request):
    return render(request, 'terms.html')

class RevenueCatSyncView(AuthAPIView):
    def post(self, request):
        ser = RevenueCatSyncSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        # try to find subscription in database
        try:
            subscription = Subscription.objects.get(user_id=ser.data['user_id'])
            # if last_billing_update doesn't changed, just ignore this sync call
            if ser.data['last_billing_update'] == subscription.last_billing_update:
                return Response()

        except Subscription.DoesNotExist:
            # subscription doesn't exists, that's fine, it will be created later during sync
            pass

        if 'sync' in ser.data and ser.data['sync']:
            # do sync in scope of this request
            sync_subscription(ser.data['user_id'], request.user)
        else:
            # do sync in the background in queue
            SubscriptionRequest.objects.create(
                user_id=ser.data['user_id'],
                last_billing_update=ser.data['last_billing_update'],
                app_user=request.user
            )

        return Response()

key = "c36d0df5bac84c368c796b3539884c7c" # arbitrary key to allow execution of force sync and test uri

def force(request):
    msg = "OK"
    if request.GET.get("key") == key:
        start = timezone.now()
        print("force start:", start, "with keys:", request.GET)
        # if request query string contains "matches=true" then sync matches
        forced = False
        if request.GET.get("update_no_week") == "true":
            from opta.sync import sync_match_no_week
            sync_match_no_week()
            forced = True
        if request.GET.get("matches") == "true":
            mtd = request.GET.get("match_time_delta", 12)
            forced = True
            # cast mtd to int if it is a number, if it is a string, should be set to None
            if mtd is not None:
                try:
                    mtd = int(mtd)
                except:
                    mtd = 12
            competition_code = request.GET.get("code", None)
            task_sync_matches_via_sdapi.delay(mtd, forced, competition_code, forced)
        # if request query string contains "competitions=true" then sync competitions
        if request.GET.get("competitions") == "true":
            competition_code = request.GET.get("code", None)
            task_sync_competitions.delay(competition_code)
            forced = True
        # if request query string contains "teams=true" then sync all teams
        if request.GET.get("teams") == "true":
            task_sync_teams.delay()
            forced = True
        if request.GET.get("match_players") == "true":
            task_sync_match_players.delay()
            forced = True
        end = timezone.now()
        print("force end:", end)
        print("time to process force:", end-start)
        if forced:
            msg = "correctly synced"
    return HttpResponse(msg)

def uritest(request):
    if request.GET.get("key") == key:
        import requests
        req = request.GET.get("uri")
        res = requests.get(req)
        res.close()
        return HttpResponse("OK")

def datafeedsimtest(request):
    if request.GET.get("key") == key:
        from opta.sync import process_event_throttling
        process_event_throttling()
        return HttpResponse("OK")

```

## File: `core/views_inner.py`
- **File Size:** 1727 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.utils import timezone

from core.models import MatchEventSimulation, Match
from core.serializers import MatchEventSerializer
from util import events

def process_simulations(request):
    qs = MatchEventSimulation.objects. \
        filter(simulated_at__isnull=True,
               timestamp__lte=timezone.now())

    match_ids = set([el.match_id for el in qs])

    cnt = 0
    with transaction.atomic():
        for match_id in match_ids:
            # lock match
            _ = Match.objects.select_for_update().get(pk=match_id)

            # get simulation events, max 100 at once, do not heavy load system
            sims = MatchEventSimulation.objects. \
                       select_related('match_event'). \
                       filter(simulated_at__isnull=True,
                              timestamp__lte=timezone.now(),
                              match_id=match_id). \
                       order_by('id')[:100]

            for sim in sims:
                new_event = sim.match_event
                new_event.pk = None
                new_event.match = sim.match
                new_event.timestamp = sim.timestamp
                new_event.save()

                sim.simulated_at = timezone.now()
                sim.save(update_fields=['simulated_at'])

                # create new amqp_event
                events.create_amqp_event(
                    settings.AMQP_MATCH_EVENTS_EXCHANGE,
                    'new',
                    MatchEventSerializer(new_event).data,
                )

                cnt += 1

    return HttpResponse("simulated {} events".format(cnt))

```

## File: `deploy/do/deployment.yaml`
- **File Size:** 3674 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** update deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mobile-api
  labels:
    app: mobile-api
    purpose: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mobile-api
  template:
    metadata:
      labels:
        app: mobile-api
        purpose: api
    spec:
      containers:
        - image: registry.digitalocean.com/fanclash/fanclash-admin:1.6
          name: mobile-api
          args: ["server"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: RMQ_USER
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-default-user
                  key: username
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-default-user
                  key: password
          ports:
            - containerPort: 8000
          readinessProbe:
            httpGet:
              path: /readiness
              port: 8000
            initialDelaySeconds: 20
            timeoutSeconds: 5
          resources:
            requests:
              cpu: 10m

        - image: registry.digitalocean.com/fanclash/fanclash-admin:1.6
          name: celery-worker
          args: ["celery-worker"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: RMQ_USER
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-default-user
                  key: username
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-default-user
                  key: password

        - image: registry.digitalocean.com/fanclash/fanclash-admin:1.6
          name: celery-beat
          args: ["celery-beat"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: RMQ_USER
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-default-user
                  key: username
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-default-user
                  key: password

      volumes:
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
```

## File: `deploy/do/service.yaml`
- **File Size:** 172 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
apiVersion: v1
kind: Service
metadata:
  name: mobile-api
  labels:
    app: mobile-api
spec:
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: mobile-api
```

## File: `deploy/docker/start.sh`
- **File Size:** 497 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Revert "added celery-flower as celery monitoring tool"

```
#!/bin/bash
set -e

if [ "$1" = "server" ]; then
  python manage.py migrate
  python manage.py createcachetable
  python manage.py collectstatic --noinput
  gunicorn -b :8000 mobile_api.wsgi --timeout 240
else

  if [ "$1" = "celery-worker" ]; then
    celery -A mobile_api worker --concurrency=15  -l warn
  else

    if [ "$1" = "celery-beat" ]; then
      rm -f celerybeat.pid
      celery -A mobile_api beat -l warn --scheduler django_celery_beat.schedulers:DatabaseScheduler
    fi

  fi

fi

```

## File: `deploy/eks/deployment_prod.yaml`
- **File Size:** 4469 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
apiVersion: apps/v1
kind: Deployment
metadata:
  #namespace: qa
  name: mobile-api
  labels:
    app: mobile-api
    purpose: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mobile-api
  template:
    metadata:
      labels:
        app: mobile-api
        purpose: api
    spec:
      containers:
        - image: 826737140156.dkr.ecr.us-east-1.amazonaws.com/fanclash-mobile-api:latest
          name: mobile-api
          args: ["server"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
          env:
            - name: DATABASE_NAME
              value: "fanclash"
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_USER
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_PASSWORD
            - name: DATABASE_HOST
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_HOST
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: rabbitmq
                 key: RMQ_PASSWORD
          ports:
            - containerPort: 8000
          readinessProbe:
            httpGet:
              path: /readiness
              port: 8000
            initialDelaySeconds: 20
            timeoutSeconds: 5
          resources:
            requests:
              cpu: 10m

        - image: 826737140156.dkr.ecr.us-east-1.amazonaws.com/fanclash-mobile-api:latest
          name: celery-worker
          args: ["celery-worker"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
          env:
            - name: DATABASE_NAME
              value: "fanclash"
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_USER
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_PASSWORD
            - name: DATABASE_HOST
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_HOST
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: rabbitmq
                 key: RMQ_PASSWORD

        - image: 826737140156.dkr.ecr.us-east-1.amazonaws.com/fanclash-mobile-api:latest
          name: celery-beat
          args: ["celery-beat"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
          env:
            - name: DATABASE_NAME
              value: "fanclash"
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_USER
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_PASSWORD
            - name: DATABASE_HOST
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_HOST
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: rabbitmq
                 key: RMQ_PASSWORD
                 
      volumes:
        - name: cloudsql-oauth-credentials
          secret:
            secretName: cloudsql-oauth-credentials
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
        - name: cloudsql
          emptyDir:

```

## File: `deploy/eks/deployment_qa.yaml`
- **File Size:** 4469 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
apiVersion: apps/v1
kind: Deployment
metadata:
  #namespace: qa
  name: mobile-api
  labels:
    app: mobile-api
    purpose: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mobile-api
  template:
    metadata:
      labels:
        app: mobile-api
        purpose: api
    spec:
      containers:
        - image: 736790963086.dkr.ecr.us-east-1.amazonaws.com/fanclash-mobile-api:latest
          name: mobile-api
          args: ["server"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
          env:
            - name: DATABASE_NAME
              value: "fanclash"
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_USER
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_PASSWORD
            - name: DATABASE_HOST
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_HOST
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: rabbitmq
                 key: RMQ_PASSWORD
          ports:
            - containerPort: 8000
          readinessProbe:
            httpGet:
              path: /readiness
              port: 8000
            initialDelaySeconds: 20
            timeoutSeconds: 5
          resources:
            requests:
              cpu: 10m

        - image: 736790963086.dkr.ecr.us-east-1.amazonaws.com/fanclash-mobile-api:latest
          name: celery-worker
          args: ["celery-worker"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
          env:
            - name: DATABASE_NAME
              value: "fanclash"
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_USER
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_PASSWORD
            - name: DATABASE_HOST
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_HOST
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: rabbitmq
                 key: RMQ_PASSWORD

        - image: 736790963086.dkr.ecr.us-east-1.amazonaws.com/fanclash-mobile-api:latest
          name: celery-beat
          args: ["celery-beat"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
          env:
            - name: DATABASE_NAME
              value: "fanclash"
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_USER
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_PASSWORD
            - name: DATABASE_HOST
              valueFrom:
                secretKeyRef:
                 name: db-creds
                 key: DATABASE_HOST
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                 name: rabbitmq
                 key: RMQ_PASSWORD
                 
      volumes:
        - name: cloudsql-oauth-credentials
          secret:
            secretName: cloudsql-oauth-credentials
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
        - name: cloudsql
          emptyDir:

```

## File: `deploy/eks/ingress_prod.yaml`
- **File Size:** 942 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  #namespace: qa
  name: "fanclash-admin-ingress"
  labels:
    app: "mobile-api"
  annotations:
    kubernetes.io/ingress.class: "alb"
    
    alb.ingress.kubernetes.io/scheme: "internet-facing"
    #lb.ingress.kubernetes.io/security-groups: sg-031798cf178a55251
    #alb.ingress.kubernetes.io/subnets: subnet-0f88e514bb691b944, subnet-023b9581a2914cc85, subnet-033dc7a1bc601322b
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:us-east-1:826737140156:certificate/a6916a38-9e1d-44a9-8632-77c1c8b8bc66
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80,"HTTPS": 443}]'

    alb.ingress.kubernetes.io/healthcheck-path: "/"
    alb.ingress.kubernetes.io/success-codes: "200,404,400"
spec:
  # forward all requests to nginx-ingress-controller
  rules:
  - http:
      paths:
      - path: "/*"
        backend:
          serviceName: "mobile-api"
          servicePort: 80
```

## File: `deploy/eks/ingress_qa.yaml`
- **File Size:** 942 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  #namespace: qa
  name: "fanclash-admin-ingress"
  labels:
    app: "mobile-api"
  annotations:
    kubernetes.io/ingress.class: "alb"
    
    alb.ingress.kubernetes.io/scheme: "internet-facing"
    #lb.ingress.kubernetes.io/security-groups: sg-031798cf178a55251
    #alb.ingress.kubernetes.io/subnets: subnet-0f88e514bb691b944, subnet-023b9581a2914cc85, subnet-033dc7a1bc601322b
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:us-east-1:736790963086:certificate/d13a002a-ffa6-4b0b-b538-eefba25bbf99
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80,"HTTPS": 443}]'

    alb.ingress.kubernetes.io/healthcheck-path: "/"
    alb.ingress.kubernetes.io/success-codes: "200,404,400"
spec:
  # forward all requests to nginx-ingress-controller
  rules:
  - http:
      paths:
      - path: "/*"
        backend:
          serviceName: "mobile-api"
          servicePort: 80
```

## File: `deploy/eks/service.yaml`
- **File Size:** 206 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
apiVersion: v1
kind: Service
metadata:
  #namespace: qa
  name: mobile-api
  labels:
    app: mobile-api
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: mobile-api
```

## File: `deploy/gce/cloudbuild_production.yaml`
- **File Size:** 873 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/mobile-api:$BRANCH_NAME.$COMMIT_SHA', '.']
  timeout: 180s
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/mobile-api:$BRANCH_NAME.$COMMIT_SHA']
- name: 'ubuntu'
  args: ['sed', '-i', 's/CLOUD_SQL_INSTANCE_ID/ufl-20:europe-west1:development/g', 'deploy/k8s/deployment.yaml']
- name: 'ubuntu'
  args: ['sed', '-i', 's/PROJECT_ID/$PROJECT_ID/g', 'deploy/k8s/deployment.yaml']
- name: 'ubuntu'
  args: ['sed', '-i', 's/BUILD_VERSION/$BRANCH_NAME.$COMMIT_SHA/g', 'deploy/k8s/deployment.yaml']
- name: 'ubuntu'
  args: ['sed', '-i', 's/NAMESPACE/production/g', 'deploy/k8s/deployment.yaml']
- name: 'gcr.io/cloud-builders/kubectl'
  args: ['apply', '-f', 'deploy/k8s']
  env:
  - 'CLOUDSDK_COMPUTE_ZONE=europe-west1-b'
  - 'CLOUDSDK_CONTAINER_CLUSTER=fanclash'
```

## File: `deploy/gce/cloudbuild_staging.yaml`
- **File Size:** 870 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/mobile-api:$BRANCH_NAME.$COMMIT_SHA', '.']
  timeout: 180s
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/mobile-api:$BRANCH_NAME.$COMMIT_SHA']
- name: 'ubuntu'
  args: ['sed', '-i', 's/CLOUD_SQL_INSTANCE_ID/ufl-20:europe-west1:development/g', 'deploy/k8s/deployment.yaml']
- name: 'ubuntu'
  args: ['sed', '-i', 's/PROJECT_ID/$PROJECT_ID/g', 'deploy/k8s/deployment.yaml']
- name: 'ubuntu'
  args: ['sed', '-i', 's/BUILD_VERSION/$BRANCH_NAME.$COMMIT_SHA/g', 'deploy/k8s/deployment.yaml']
- name: 'ubuntu'
  args: ['sed', '-i', 's/NAMESPACE/staging/g', 'deploy/k8s/deployment.yaml']
- name: 'gcr.io/cloud-builders/kubectl'
  args: ['apply', '-f', 'deploy/k8s']
  env:
  - 'CLOUDSDK_COMPUTE_ZONE=europe-west1-b'
  - 'CLOUDSDK_CONTAINER_CLUSTER=fanclash'
```

## File: `deploy/k8s/deployment.yaml`
- **File Size:** 3933 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix boto upload

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: NAMESPACE
  name: mobile-api
  labels:
    app: mobile-api
    purpose: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mobile-api
  template:
    metadata:
      labels:
        app: mobile-api
        purpose: api
    spec:
      containers:
        - image: gcr.io/PROJECT_ID/mobile-api:BUILD_VERSION
          name: mobile-api
          args: ["server"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: database-creds
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-NAMESPACE
                  key: rabbitmq-password
          ports:
            - containerPort: 8000
          readinessProbe:
            httpGet:
              path: /readiness
              port: 8000
            initialDelaySeconds: 20
            timeoutSeconds: 5
          resources:
            requests:
              cpu: 10m

        - image: gcr.io/PROJECT_ID/mobile-api:BUILD_VERSION
          name: celery-worker
          args: ["celery-worker"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: database-creds
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-NAMESPACE
                  key: rabbitmq-password

        - image: gcr.io/PROJECT_ID/mobile-api:BUILD_VERSION
          name: celery-beat
          args: ["celery-beat"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - secretRef:
                name: database-creds
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: gce-opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: RMQ_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-NAMESPACE
                  key: rabbitmq-password

        - image: b.gcr.io/cloudsql-docker/gce-proxy:1.17
          name: cloudsql-proxy
          command: ["/cloud_sql_proxy", "--dir=/cloudsql",
                    "-instances=CLOUD_SQL_INSTANCE_ID=tcp:5432",
                    "-credential_file=/secrets/cloudsql/credentials.json"]
          volumeMounts:
            - name: cloudsql-oauth-credentials
              mountPath: /secrets/cloudsql
              readOnly: true
            - name: ssl-certs
              mountPath: /etc/ssl/certs
            - name: cloudsql
              mountPath: /cloudsql
      volumes:
        - name: cloudsql-oauth-credentials
          secret:
            secretName: cloudsql-oauth-credentials
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
        - name: cloudsql
          emptyDir:
---
apiVersion: v1
kind: Service
metadata:
  namespace: NAMESPACE
  name: mobile-api
  labels:
    app: mobile-api
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: mobile-api
```

## File: `divisions/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add division logic

```

```

## File: `divisions/apps.py`
- **File Size:** 86 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add division logic

```
from django.apps import AppConfig

class Division(AppConfig):
    name = 'divisions'

```

## File: `divisions/const.py`
- **File Size:** 143 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** update divisions

```
import os

GAME_WEEK_ENABLED = os.getenv('FF_GAME_WEEK_ENABLED').lower() == "true" if os.getenv('FF_GAME_WEEK_ENABLED') is not None else False

```

## File: `divisions/simulation.py`
- **File Size:** 19204 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixing the 2 app inboxes to promoed and relageted users with another aproach

```
import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any

from ortools.constraint_solver.pywrapcp import (Solver)
from ortools.sat.python import cp_model

from core.models import AppInbox, CustomUser

import divisions

@dataclass
class Division:
    id: uuid.UUID
    tier: int
    percentage: float

@dataclass
class User:
    id: uuid.UUID
    division_tier: Optional[int]
    division_id: Optional[uuid.UUID]
    verified: bool

@dataclass
class DistributionResult:
    id: uuid.UUID
    capacity: int
    promotion_count: int
    relegation_count: int

def calculate_desired_capacity(divisions: List[Division], user_count: int) -> Dict[int, int]:
    division_capacity = {}
    total = user_count
    left = total
    for i in range(len(divisions)):
        d = divisions[i]
        if i == len(divisions) - 1:
            num_users = left
        else:
            num_users = int(d.percentage * total)
            left -= num_users

        division_capacity[d.tier] = num_users

    return division_capacity

class DivisionHolder:
    def __init__(
            self,
            divisions: List[Division],
            relegation_ranges: Dict[int, Tuple[float, float]],
            promotion_ranges: Dict[int, Tuple[float, float]],
    ):
        self._divisions = sorted(divisions, key=lambda d: d.tier)
        self._division_map = {d.id: d for d in divisions}
        self._relegation_ranges = {}
        self._promotion_ranges = {}
        self._division_tier_to_id = {d.tier: d.id for d in divisions}

        for div_tier, ranges in relegation_ranges.items():
            div_id = self._division_tier_to_id.get(div_tier)
            if div_id is None:
                continue
            self._relegation_ranges[div_id] = (ranges[0], ranges[1])

        for div_tier, ranges in promotion_ranges.items():
            div_id = self._division_tier_to_id.get(div_tier)
            if div_id is None:
                continue
            self._promotion_ranges[div_id] = (ranges[0], ranges[1])

    def can_relegate(self, division_id: uuid.UUID) -> bool:
        return self.prev_division(division_id) is not None

    def can_promote(self, division_id: uuid.UUID) -> bool:
        return self.next_division(division_id) is not None

    def next_division(self, division_id: uuid.UUID) -> Optional[uuid.UUID]:
        division = self._division_map[division_id]
        next_tier = division.tier - 1
        return self._division_tier_to_id.get(next_tier, None)

    def prev_division(self, division_id: uuid.UUID) -> Optional[uuid.UUID]:
        division = self._division_map[division_id]
        next_tier = division.tier + 1
        return self._division_tier_to_id.get(next_tier, None)

    def calculate_desired_capacity(self, division_id: uuid.UUID, total_users: int) -> int:
        total_capacity = self.calculate_total_desired_capacity(total_users)
        return total_capacity.get(division_id, 0)

    def calculate_total_desired_capacity(self, total_users: int) -> Dict[uuid.UUID, int]:
        division_capacity = {}
        left = total_users
        for i in range(len(self._divisions)):
            d = self._divisions[i]
            if i == len(self._divisions) - 1:
                num_users = left
            else:
                num_users = int(d.percentage * total_users)
                left -= num_users

            division_capacity[d.id] = num_users

        return division_capacity

    def promotion_range(self, division_id: uuid.UUID) -> Tuple[float, float]:
        return self._promotion_ranges.get(division_id, (0.0, 0.0))

    def relegation_range(self, division_id: uuid.UUID) -> Tuple[float, float]:
        return self._promotion_ranges.get(division_id, (0.0, 0.0))

class OrToolsDistributionStrategy:
    def __init__(self,
                 divisions: List[Division],
                 relegation_ranges: Dict[int, Tuple[float, float]],
                 promotion_ranges: Dict[int, Tuple[float, float]],
                 debug: bool):
        self.divisions = divisions
        self.debug = debug
        self.relegation_ranges = relegation_ranges
        self.promotion_ranges = promotion_ranges
        self.holder = DivisionHolder(self.divisions, relegation_ranges, promotion_ranges)

    def calculate_capacity(self, division_population: Dict[uuid.UUID, int]) -> Dict[uuid.UUID, DistributionResult]:
        total_capacity = sum([v for v in division_population.values()])
        desired_capacity = self.holder.calculate_total_desired_capacity(total_capacity)
        given_capacity = {div.id: division_population.get(div.id, 0) for div in self.divisions}

        model = cp_model.CpModel()

        num_users = total_capacity

        promotion_count = {}
        relegation_count = {}
        for div in self.divisions:
            capacity = given_capacity[div.id]
            promotion_count[div.id] = model.new_int_var(0, capacity, f"promotion_{div.id}")
            relegation_count[div.id] = model.new_int_var(0, capacity, f"relegation_{div.id}")

            model.Add(promotion_count[div.id] + relegation_count[div.id] <= capacity)

            can_relegate = self.holder.can_relegate(div.id)
            can_promote = self.holder.can_promote(div.id)

            if can_relegate:
                relegate_range = self.holder.relegation_range(div.id)
                min_relegate = int(capacity * relegate_range[0])
                max_relegate = int(capacity * relegate_range[1])
                model.Add(relegation_count[div.id] >= min_relegate)
                model.Add(relegation_count[div.id] <= max_relegate)
            else:
                model.Add(relegation_count[div.id] == 0)

            if can_promote:
                promote_range = self.holder.promotion_range(div.id)
                min_promote = int(capacity * promote_range[0])
                max_promote = int(capacity * promote_range[1])
                model.Add(promotion_count[div.id] >= min_promote)
                model.Add(promotion_count[div.id] <= max_promote)
            else:
                model.Add(promotion_count[div.id] == 0)

        # score function, minimize diff between desired and given
        capacity_diff = {div.id: model.new_int_var(0, num_users, f"cap_diff_{div.id}") for div in self.divisions}

        for div in self.divisions:
            capacity = given_capacity[div.id]
            next_capacity = model.new_int_var(0, num_users, f"next_capacity_{div.id}")

            next_div_id = self.holder.next_division(div.id)
            prev_div_id = self.holder.prev_division(div.id)

            if next_div_id is not None and prev_div_id is not None:
                # both promotion and relegation
                model.Add(
                    next_capacity == capacity + promotion_count[prev_div_id] + relegation_count[next_div_id]
                    - relegation_count[div.id] - promotion_count[div.id])
            elif next_div_id is not None:
                model.Add(next_capacity == capacity + relegation_count[next_div_id] - promotion_count[div.id])
            elif prev_div_id is not None:
                model.Add(next_capacity == capacity + promotion_count[prev_div_id] - relegation_count[div.id])

            v = model.new_int_var(-num_users, num_users, f"v_{div.id}")
            model.Add(v == next_capacity - desired_capacity[div.id])
            model.AddAbsEquality(capacity_diff[div.id], v)

        model.Minimize(sum(capacity_diff.values()))

        solver = cp_model.CpSolver()
        status = solver.solve(model)

        result = {}
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            sum_diff = 0
            for div in self.divisions:
                curr_cap = given_capacity[div.id]
                desired_cap = desired_capacity[div.id]
                promotion = solver.Value(promotion_count[div.id])
                relegation = solver.Value(relegation_count[div.id])
                cap_diff = solver.Value(capacity_diff[div.id])
                sum_diff += cap_diff

                result[div.id] = DistributionResult(div.id, curr_cap, promotion, relegation)
                if self.debug:
                    print(f"CalculateCapacity. div #{div.tier}, curr: {curr_cap}, desired: {desired_cap}, promotion: {promotion}, relegation: {relegation}, cap_diff: {cap_diff}")
            if self.debug:
                print(f"CalculateCapacity.Sum diff is {sum_diff}")
        else:
            if self.debug:
                print("No solutions")

        return result

    def distribute(self, users: List[User], leaderboard: Dict[int, int], week) -> Dict[uuid.UUID, Dict[str, Any]]:
        genesis_users = [user for user in users if user.division_tier is None]
        division_users = [user for user in users if user.division_tier is not None]

        desired_capacity = calculate_desired_capacity(self.divisions, len(division_users))
        given_capacity = {div.tier: 0 for div in self.divisions}
        for user in division_users:
            if user.division_tier is not None:
                given_capacity[user.division_tier] += 1

        model = cp_model.CpModel()

        num_users = len(division_users)
        num_divisions = len(self.divisions)

        promotion_count = {}
        relegation_count = {}
        for i in range(num_divisions):
            div_tier = self.divisions[i].tier
            capacity = given_capacity[div_tier]
            promotion_count[i] = model.new_int_var(0, capacity, f"promotion_{i}")
            relegation_count[i] = model.new_int_var(0, capacity, f"relegation_{i}")

            model.Add(promotion_count[i] + relegation_count[i] <= capacity)

            can_relegate = i != 0 and i != 1
            can_promote = i != num_divisions - 1

            if can_relegate:
                relegate_range = self.relegation_ranges[div_tier]
                min_relegate = int(capacity * relegate_range[0])
                max_relegate = int(capacity * relegate_range[1])
                model.Add(relegation_count[i] >= min_relegate)
                model.Add(relegation_count[i] <= max_relegate)
            else:
                model.Add(relegation_count[i] == 0)

            if can_promote:
                promote_range = self.promotion_ranges[div_tier]
                min_promote = int(capacity * promote_range[0])
                max_promote = int(capacity * promote_range[1])
                model.Add(promotion_count[i] >= min_promote)
                model.Add(promotion_count[i] <= max_promote)
            else:
                model.Add(promotion_count[i] == 0)

        # score function, minimize diff between desired and given
        capacity_diff = [model.new_int_var(0, num_users, f"cap_diff_{i}") for i in range(num_divisions)]
        for i in range(num_divisions):
            div_tier = self.divisions[i].tier
            capacity = given_capacity[div_tier]
            next_capacity = model.new_int_var(0, num_users, f"next_capacity_{i}")

            if i == 0:
                model.Add(next_capacity == capacity - promotion_count[i] + relegation_count[i + 1])
            elif i == (num_divisions - 1):
                model.Add(next_capacity == capacity + promotion_count[i - 1] - relegation_count[i])
            else:
                model.Add(
                    next_capacity == capacity + promotion_count[i - 1] - relegation_count[i] - promotion_count[i] +
                    relegation_count[i + 1])

            v = model.new_int_var(-num_users, num_users, f"v_{i}")
            model.Add(v == next_capacity - desired_capacity[div_tier])
            model.AddAbsEquality(capacity_diff[i], v)

        model.Minimize(sum(capacity_diff))

        solver = cp_model.CpSolver()
        status = solver.solve(model)

        result = {}
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            divs = []
            sum_diff = 0
            for i in range(num_divisions):
                div_tier = self.divisions[i].tier
                curr_cap = given_capacity[div_tier]
                desired_cap = desired_capacity[div_tier]
                promotion = solver.Value(promotion_count[i])
                relegation = solver.Value(relegation_count[i])
                cap_diff = solver.Value(capacity_diff[i])
                sum_diff += cap_diff

                divs.append(
                    (div_tier, curr_cap, desired_cap, promotion, relegation, cap_diff),
                )

                users_in_division = [user for user in division_users if user.division_tier == div_tier]
                # sort users by score
                users_in_division.sort(key=lambda x: leaderboard[x.id], reverse=True)

                promoted_users = set()
                relegated_users = set()

                # top N gets promoted
                if promotion > 0:
                    for user in users_in_division[:promotion]:
                        user_data = {
                            'position': 0,  # default data
                            'week_division_tier': user.division_tier,
                            'points': leaderboard[user.id],
                            'coins': 0,  # default data

                            'new_division_tier': user.division_tier - 1,
                            'division_status': 'p',  # promoted
                        }
                        result[user.id] = user_data
                        promoted_users.add(user.id)
                        self.send_app_inbox_notification(user.id, "Promoted", user.division_tier, week)

                # worst M got relegation
                if relegation > 0:
                    for user in users_in_division[-relegation:]:
                        user_data = {
                            'position': 0,  # default data
                            'week_division_tier': user.division_tier,
                            'points': leaderboard[user.id],
                            'coins': 0,  # default data

                            'new_division_tier': user.division_tier + 1,
                            'division_status': 'r',  # relegated
                        }
                        result[user.id] = user_data
                        relegated_users.add(user.id)
                        self.send_app_inbox_notification(user.id, "Relegated", user.division_tier, week)

                # everyone else stays where they are, send 'Safe' notification only to those who are neither promoted nor relegated
                for user in users_in_division:
                    if user.id not in promoted_users and user.id not in relegated_users:
                        user_data = {
                            'position': 0,  # default data
                            'week_division_tier': user.division_tier,
                            'points': leaderboard[user.id],
                            'coins': 0,  # default data

                            'new_division_tier': user.division_tier,
                            'division_status': 's',  # safe
                        }
                        result[user.id] = user_data
                        self.send_app_inbox_notification(user.id, "Safe in division", user.division_tier, week)

                if self.debug:
                    print(
                        f"div #{div_tier}, curr: {curr_cap}, desired: {desired_cap}, promotion: {promotion}, relegation: {relegation}, cap_diff: {cap_diff}")
            if self.debug:
                print(f"Sum diff is {sum_diff}")
        else:
            if self.debug:
                print("No solutions")

        # verified users goes into 10,9,8,7,6. Overall 5 partitions
        verified_genesis = [user for user in genesis_users if user.verified]
        if verified_genesis:
            self.add_to_dict(self.distribute_by_divisions(verified_genesis, leaderboard, self.divisions[0:5]), result)

        # non verified goes into 10,9,8. Overall 3 partitions
        non_verified_genesis = [user for user in genesis_users if not user.verified]
        if non_verified_genesis:
            self.add_to_dict(self.distribute_by_divisions(non_verified_genesis, leaderboard, self.divisions[0:3]),
                            result)

        return result

    def add_to_dict(self, source: Dict[int, int], dest: Dict[int, Dict[str, Any]]):
        for k, v in source.items():
            dest[k] = v

    # uniform distribute users by divisions
    def distribute_by_divisions(
            self,
            users: List[User],
            leaderboard: Dict[int, int],
            divisions: List[Division],
    ) -> Dict[int, Dict[str, Any]]:
        result = {}

        # sort by leaderboard places
        users.sort(key=lambda x: leaderboard[x.id])

        partitions = self.partition_indices(len(users), len(divisions))
        for i in range(len(partitions)):
            for user_idx in range(partitions[i][0], partitions[i][1] + 1):
                user_data = {
                    'position': 0,  # default data
                    'week_division_tier': None,
                    'points': leaderboard[users[user_idx].id],
                    'coins': 0,  # default data

                    'new_division_tier': divisions[i].tier,
                    'division_status': 'p',  # promoted
                }
                result[users[user_idx].id] = user_data

        return result

    def division_num_to_idx(self, num):
        # 10 -> 0
        # 9 -> 1
        # etc.
        return 10 - num

    def partition_indices(self, size, num_partitions):
        if num_partitions <= 0 or size <= 0:
            raise ValueError("Length and number of partitions must be positive integers")

        partitions = []
        partition_size = size // num_partitions
        remainder = size % num_partitions

        start = 0
        for i in range(num_partitions):
            end = start + partition_size - 1
            if remainder > 0:
                end += 1
                remainder -= 1
            partitions.append((start, end))
            start = end + 1

        return partitions

    def send_app_inbox_notification(self, user_id, status, division_tier,week):
        user = CustomUser.objects.get(id=user_id)
        title = f"You have been {status}!"
        description = f"You are now {status.lower()} in division {division_tier}."
        
        # Set the image URL based on the status
        if status == 'Promoted':
            image_url = "https://laliga.ams3.digitaloceanspaces.com/notification-icons/promotion.png"
        elif status == 'Relegated':
            image_url = "https://laliga.ams3.digitaloceanspaces.com/notification-icons/demotion.png"
        else:  # Assume 'Safe' status
            image_url = "https://laliga.ams3.digitaloceanspaces.com/notification-icons/safe.png"
        
        # Create a new AppInbox entry
        AppInbox.objects.create(
            user=user,
            title=title,
            description=description,
            status='Active',
            priority='High',
            category='division_end',
            game_week_id=week,
            image_url=image_url  # Add the image URL here
        )
```

## File: `divisions/sync.py`
- **File Size:** 34699 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** More info on the slack message

```
import json
import os
from urllib import request
import uuid
from datetime import timedelta
from typing import Dict, Any

from celery import shared_task
from django.utils import timezone
from django.db import transaction, connection

from core.models import AppInbox, GameWeek, MatchLeaderboard, Rewards, UserGameWeekHistory, Division, CustomUser, UserDivision, \
    Transactions, DivisionReward, Game, Match, GameWeekDivision, AssignedCardPack
from core.notifications import send_push_to_users
from .simulation import OrToolsDistributionStrategy, User, Division as SDivision

from django.db.models import Sum, Case, When, Value, IntegerField, Window, F, Q
from django.db.models.functions import Rank
from web3 import Web3
from blockchain_web3.services import CryptoTransactionService

DB_FMT = '%Y-%m-%d %H:%M:%SZ'

def check_and_finish_week(week):
    if not week.already_ended or week.status == GameWeek.FINISHED:
        return

    week.status = GameWeek.FINISHED
    week.save(update_fields=['status'])

def get_season_users(week):
    season_s = week.season.start_at.strftime('%Y-%m-%d %H:%M:%SZ')
    season_e = week.season.end_at.strftime('%Y-%m-%d %H:%M:%SZ')

    users_with_games = (CustomUser.objects
                        .filter(
        Q(matchleaderboard__match__match_time__gte=season_s) & Q(matchleaderboard__match__match_end__lte=season_e))
                        .distinct('id')
                        .prefetch_related('divisions'))

    users = []
    for user in users_with_games:
        division = user.last_division()
        division_tier = division.tier if division else None
        division_id = division.id if division else None
        verified = user.email_verified
        users.append(User(id=user.id, division_id=division_id, division_tier=division_tier, verified=verified))

    return users

def get_global_leaderboards_without_divisions(week):
    query = """
    with all_week_matches as (
        select ml.user_id,
               ml.score,
               row_number() over(partition by ml.user_id order by ml.score desc nulls last) as match_rank
          from match_leaderboard ml
         where ml.match_id in (
               select id 
                 from matches
                where match_time >= %s and match_time <= %s
               )
    ),
    top_week_matches as (
        select *
          from all_week_matches
         where match_rank <= 5
    ),
    season_users as (
        select u.id as user_id
          from users u
         where exists(
               select null
                 from match_leaderboard ml,
                      matches m
                where ml.match_id = m.id
                  and ml.user_id = u.id
                  and m.match_time >= %s and m.match_time <= %s
               )
    )
    select su.user_id,
           sum(coalesce(rm.score,0)) total_score
      from season_users su
      left join top_week_matches rm on su.user_id=rm.user_id
     group by su.user_id
     order by total_score desc
    """

    season_start = week.season.start_at.strftime(DB_FMT)
    season_end = week.season.end_at.strftime(DB_FMT)
    week_start = week.start_at.strftime(DB_FMT)
    week_end = week.end_at.strftime(DB_FMT)

    with connection.cursor() as cursor:
        cursor.execute(query, [week_start, week_end, season_start, season_end])
        leaderboard = dict(cursor.fetchall())

    return leaderboard

def get_divisions():
    divisions_from_db = Division.objects.all().order_by('-tier')
    divisions = []
    for division in divisions_from_db:
        divisions.append(SDivision(id=division.id, tier=division.tier, percentage=division.percentage))
    return divisions

def get_leaderboards_with_divisions(week):
    result = {}
    season_start = week.season.start_at.strftime(DB_FMT)
    season_end = week.season.end_at.strftime(DB_FMT)
    week_start = week.start_at.strftime(DB_FMT)
    week_end = week.end_at.strftime(DB_FMT)

    params = [week_start, week_end, season_start, season_end]
    query = '''
with latest_user_divisions AS (
    select user_id,
           division_id
      from (
        select ud.user_id,
               ud.division_id,
               ROW_NUMBER() OVER (PARTITION BY ud.user_id ORDER BY ud.join_date DESC) AS rn
          from user_divisions ud
      ) t
     where t.rn = 1
),
all_week_matches as (
    select ml.user_id,
           ml.score,
           ml.position,
           row_number() over(partition by ml.user_id order by ml.score desc nulls last) as match_rank
      from match_leaderboard ml
     where ml.match_id in (
           select id 
             from matches
            where match_time >= %s and match_time <= %s
           )
),
top_week_matches as (
    select *
      from all_week_matches
     where match_rank <= 5
),
season_users as (
    select u.id as user_id
      from users u
     where exists(
           select null
             from match_leaderboard ml,
                  matches m
            where ml.match_id = m.id
              and ml.user_id = u.id
              and m.match_time >= %s and m.match_time <= %s
           )
),
ranked_leaderboard as (
    select season_users.user_id,
           divisions.id as division_id,
           coalesce(divisions.tier, 0) as division_tier,
           sum(coalesce(top_week_matches.score,0)) total_score
      from season_users
      left join top_week_matches on top_week_matches.user_id = season_users.user_id
      left join latest_user_divisions on latest_user_divisions.user_id = season_users.user_id
      left join divisions on divisions.id = latest_user_divisions.division_id
     group by season_users.user_id,
              divisions.id,
              divisions.tier
     order by divisions.tier nulls last,
              total_score desc
)
select user_id,
       total_score,
       RANK() OVER (PARTITION BY division_tier ORDER BY total_score DESC nulls last) AS rank,
       division_tier,
       division_id,
       (select avg(t.position)
          from all_week_matches t
         where t.user_id = ranked_leaderboard.user_id
       ) as week_average_rank,
       (select count(*)
          from all_week_matches t
         where t.user_id = ranked_leaderboard.user_id
       ) as week_matches_played
  from ranked_leaderboard;
    '''

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        returned_result = cursor.fetchall()

    for entry in returned_result:
        d_tier = entry[3]
        if d_tier is None or d_tier == 0:
            d_tier = 'genesis'
        if entry[0] not in result:
            result[entry[0]] = {}
        user_data = {
            'division_tier': d_tier,
            'total_score': entry[1],
            'rank': entry[2],
            'week_average_rank': entry[5],
            'week_matches_played': entry[6],
        }
        result[entry[0]] = user_data

    return result

def get_division_ranges():
    divisions = Division.objects.all()

    relegation_ranges = {
        division.tier: (division.relegation_min_range, division.relegation_max_range)
        for division in divisions
    }

    promotion_ranges = {
        division.tier: (division.promotion_min_range, division.promotion_max_range)
        for division in divisions
    }

    return relegation_ranges, promotion_ranges

def distribute_players(week):
    leaderboards = get_global_leaderboards_without_divisions(week)  # {user_uuid: score_int}
    divisions = get_divisions()
    relegation_ranges, promotion_ranges = get_division_ranges()
    print(f"relegation_ranges: {relegation_ranges}, promotion_ranges: {promotion_ranges}")
    users_with_games = get_season_users(week)
    distribution_service = OrToolsDistributionStrategy(divisions, relegation_ranges, promotion_ranges, True)
    distribution_data = distribution_service.distribute(users_with_games, leaderboards,week)

    def division_cache():
        cache = {}
        divs = Division.objects.all()

        for division in divs:
            cache[division.tier] = division.id

        return cache

    def update_dict_of_users(data: Dict[uuid.UUID, Dict[str, Any]]):
        cache = division_cache()

        leaderboard = get_leaderboards_with_divisions(week)
        for user_id, user_info in data.items():
            data[user_id]['week_division_id'] = cache[user_info['week_division_tier']] if user_info[
                                                                                              'week_division_tier'] is not None else None
            data[user_id]['new_division_id'] = cache[user_info['new_division_tier']] if user_info[
                                                                                            'new_division_tier'] is not None else None
            data[user_id]['position'] = leaderboard[user_id]['rank']  # Update position from leaderboard
            data[user_id]['week_matches_played'] = leaderboard[user_id]['week_matches_played']
            data[user_id]['week_average_rank'] = leaderboard[user_id]['week_average_rank']
            print(
                f"user_id: {user_id}, old_division: {user_info['week_division_tier']}, new_division: {user_info['new_division_tier']}, points: {user_info['points']}, position: {user_info['position']}"
            )
        return data

    return update_dict_of_users(distribution_data)

def set_concluded_status(week):
    week.status = GameWeek.CLOSED
    week.scored_at = timezone.now()
    week.save(update_fields=['status', 'scored_at'])

def create_history_data(week, distributed_players):
    for user_id, user_data in distributed_players.items():
        UserGameWeekHistory.objects.create(
            user_id=user_id,
            game_week=week,
            week_division_id=user_data['week_division_id'],
            week_division_position=user_data['position'],
            week_division_tier=user_data['week_division_tier'],
            week_points=user_data['points'],
            week_coins=user_data['coins'],
            week_matches_played=user_data['week_matches_played'],
            week_average_rank=user_data['week_average_rank'],

            # store results of promoted/safe/relegated/ from finished week to new week
            new_division_id=user_data['new_division_id'],
            new_division_tier=user_data['new_division_tier'],
            status=user_data['division_status'],

        )

def create_new_week(week):
    start_at = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_at = start_at + timedelta(days=6, hours=23, minutes=59, seconds=59)

    season_start_at = week.season.start_at
    season_end_at = week.season.end_at

    # Check if the new week falls outside the season's start and end dates
    if season_start_at is None or season_end_at is None:
        # Handle cases where the season's start or end dates are not set
        return None

    if start_at < season_start_at or end_at > season_end_at:
        return None

    game_week = GameWeek.objects.create(
        name=f"Week of {start_at.strftime('%Y-%m-%d')} - {end_at.strftime('%Y-%m-%d')}",
        start_at=start_at,
        end_at=end_at,
        status=GameWeek.LIVE,
        season=week.season
    )
    return game_week

def assign_user_to_division(distribution_data, new_game_week_id):
    new_user_divisions = []

    for user_id, user_info in distribution_data.items():
        user_division = UserDivision(
            user_id=user_id,
            division_id=user_info['new_division_id'],
            game_week_id=new_game_week_id,

        )
        new_user_divisions.append(user_division)

    UserDivision.objects.bulk_create(new_user_divisions)

def calculate_rewards(division_rewards, players: Dict[uuid.UUID, Dict[str, Any]]):
    result = []

    def binary_search(ranges, target):
        left, right = 0, len(ranges) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if ranges[mid].min_position <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right  # return high index

    def find_rewards(position, division_id):
        division_rewards_list = [r for r in division_rewards if r.division_id == division_id]
        division_rewards_list.sort(key=lambda r: r.min_position)
        idx = binary_search(division_rewards_list, position)
        if idx >= 0:
            r = division_rewards_list[idx]
            if not r.max_position or position <= r.max_position:
                return {
                    'virtual': r.reward.credits,
                    'game': r.reward.game_token,
                    'lapt': r.reward.lapt_token,
                    'tickets': r.reward.event_tickets,
                    'balls': r.reward.ball,
                    'signed_balls': r.reward.signed_ball,
                    'shirts': r.reward.shirt,
                    'signed_shirts': r.reward.signed_shirt,
                    'kickoff_pack_1': r.reward.kickoff_pack_1,
                    'kickoff_pack_2': r.reward.kickoff_pack_2,
                    'kickoff_pack_3': r.reward.kickoff_pack_3,
                    'season_pack_1': r.reward.season_pack_1,
                    'season_pack_2': r.reward.season_pack_2,
                    'season_pack_3': r.reward.season_pack_3,
                }
        return {
            'virtual': 0,
            'game': 0,
            'lapt': 0,
            'tickets': 0,
            'balls': 0,
            'signed_balls': 0,
            'shirts': 0,
            'signed_shirts': 0,
            'kickoff_pack_1': 0,
            'kickoff_pack_2': 0,
            'kickoff_pack_3': 0,
            'season_pack_1': 0,
            'season_pack_2': 0,
            'season_pack_3': 0,
        }

    for player_id, player in players.items():
        rewards = find_rewards(player['position'], player['week_division_id'])
        player['coins'] = rewards['virtual']
        player['game'] = rewards['game']
        player['lapt'] = rewards['lapt']
        player['tickets'] = rewards['tickets']
        player['balls'] = rewards['balls']
        player['signed_balls'] = rewards['signed_balls']
        player['shirts'] = rewards['shirts']
        player['signed_shirts'] = rewards['signed_shirts']
        player['kickoff_pack_1'] = rewards['kickoff_pack_1']
        player['kickoff_pack_2'] = rewards['kickoff_pack_2']
        player['kickoff_pack_3'] = rewards['kickoff_pack_3']
        player['season_pack_1'] = rewards['season_pack_1']
        player['season_pack_2'] = rewards['season_pack_2']
        player['season_pack_3'] = rewards['season_pack_3']
        result.append(
            {
                'user_id': player_id,
                **rewards,
                'position': player['position'],
                'division_id': player['week_division_id']
            }
        )

    return result, players

def process_week_rewards(week, players: Dict[uuid.UUID, Dict[str, Any]]):
    if week.status == GameWeek.FINISHED:
        division_rewards = DivisionReward.objects.filter(week_id=week.id).select_related('reward')

        user_rewards, players = calculate_rewards(division_rewards, players)

        transactions = []
        reward_inboxes = []
        
        for r in user_rewards:
            user = CustomUser.objects.get(id=r['user_id'])
            # Check for virtual currency rewards (credits)
            if r['virtual'] > 0:
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    amount=r['virtual'],
                    text=f"Virtual reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.VIRTUAL,
                    delivered=True
                ))
            # Check for game token rewards
            if r['game'] > 0:
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    amount=r['game'],
                    text=f"GAME reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.GAME,
                    delivered=False
                ))
            # Check for LAPT token rewards
            if r['lapt'] > 0:
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    amount=r['lapt'],
                    text=f"LAPT reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.LAPT,
                    delivered=False
                ))
            # Check for event tickets rewards
            if r['tickets'] > 0:
                reward = Rewards(event_tickets=r['tickets'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['tickets'],
                    text=f"Event tickets reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.EVENT_TICKET,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['tickets']} Event Tickets",
                    description=f"Congratulations! You have received {r['tickets']} Event Tickets for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Tickets.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['tickets']} Event Tickets for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )

                # Send the Slack alert
                send_slack_alert(slack_message)            # Check for ball rewards
            if r['balls'] > 0:
                reward = Rewards(balls=r['balls'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['balls'],
                    text=f"Ball reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.BALL,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['balls']} Balls",
                    description=f"Congratulations! You have received {r['balls']} Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Frame.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['balls']} Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message) 
            # Check for signed ball rewards
            if r['signed_balls'] > 0:
                reward = Rewards(signed_balls=r['signed_balls'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['signed_balls'],
                    text=f"Signed Ball reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.SIGNED_BALL,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['signed_balls']} Signed Balls",
                    description=f"Congratulations! You have received {r['signed_balls']} Signed Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Frame.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['signed_balls']} Signed Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message) 
            # Check for shirt rewards
            if r['shirts'] > 0:
                reward = Rewards(shirts=r['shirts'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['shirts'],
                    text=f"Shirt reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.SHIRT,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['shirts']} Shirts",
                    description=f"Congratulations! You have received {r['shirts']} Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Shirt.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['shirts']} Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message)
            # Check for signed shirt rewards
            if r['signed_shirts'] > 0:
                reward = Rewards(signed_shirts=r['signed_shirts'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['signed_shirts'],
                    text=f"Signed Shirt reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.SIGNED_SHIRT,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['signed_shirts']} Signed Shirts",
                    description=f"Congratulations! You have received {r['signed_shirts']} Signed Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Shirt.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['signed_shirts']} Signed Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message)
            # Check for kickoff pack rewards
            if r['season_pack_1'] > 0:
                reward = Rewards(season_pack_1=r['season_pack_1'])
                reward.save()  # Save individual reward
                for i in range(r['season_pack_1']):
                    transactions.append(Transactions(
                        user_id=r['user_id'],
                        quantity=1,
                        text=f"Card pack reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                        week_id=week.id,
                        object_type=Transactions.SEASON_PACK_1,
                        delivered=False
                    ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['season_pack_1']} Card Packs",
                    description=f"Congratulations! You have received {r['season_pack_1']} Card Packs for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.cdn.digitaloceanspaces.com/notification-icons/Packs.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))

            if r['season_pack_2'] > 0:
                reward = Rewards(season_pack_2=r['season_pack_2'])
                reward.save()  # Save individual reward
                for i in range(r['season_pack_2']):
                    transactions.append(Transactions(
                        user_id=r['user_id'],
                        quantity=1,
                        text=f"Card pack reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                        week_id=week.id,
                        object_type=Transactions.SEASON_PACK_2,
                        delivered=False
                    ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['season_pack_2']} Card Packs",
                    description=f"Congratulations! You have received {r['season_pack_2']} Card Packs for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.cdn.digitaloceanspaces.com/notification-icons/Packs.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                
            if r['season_pack_3'] > 0:
                reward = Rewards(season_pack_3=r['season_pack_3'])
                reward.save()  # Save individual reward
                for i in range(r['season_pack_3']):
                    transactions.append(Transactions(
                        user_id=r['user_id'],
                        quantity=1,
                        text=f"Card pack reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                        week_id=week.id,
                        object_type=Transactions.SEASON_PACK_3,
                        delivered=False
                    ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['season_pack_3']} Card Packs",
                    description=f"Congratulations! You have received {r['season_pack_3']} Card Packs for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.cdn.digitaloceanspaces.com/notification-icons/Packs.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))

        # After processing, bulk create the transactions and inbox entries
        Transactions.objects.bulk_create(transactions)
        AppInbox.objects.bulk_create(reward_inboxes)

        return players

@shared_task
def conclude_game_week(week):
    if week.season:
        with transaction.atomic():
            # Step 1: Check and finish the current game week
            check_and_finish_week(week)
            # Step 2: Distribute players based on their performance
            distributed_players = distribute_players(week)
            if distributed_players:
                # Step 3: Process rewards for the distributed players
                modified_distributed_players = process_week_rewards(week, distributed_players)
            else:
                modified_distributed_players = None
            # Step 4: Set the current game week's status to 'concluded'
            set_concluded_status(week)
            # Step 5: Create a new game week
            new_week = create_new_week(week)
            if modified_distributed_players:
                # Step 6: Assign users to their new divisions for the new week
                assign_user_to_division(modified_distributed_players, new_week.id)
                # Step 7: Create history data for the concluded game week
                create_history_data(week, modified_distributed_players)
            # Step 8: Recalculate new week
            calculate_promotion_and_relegation(new_week)

    # Notify players that the week has been concluded
    if modified_distributed_players:
        send_push_to_users.delay(list(modified_distributed_players.keys()), week.id)
    return modified_distributed_players

@shared_task
def calculate_promotion_and_relegation(week):
    divisions = get_divisions()
    relegation_ranges, promotion_ranges = get_division_ranges()
    users_with_games = get_season_users(week)
    division_population = {}
    for user in users_with_games:
        if user.division_id is None:
            continue
        if user.division_id not in division_population:
            division_population[user.division_id] = 0
        division_population[user.division_id] += 1

    distribution_service = OrToolsDistributionStrategy(divisions, relegation_ranges, promotion_ranges, True)
    distribution_data = distribution_service.calculate_capacity(division_population)

    for div_id, data in distribution_data.items():
        GameWeekDivision.objects.get_or_create(week=week, division_id=div_id, defaults={
            'capacity': data.capacity,
            'promotion_count': data.promotion_count,
            'relegation_count': data.relegation_count,
        })

# Slack webhook URL
slack_webhook_url = 'https://hooks.slack.com/services/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'

def send_slack_alert(message):
    payload = {
        "text": message  # Message that will be sent to the Slack channel
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = request.post(slack_webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request to Slack returned error {response.status_code}, the response is:\n{response.text}")

```

## File: `divisions/tests.py`
- **File Size:** 16679 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** calculate division capacity

```
import uuid
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from core.models import (
    GameWeek, DivisionReward, CustomUser,
    Transactions, Division,Match, Game,
    MatchLeaderboard, UserGameWeekHistory,
    Team, Season, Competition, UserDivision, GameSeason)

from .sync import (
    check_and_finish_week, get_season_users,
    get_global_leaderboards_without_divisions,
    create_history_data, create_new_week,
    assign_user_to_division, calculate_rewards,
    process_week_rewards, conclude_game_week, get_leaderboards_with_divisions
)
from .simulation import OrToolsDistributionStrategy, User, Division as SDivision

class BaseClassTest(TestCase):
    def setUp(self):
        DivisionReward.objects.all().delete()
        MatchLeaderboard.objects.all().delete()
        Game.objects.all().delete()
        Match.objects.all().delete()
        CustomUser.objects.all().delete()
        Division.objects.all().delete()
        GameWeek.objects.all().delete()
        Team.objects.all().delete()
        Season.objects.all().delete()
        Competition.objects.all().delete()

        divisions = [
            {'name': "Division 10", 'tier': 10, 'percentage': 0.08},
            {'name': "Division 9", 'tier': 9, 'percentage': 0.10},
            {'name': "Division 8", 'tier': 8, 'percentage': 0.15},
            {'name': "Division 7", 'tier': 7, 'percentage': 0.19},
            {'name': "Division 6", 'tier': 6, 'percentage': 0.15},
            {'name': "Division 5", 'tier': 5, 'percentage': 0.12},
            {'name': "Division 4", 'tier': 4, 'percentage': 0.09},
            {'name': "Division 3", 'tier': 3, 'percentage': 0.07},
            {'name': "Division 2", 'tier': 2, 'percentage': 0.04},
            {'name': "Division 1", 'tier': 1, 'percentage': 0.01},
        ]

        for division in divisions:
            Division.objects.create(name=division['name'], tier=division['tier'], percentage=division['percentage'])

        self.division = Division.objects.order_by('-tier').first()
        self.division2 = Division.objects.filter(tier=(self.division.tier - 1)).first()
        self.season = Season.objects.create(name="Test Season")
        self.game_season = GameSeason.objects.create(name="Test Game Season", start_at=(timezone.now() - timedelta(days=20)), end_at=(timezone.now() + timedelta(days=10)))

        self.game_week = GameWeek.objects.create(
            name="Week 1",
            start_at=timezone.now() - timedelta(days=7),
            end_at=timezone.now(),
            status=GameWeek.LIVE,
            season=self.game_season,
        )
        self.user1 = CustomUser.objects.create(name="user1")
        self.user2 = CustomUser.objects.create(name="user2", email='example@email.com')
        self.user3 = CustomUser.objects.create(name="user3", email='example2@email.com')

        self.team1 = Team.objects.create()
        self.team2 = Team.objects.create()
        self.competition = Competition.objects.create(name='Test Competition')

        self.match = Match.objects.create(
            match_time=timezone.now() - timedelta(days=1),
            match_end=timezone.now() - timedelta(minutes=1),
            competition=self.competition,
            season=self.season,
            home_team=self.team1,
            away_team=self.team2,
            match_type=Match.MATCH_TYPE_FREE,
            import_id='test-' + str(uuid.uuid4()),
        )

        self.game_user1 = Game.objects.create(
            user=self.user1,
            match=self.match,
            score=100

        )
        self.game_user2 = Game.objects.create(
            user=self.user2,
            match=self.match,
            score=80
        )

        self.old_match = Match.objects.create(
            season=self.season,
            match_time=timezone.now() - timezone.timedelta(days=19),
            match_end=timezone.now() - timezone.timedelta(days=18),
            competition=self.competition,
            home_team=self.team1,
            away_team=self.team2,
            match_type=Match.MATCH_TYPE_FREE,
            import_id='test-' + str(uuid.uuid4()),
        )

        # Create games for user3 outside the current game week
        self.old_game = Game.objects.create(
            user=self.user3,
            match=self.old_match,
            score=150
        )

        self.leaderboard1, created = MatchLeaderboard.objects.update_or_create(
            match=self.match,
            user=self.user1,
            defaults={
                'position': 1,
                'score': 100,
                'division': self.division
            }
        )

        self.leaderboard2, created = MatchLeaderboard.objects.update_or_create(
            match=self.match,
            user=self.user2,
            defaults={
                'position': 2,
                'score': 80,
                'division': self.division
            }
        )

        self.leaderboard3, created = MatchLeaderboard.objects.update_or_create(
            match=self.old_match,
            user=self.user3,
            defaults={
                'position': 1,
                'score': 150,
                'division': self.division2
            }
        )

        self.old_game_week = GameWeek.objects.create(
            name="Old Week",
            start_at=timezone.now() - timedelta(days=10),
            end_at=timezone.now() - timedelta(days=7),
            status=GameWeek.CLOSED,
            season=self.game_season,
        )
        self.user_division = UserDivision.objects.create(
            user=self.user3,
            division=self.division2,
            game_week=self.old_game_week
        )

        self.distributed_players = {
            self.user1.id: {
                'position': 1,
                'week_division_tier': None,
                'week_division_id': None,
                'points': self.leaderboard1.score,
                'coins': 0,
                'new_division_tier': self.division.tier,
                'new_division_id': self.division.id,
                'division_status': UserGameWeekHistory.PROMOTED,
            }, self.user2.id: {
                'position': 2,
                'week_division_tier': None,
                'week_division_id': None,
                'points': self.leaderboard2.score,
                'coins': 0,
                'new_division_tier': self.division.tier,
                'new_division_id': self.division.id,
                'division_status': UserGameWeekHistory.PROMOTED,
            }, self.user3.id: {
                'position': 1,
                'week_division_tier': self.division2.tier,
                'week_division_id': self.division2.id,
                'points': 0,
                'coins': 0,
                'new_division_tier': self.division2.tier,
                'new_division_id': self.division2.id,
                'division_status': UserGameWeekHistory.SAFE,

            }
        }

class RewardCalculationTest(BaseClassTest):
    def test_check_and_finish_week(self):
        result = check_and_finish_week(self.game_week)

        self.assertIsNone(result)
        self.assertEqual(self.game_week.status, GameWeek.FINISHED)

    def get_season_users(self):
        users = get_season_users(self.game_week)

        self.assertIn(User(id=self.user1.id, division_id=None, division_tier=None, verified=False), users)
        self.assertIn(User(id=self.user2.id, division_id=None, division_tier=None, verified=True), users)
        self.assertIn(User(id=self.user3.id, division_id=None, division_tier=None, verified=True), users)

    def test_get_global_leaderboards_without_divisions(self):
        leaderboard = get_global_leaderboards_without_divisions(self.game_week)

        self.assertEqual(leaderboard[self.user1.id], 100)
        self.assertEqual(leaderboard[self.user2.id], 80)
        self.assertEqual(leaderboard[self.user3.id], 0)

    def test_get_leaderboards_with_divisions(self):
        leaderboard = get_leaderboards_with_divisions(self.game_week)
        expected_result = {
            self.user1.id: {'division_tier': self.division.tier, 'total_score': 100.0, 'rank': 1},
            self.user2.id: {'division_tier': self.division.tier, 'total_score': 80.0, 'rank': 2},
            self.user3.id: {'division_tier': self.division2.tier, 'total_score': 0.0, 'rank': 1},
        }

        self.assertEqual(set(leaderboard.keys()), set(expected_result.keys()),
                         "The keys of the actual result do not match the expected keys.")

        for user_id, expected_data in expected_result.items():
            self.assertIn(user_id, leaderboard, f"User ID {user_id} not found in the actual result.")
            actual_data = leaderboard[user_id]

            self.assertEqual(actual_data['division_tier'], expected_data['division_tier'],
                             f"Division tier for user {user_id} does not match.")
            self.assertEqual(actual_data['total_score'], expected_data['total_score'],
                             f"Total score for user {user_id} does not match.")
            self.assertEqual(actual_data['rank'], expected_data['rank'], f"Rank for user {user_id} does not match.")

    def test_distribute_players(self):
        leaderboards = get_global_leaderboards_without_divisions(self.game_week)
        divisions = Division.objects.all()
        users = get_season_users(self.game_week)
        relegation_ranges = {i.tier: (0.2, 0.5) for i in divisions}
        promotion_ranges = {i.tier: (0.2, 0.5) for i in divisions}
        distribution_service = OrToolsDistributionStrategy(divisions, relegation_ranges, promotion_ranges, True)
        distribution_data = distribution_service.distribute(users, leaderboards)

        self.assertIsNotNone(distribution_data)

    def test_create_history_data(self):
        create_history_data(self.game_week, self.distributed_players)

        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user1, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user2, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user3, game_week=self.game_week).exists())

    def test_create_new_week(self):
        new_week = create_new_week(self.game_week)

        self.assertEqual(new_week.status, GameWeek.LIVE)
        self.assertEqual(new_week.season, self.game_season)

    def test_assign_user_to_division(self):
        new_week = create_new_week(self.game_week)
        assign_user_to_division(self.distributed_players, new_week.id)

        self.assertTrue(UserDivision.objects.filter(user=self.user1, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user2, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user3, game_week=new_week).exists())

    def test_calculate_rewards(self):
        rewards = DivisionReward.objects.filter(week=self.game_week)
        user_rewards, _players = calculate_rewards(rewards, self.distributed_players)

        self.assertEqual(user_rewards[0]['reward'], 600)
        self.assertEqual(user_rewards[1]['reward'], 300)
        self.assertEqual(user_rewards[2]['reward'], 666.6666666666667)

    def test_process_week_rewards(self):
        players = self.distributed_players
        self.game_week.status = GameWeek.FINISHED
        process_week_rewards(self.game_week, players)
        transactions = Transactions.objects.filter(week=self.game_week)

        self.assertEqual(len(list(transactions)), 3)
        self.assertEqual(transactions[0].user_id, self.user1.id)
        self.assertEqual(transactions[1].user_id, self.user2.id)
        self.assertEqual(transactions[2].user_id, self.user3.id)

class ConcludeGameWeekTest(BaseClassTest):
    def test_conclude_game_week(self):
        distribution_data = conclude_game_week(self.game_week)
        self.distributed_players[self.user1.id]['coins'] = 600
        self.distributed_players[self.user2.id]['coins'] = 300
        self.distributed_players[self.user3.id]['coins'] = 666.6666666666667
        self.distributed_players[self.user1.id]['new_division_id'] = self.division.id
        self.distributed_players[self.user2.id]['new_division_id'] = self.division.id
        self.distributed_players[self.user3.id]['new_division_id'] = self.division2.id
        self.distributed_players[self.user1.id]['new_division_tier'] = self.division.tier
        self.distributed_players[self.user2.id]['new_division_tier'] = self.division.tier
        self.distributed_players[self.user3.id]['new_division_tier'] = self.division2.tier

        self.assertEqual(set(distribution_data.keys()), set(self.distributed_players.keys()),
                         "The keys of the actual result do not match the expected keys.")

        for user_id, expected_data in self.distributed_players.items():
            self.assertIn(user_id, distribution_data, f"User ID {user_id} not found in the actual result.")
            actual_data = distribution_data[user_id]

            self.assertEqual(actual_data['new_division_id'], expected_data['new_division_id'],
                             f"new_division_id tier for user {user_id} does not match.")
            self.assertEqual(actual_data['week_division_id'], expected_data['week_division_id'],
                             f"week_division_id tier for user {user_id} does not match.")
            self.assertEqual(actual_data['division_status'], expected_data['division_status'],
                             f"division_status tier for user {user_id} does not match.")
            self.assertEqual(actual_data['new_division_tier'], expected_data['new_division_tier'],
                             f"Division tier for user {user_id} does not match.")
            self.assertEqual(actual_data['coins'], expected_data['coins'],
                             f"Coins for user {user_id} does not match.")
            self.assertEqual(actual_data['points'], expected_data['points'],
                             f"Total points for user {user_id} does not match.")
            self.assertEqual(actual_data['week_division_tier'], expected_data['week_division_tier'],
                             f"Week_division_tier for user {user_id} does not match.")
            self.assertEqual(actual_data['position'], expected_data['position'], f"Rank for user {user_id} does not match.")

        self.game_week.refresh_from_db()
        self.assertEqual(self.game_week.status, GameWeek.CLOSED)

        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user1, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user2, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user3, game_week=self.game_week).exists())

        transactions = list(Transactions.objects.filter(week=self.game_week).order_by('user_id'))
        self.assertEqual(len(transactions), 3)
        user_ids = sorted([self.user1.id, self.user2.id, self.user3.id])
        transaction_user_ids = [transaction.user_id for transaction in transactions]

        self.assertEqual(transaction_user_ids, user_ids)

        new_week = GameWeek.objects.get(status=GameWeek.LIVE)
        start_at = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_at = start_at + timedelta(days=6, hours=23, minutes=59, seconds=59)

        self.assertEqual(new_week.status, GameWeek.LIVE)
        self.assertEqual(new_week.start_at, start_at)
        self.assertEqual(new_week.end_at, end_at)
        self.assertEqual(new_week.season, self.game_season)

        self.assertTrue(UserDivision.objects.filter(user=self.user1, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user2, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user3, game_week=new_week).exists())

class TestDistribution(BaseClassTest):
    def test_ortools_distributor(self):
        divisions = Division.objects.all()
        s = OrToolsDistributionStrategy(
            [SDivision(div.id, div.tier, div.percentage) for div in divisions],
            {div.tier: (div.relegation_min_range, div.relegation_max_range) for div in divisions},
            {div.tier: (div.promotion_min_range, div.promotion_max_range) for div in divisions},
            True,
        )
        population = {}
        for division in divisions:
            population[division.id] = division.tier * 100
        print(s.calculate_capacity(population))
```

## File: `images/laliga-matchfantasy-admin/deployment_dev.yaml`
- **File Size:** 3651 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Revert "added celery-flower as celery monitoring tool"

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mobile-api
  namespace: "fanclash-dev"
  labels:
    app: mobile-api
    purpose: api
    tags.datadoghq.com/env: "dev"
    tags.datadoghq.com/service: "laliga-matchfantasy-admin-mobile"
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mobile-api
  template:
    metadata:
      labels:
        app: mobile-api
        purpose: api
        tags.datadoghq.com/env: "dev"
        tags.datadoghq.com/service: "laliga-matchfantasy-admin-mobile"
    spec:
      containers:
        - image: registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:TAG_PLACEHOLDER
          imagePullPolicy: IfNotPresent
          name: mobile-api
          args: ["server"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - configMapRef:
                name: redis-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: rmq-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: DD_SERVICE_NAME
              value: "mobile-api"
          ports:
            - containerPort: 8000
          readinessProbe:
            httpGet:
              path: /readiness
              port: 8000
            initialDelaySeconds: 20
            timeoutSeconds: 5
          resources:
            requests:
              cpu: 30m

        - image: registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:TAG_PLACEHOLDER
          imagePullPolicy: IfNotPresent
          name: celery-worker
          args: ["celery-worker"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - configMapRef:
                name: redis-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: rmq-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: DD_SERVICE_NAME
              value: "celery-worker"

        - image: registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:TAG_PLACEHOLDER
          imagePullPolicy: IfNotPresent
          name: celery-beat
          args: ["celery-beat"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - configMapRef:
                name: redis-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: rmq-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: DD_SERVICE_NAME
              value: "celery-beat"
      volumes:
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
```

## File: `images/laliga-matchfantasy-admin/deployment_prd.yaml`
- **File Size:** 3495 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** update deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mobile-api
  namespace: "prd-fanclash"
  labels:
    app: mobile-api
    purpose: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mobile-api
  template:
    metadata:
      labels:
        app: mobile-api
        purpose: api
    spec:
      # imagePullSecrets:
      # - name: gameon-ams3
      containers:
        - image: registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:TAG_PLACEHOLDER
          imagePullPolicy: IfNotPresent
          name: mobile-api
          args: ["server"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - configMapRef:
                name: redis-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: rmq-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: DD_SERVICE_NAME
              value: "mobile-api"
          ports:
            - containerPort: 8000
          readinessProbe:
            httpGet:
              path: /readiness
              port: 8000
            initialDelaySeconds: 20
            timeoutSeconds: 5
          resources:
            requests:
              cpu: 30m

        - image: registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:TAG_PLACEHOLDER
          imagePullPolicy: IfNotPresent
          name: celery-worker
          args: ["celery-worker"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - configMapRef:
                name: redis-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: rmq-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: DD_SERVICE_NAME
              value: "celery-worker"

        - image: registry.digitalocean.com/gameon-ams3/laliga-matchfantasy-admin:TAG_PLACEHOLDER
          imagePullPolicy: IfNotPresent
          name: celery-beat
          args: ["celery-beat"]
          envFrom:
            - configMapRef:
                name: fanclash-config
            - configMapRef:
                name: mobile-api-config
            - configMapRef:
                name: rmq-config
            - configMapRef:
                name: redis-config
            - secretRef:
                name: fcm-creds
            - secretRef:
                name: opta-feed-creds
            - secretRef:
                name: ortec-creds
            - secretRef:
                name: db-creds
            - secretRef:
                name: rmq-creds
            - secretRef:
                name: do-api-creds
          env:
            - name: DD_SERVICE_NAME
              value: "celery-beat"
      volumes:
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
```

## File: `images/laliga-matchfantasy-admin/service_prd.yaml`
- **File Size:** 200 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add prd deployment files

```
apiVersion: v1
kind: Service
metadata:
  name: mobile-api
  namespace: "prd-fanclash"
  labels:
    app: mobile-api
spec:
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: mobile-api
```

## File: `manage.py`
- **File Size:** 542 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobile_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

```

## File: `mobile_api/__init__.py`
- **File Size:** 65 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from .celery import app as celery_app

__all__ = ('celery_app',)

```

## File: `mobile_api/celery.py`
- **File Size:** 4281 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** redeploy

```
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

broker_url = 'amqp://{}:{}@{}:{}/{}'.format(
    os.getenv("RMQ_USER"),
    os.getenv("RMQ_PASSWORD"),
    os.getenv("RMQ_HOST"),
    os.getenv("RMQ_PORT"),
    os.getenv("RMQ_VHOST"),
)

WSocketEnabled =  os.getenv('WSOCKET_ENABLED').lower() == "true" if os.getenv('WSOCKET_ENABLED') is not None else False

app = Celery('mobile_api', broker=broker_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sync_competitions': {
        'task': 'core.tasks.task_sync_competitions',
        'schedule': crontab(hour=4, minute=30),  # every day at 04:30
    },
    'task_sync_teams': {
        'task': 'core.tasks.task_sync_teams',
        'schedule': crontab(hour=3, minute=30),  # every day at 03:30
    },
    'task_sync_matches': {
        'task': 'core.tasks.task_sync_matches',
        'schedule': 60 if WSocketEnabled else 5,  # every 5 sec or 60 sec
    },
    'task_sync_match_players': {
        'task': 'core.tasks.task_sync_match_players',
        'schedule': 60 * 60,  # every 1 hour
    },
    'task_process_simulations': {
        'task': 'core.tasks.task_process_simulations',
        'schedule': 30,  # every 30 sec
    },
    'task_sync_soccer_wiki': {
        'task': 'core.tasks.task_sync_soccer_wiki',
        'schedule': 30 * 60,  # every 30 min
    },
    'task_download_soccer_wiki': {
        'task': 'core.tasks.task_download_soccer_wiki',
        'schedule': crontab(hour=4, minute=30),  # every day at 04:30
    },
    'task_update_user_stats': {
        'task': 'core.tasks.task_update_user_stats',
        'schedule': crontab(hour=2, minute=30),  # every day at 02:30
    },
    'task_process_subscription_requests': {
        'task': 'core.tasks.task_process_subscription_requests',
        'schedule': 30,  # every 30 sec
    },
    'task_expire_subscriptions': {
        'task': 'core.tasks.task_expire_subscriptions',
        'schedule': crontab(hour=2, minute=50),  # every day at 02:50
    },
    'task_run_event_throttling': {
        'task': 'core.tasks.task_run_event_throttling',
        'schedule': settings.AMQP_THROTTLING_SCHEDULE_INTERVAL,
    },
    'task_normalize_and_check_all_names': {
        'task': 'core.tasks.task_normalize_and_check_all_names',
        'schedule': crontab(hour=0, minute=0),  # Runs daily at midnight
    },
    'task_conclude_game_week':{
        'task': 'core.tasks.task_conclude_game_week',
        'schedule': 60 * 10,
        # 'schedule': crontab(hour=0, minute=1),  # Runs daily at 00:01
    },
    'task_calculate_promotion_and_relegation':{
        'task': 'core.tasks.task_calculate_promotion_and_relegation',
        # 'schedule': 60 * 6,
        'schedule': 30 * 60,  # every 30 min
    },
    'task_sync_matches_via_sdapi': {
        'task': 'core.tasks.task_sync_matches_via_sdapi',
        'schedule': 60 * 2,  # every 2 minutes (lowest avg SDAPI update)
    },
    # 'task_update_order_statuses': {
    #     'task': 'core.tasks.task_update_order_statuses',
    #     'schedule': 30,  # every 30 sec
    # },
    'task_mint_nfts_for_expired_cardpacks': {
        'task': 'core.tasks.mint_nfts_for_expired_cardpacks',
        'schedule': crontab(minute='*/45'),  # Runs every 45 minutes
    },
    'task_process_pending_crypto_transactions': {
        'task': 'core.tasks.mint_process_pending_crypto_transactions',
        'schedule': crontab(minute='*/15'),  # Runs every 15 minutes
    },
    'task_process_pending_cardpack_transactions': {
        'task': 'core.tasks.mint_process_pending_cardpack_transactions',
        'schedule': crontab(minute='*/15'),  # Runs every 15 minutes
    },
    'assign-default-items-every-10-minutes': {
        'task': 'core.tasks.assign_default_items_to_users_task',
        'schedule': crontab(minute='*/10'),  # Runs every 10 minutes
    }
}

```

## File: `mobile_api/settings/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `mobile_api/settings/base.py`
- **File Size:** 6409 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** added opta proxy

```
"""
Django settings for mobile_api project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import datetime
import json
import os

from opta.websocket import OptaWebSocketClient
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from ortec.api import OrtecAPI
from opta.api import OptaAPI

from revenue_cat.api import RevenueCatAPI

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "65r&%#$ocukd68u^&v+g=u%q%)u5v4#sp70ac-wz@9nnrl$wbz"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
    'rabbit',
    'soccer_wiki',
    'django_celery_beat',
    'blockchain_web3',
    'csvexport',
    'divisions'
]

MIDDLEWARE = [
    # 'util.middlewares.MetricMiddleware',
    "util.middlewares.HealthCheckMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mobile_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mobile_api.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
        # 'ENGINE': 'django.db.backends.mysql' instead of the following.
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT", "5432"),
        "OPTIONS": {"sslmode": os.getenv("DATABASE_SSLMODE", "disabled")},
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "core.exceptions.custom_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": ("core.authentication.JWTAuthentication",),
    "DEFAULT_RENDERER_CLASSES": (
        "core.renderers.CustomJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
}

GCE_PROJECT_ID = os.getenv("GCE_PROJECT_ID")
GCE_OPTA_FEED_BUCKET = os.getenv("GCE_OPTA_FEED_BUCKET")
GCE_OPTA_FEED_CREDENTIALS = os.getenv("GCE_OPTA_FEED_CREDENTIALS")
GCE_PLAYER_IMAGES_BUCKET = os.getenv("GCE_PLAYER_IMAGES_BUCKET")
GCE_TEAM_CRESTS_BUCKET = os.getenv("GCE_TEAM_CRESTS_BUCKET")
GCE_USER_AVATAR_BUCKET = os.getenv("GCE_USER_AVATAR_BUCKET")

# 20 mb
DATA_UPLOAD_MAX_MEMORY_SIZE = 20971520
AMQP_MATCH_EVENTS_EXCHANGE = os.getenv("AMQP_MATCH_EVENTS_EXCHANGE")
AMQP_GAMES_EXCHANGE = os.getenv("AMQP_GAMES_EXCHANGE")
AMQP_SYSTEM_EXCHANGE = os.getenv("AMQP_SYSTEM_EXCHANGE")
AMPQ_NOTIFICATIONS_EXCHANGE = os.getenv("AMQP_NOTIFICATIONS_EXCHANGE")
RMQ_FCM_EXCHANGE= os.getenv("RMQ_FCM_EXCHANGE")

FCM_CREDENTIALS = os.getenv("FCM_CREDENTIALS")

# gameplay settings
GAME_DISPLAY_LOW_DELTA = datetime.timedelta(hours=12)
MATCH_DISPLAY_LOW_DELTA = datetime.timedelta(hours=12)
MATCH_DISPLAY_HIGH_DELTA = datetime.timedelta(days=3)
MAX_PICKS = 4
STAR_PLAYERS_TOP = 8
MIN_CASHOUT_AMOUNT = 15
AVG_STAT_GAME_COUNT = 50

# init fcm
# firebase_admin.initialize_app(credentials.Certificate(json.loads(FCM_CREDENTIALS)))

# STATSD_HOST = os.getenv('STATSD_HOST')
# STATSD_PORT = int(os.getenv('STATSD_PORT', 8125))
# STATSD_CLIENT = 'django_statsd.clients.normal'

ORTEC_CLIENT = OrtecAPI(os.getenv("ORTEC_USERNAME"), os.getenv("ORTEC_PASSWORD"))

OPTA_CLIENT = OptaAPI(
    os.getenv("OPTA_OUTLET_AUTH_KEY"),
    os.getenv("OPTA_RT_MODE"),
    os.getenv("OPTA_DATA_FORMAT"),
)
OPTA_WS_CLIENT = OptaWebSocketClient(os.getenv("OPTA_OUTLET_AUTH_KEY"))

REVENUE_CAT_CLIENT = RevenueCatAPI(os.getenv("REVENUE_CAT_API_KEY"))

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "fanclash_cache",
    }
}

PREMIUM_SUBSCRIPTION_PRICE = 10.00

DO_SPACE_API_KEY = os.getenv("DO_SPACE_API_KEY")
DO_SPACE_API_SECRET = os.getenv("DO_SPACE_API_SECRET")

AMQP_THROTTLING_ENABLED = os.getenv("AMQP_THROTTLING_ENABLED", True)
AMQP_THROTTLING_THRESHOLD = os.getenv("AMQP_THROTTLING_THRESHOLD", 55)
AMQP_THROTTLING_SCHEDULE_INTERVAL = os.getenv("AMQP_THROTTLING_SCHEDULE_INTERVAL", 60)

OPTA_PROXY = os.getenv("OPTA_PROXY")
```

## File: `mobile_api/settings/development.py`
- **File Size:** 114 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** wip

```
from .base import *

DEBUG=True
ENV_NAME = 'development'
SYNC_DELAY_BEFORE_MATCH = 60
SYNC_DELAY_DURING_MATCH = 5

```

## File: `mobile_api/settings/production.py`
- **File Size:** 115 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** use env var

```
from .base import *

DEBUG = True
ENV_NAME = 'production'
SYNC_DELAY_BEFORE_MATCH = 60
SYNC_DELAY_DURING_MATCH = 2

```

## File: `mobile_api/settings/staging.py`
- **File Size:** 240 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** use env var

```
from .base import *

ENV_NAME = 'staging'
# Sync matches rarely on staging since
# both prod and staging are running in the same cluster and compete for resources
SYNC_DELAY_BEFORE_MATCH = 60 * 10
SYNC_DELAY_DURING_MATCH = 5
USE_TZ = False

```

## File: `mobile_api/urls.py`
- **File Size:** 952 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
"""mobile_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```

## File: `mobile_api/wsgi.py`
- **File Size:** 397 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
"""
WSGI config for mobile_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobile_api.settings')

application = get_wsgi_application()

```

## File: `opta/__init__.py`
- **File Size:** 166 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add comprehensive logging level and format for our service

```
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S", format="[%(asctime)s] [%(levelname)s] %(message)s")
```

## File: `opta/api.py`
- **File Size:** 2705 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fixed proxy for requests

```
import logging
import requests
from django.conf import settings

logger = logging.getLogger()

class OptaAPI:
    def __init__(self, outletAuthKey, mode, dataformat):
        self.outletAuthKey = outletAuthKey
        self.mode = mode
        self.dataformat = dataformat

    def get_proxies(self):
        proxy_url = settings.OPTA_PROXY
        if proxy_url is None or proxy_url == "":
            return None
        return {
            'http': proxy_url,
            'https': proxy_url,
        }

    def get_competitions(self):
        return self._process_request("/tournamentcalendar", "/active/authorized")

    def get_competition_phases(self, tournamentCalendarUuid):
        return self._process_request(f"/standings", "", f"tmcl={tournamentCalendarUuid}")

    def get_schedule(self, tournamentCalendarUuid):
        return self._process_request(f"/tournamentschedule", f"/{tournamentCalendarUuid}")

    def get_selection_persons(self, tournamentCalendarUuid, contestantUUID):
        # with stats info for the players, currently not needed
        # return self._process_request(f"/squads", "", f"tmcl={tournamentCalendarUuid}&ctst={contestantUUID}&detailed=yes")
        return self._process_request(f"/squads", "", f"tmcl={tournamentCalendarUuid}&ctst={contestantUUID}&detailed=no")

    def get_match_events(self, match_id):
        return self._process_request(f"/matchevent", f"", f"fx={match_id}")

    def get_match_stats(self, match_id, detailed="yes"):
        return self._process_request(f"/matchstats", f"/{match_id}", f"detailed={detailed}")

    @staticmethod
    def _build_url(self, path, extraPath="", extraQuery=""):
        if extraQuery and extraQuery != "" and extraQuery != None:
            extraQuery = "&" + extraQuery
        q = f"?_rt={self.mode}&_fmt={self.dataformat}" + extraQuery
        url = f"https://api.performfeeds.com/soccerdata{path}/{self.outletAuthKey}{extraPath}" + q
        # print(url)
        return url

    def _process_request(self, path, extraPath="", extraQueryString="", data=None):
        final_url = self._build_url(self, path, extraPath, extraQueryString)
        # logger.info("Making request to {}".format(final_url))
        # print("Making request to {}".format(final_url))

        res = requests.get(
            final_url,
            data,
            proxies=self.get_proxies(),
            # headers={"Authorization": "Session {}".format(self.get_token())},
        )

        if res.status_code != 200:
            raise Exception(
                "Received invalid status code {} for {}: {}".format(
                    res.status_code, final_url, res.content
                )
            )
        return res.json()

```

## File: `opta/conv.py`
- **File Size:** 567 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Fix for attackers

```
from core import const

# Goalkeeper | Wing Back | Defender | Defensive Midfielder | Attacking Midfielder | Midfielder | Striker | Substitute
POSITION_MAP = {
    "Goalkeeper": const.POSITION_GOALKEEPER,
    "Wing Back": const.POSITION_DEFENDER,
    "Defender": const.POSITION_DEFENDER,
    "Defensive Midfielder": const.POSITION_MIDFIELDER,
    "Attacking Midfielder": const.POSITION_MIDFIELDER,
    "Midfielder": const.POSITION_MIDFIELDER,
    "Striker": const.POSITION_FORWARD,
    "Attacker": const.POSITION_FORWARD,
    "Substitute": const.POSITION_SUBSTITUTE,
}
```

## File: `opta/parser.py`
- **File Size:** 21420 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** get rid of _ in the actual provider_id, we ,anage version with version_hashes

```
import json
import logging
from functools import lru_cache
from django.utils import timezone
from core.models import MatchEvent, Player, Action
import dateutil.parser

logger = logging.getLogger()

LabelStartPhase = 32
LabelEndPhase = 30
LabelGoal = 16
LabelOwnGoal = 16 # But qualifier
LabelYellowCard = 17
LabelRedCard = 17
LabelSubIn = 7
LabelSubOut = 8
LabelOutOfPlay = 9
LabelFoul = 10
LabelPass = 1
LabelReception = 12
LabelGoalAttempt = 13
LabelSaveOnGoalAttempt = 14
LabelInterception = 15
LabelGoalKick = 16
LabelCorner = 17
LabelThrowIn = 18
LabelPenalty = 19
LabelFreeKick = 20
LabelTouch = 21
LabelDribble = 22
LabelClearance = 23
LabelDefensiveBlock = 24
LabelDuel = 25
LabelOffside = 26
LabelFreeKickOnGoal = 27

# properties
PropertyOwnGoal = 28

PropertyRightFoot = 1
PropertyLeftFoot = 2
PropertyHead = 3
PropertyHigh = 4
PropertyDirect = 5
PropertyFakePass = 6
PropertyCross = 7
PropertyCompleted = 8
PropertyNotCompleted = 9
PropertyDirectionForwards = 10
PropertyDirectionWide = 11
PropertyDirectionBack = 12
PropertyDiagonalForwardDirection = 13
PropertyDiagonalBackDirection = 14
PropertyLengthShort = 15
PropertyLengthMedium = 16
PropertyLengthLong = 17
PropertyBadControl = 18
PropertyError = 19
PropertyBigChance = 20
PropertyAirDuel = 21
PropertyGroundDuel = 22
PropertyDuelWon = 23
PropertyDuelLost = 24
PropertyBody = 25
PropertySliding = 26
PropertyTouched = 27
PropertyUntouched = 28
PropertyShieldOpponent = 29
PropertyOvertakeOpponentLeft = 30
PropertyOvertakeOpponentRight = 31
PropertyBlocked = 32
PropertySaveAGoal = 33
PropertyTrajectoryUnchanged = 34
PropertyPossessionRegain = 35
PropertyPossessionLost = 36
PropertyInterception = 37
PropertyCurvedIn = 38
PropertyCurvedOut = 39
PropertyStraight = 40
PropertyAssist = 41
PropertyKeyAction = 42
PropertyGoal = 43
PropertySaved = 44
PropertyOnThePost = 45
PropertyOnTheCrossBar = 46
PropertyWide = 47
PropertyOver = 48
PropertyShotOnTarget = 49
PropertyShotOffTarget = 50
PropertyDisallowedGoal = 51
PropertyIncorrect = 52
PropertyOnDeepPass = 53
PropertyOnCrossPass = 54
PropertyPunched = 55
PropertyCaught = 56
PropertyGround = 57
PropertyStanding = 58
PropertyDiving = 59
PropertySixSecondRule = 60
PropertyDangerousPlay = 61
PropertyHands = 62
PropertyObstruction = 63
PropertyProtest = 64
PropertySimulation = 65
PropertyTimeDelay = 66
PropertySuccessfulSave = 67
PropertyUnsuccessfulSave = 68
PropertyOffensivePart = 69
PropertyDefensivePart = 70
PropertyCornerShort = 71
PropertyPassThrow = 72
PropertySubjectedToFoul = 73
PropertyFiftyFiftyDuels = 74
PropertyThrowinKeepPossession = 75
PropertyShotBlocked = 76
PropertyPassFromHand = 77
PropertyGoalAttemptFromBuildUp = 78
PropertyGoalAttemptFromOffensive = 79
PropertyGoalAttemptFromCounter = 80
PropertyGoalAttemptFromTurnOver = 81
PropertyGoalAttemptFromSetPlay = 82
PropertyThrowinLong = 83
PropertyThrowInToOpponentBox = 84
PropertyFinalThirdEntry = 85

# player ones
Action70 = 70  # Last Line Save
Action71 = 71  # Last Man Tackle
Action36 = 36  # Defensive Block
Action32 = 32  # Tackle - Won
Action31 = 31  # Interception
Action33 = 33  # Tackle - Won (without Possession)
Action38 = 38  # Effective Clearance
Action18 = 18  # Aerial Duel - Won
Action19 = 19  # Aerial Duel - Lost
Action26 = 26  # Foul - Conceded
Action57 = 57  # Penalty Conceded
Action49 = 49  # Own Goal
Action27 = 27  # Handball Conceded
Action58 = 58  # Yellow Card
Action59 = 59  # 2nd Yellow Card
Action60 = 60  # Red Card
Action69 = 69  # Won Corner
Action73 = 73  # Penalty Won
Action61 = 61  # Great Skill
Action55 = 55  # Successful Take On (dribble)
Action25 = 25  # Foul - Won
Action67 = 67  # Dispossessed
Action56 = 56  # Unsuccessful dribble
Action62 = 62  # Big Error - lead to shot
Action80 = 80  # Goalkeeper Save
Action37 = 37  # Goalkeeper Claim
Action75 = 75  # Goalkeeper Punch
Action77 = 77  # Keeper pick-up
Action87 = 87  # Goal Kick  Successful
Action85 = 85  # Goalkeeper Throw - Successful
Action88 = 88  # Goal Kick Unsuccessful
Action79 = 79  # Cross not claimed
Action7 = 7  # Assist
Action8 = 8  # Key Pass
Action68 = 68  # Through Ball
Action5 = 5  # Successful Cross - Bonus
Action29 = 29  # Corners Into box - Successful
Action2 = 2  # Pass - Successful
Action3 = 3  # Pass - Unsuccessful
Action6 = 6  # Unsuccessful Crosses Total (excl corners & freekicks)
Action86 = 86  # Goalkeeper Throw - Unsuccessful
Action64 = 64  # Big Error - lead to goal
Action45 = 45  # Goal
Action63 = 63  # Shot hit the Post
Action43 = 43  # Shot on Target
Action53 = 53  # Shot Blocked
Action44 = 44  # Shot off Target
Action65 = 65  # Caught Offside
Action72 = 72  # Big Chance Missed
Action74 = 74  # Penalty Missed

# system ones
ActionPeriodStart = 10001
ActionPeriodEnd = 10002
ActionGoal = 10003
ActionSelfGoal = 10004
ActionLineUp = 10005
ActionMatchEnd = 10006
ActionSubstitution = 10007

# no operation
ActionNoop = 20000

# cancel
ActionCancel = 30000

# typeId / property = qualifier
# "properties_values" => a dict where key = property value / value = actual value that property could have
ActionRules = {
    # Goal
    Action45: [{ "labels": [16], "excluded_properties": [28] }],

    # Assist
    # Action7: [{ "labels": [1], "properties": [210], "properties_values": { 210: ["16"] }, "outcomes": [1] }],

    # Penalty Won
    Action73: [{ "labels": [4], "properties": [9], "outcomes": [1] }],

    # Shot Hit Post
    Action63: [{ "labels": [14], "outcomes": [1] }],

    # Goalkeeper Save
    Action80: [{ "labels": [10], "excluded_properties": [94] }],

    # Shot On Target
    Action43: [{ "labels": [15], "excluded_properties": [9, 82] }],

    # Key Pass
    Action8: [{ "labels": [1], "properties": [210], "properties_values": { 210: ["13", "14", "15"] } }],

    # Successful Cross - Bonus
    Action5: [{ "labels": [1], "properties": [2], "excluded_properties": [5, 6], "outcomes": [1] }],

    # Through Ball
    Action68: [{ "labels": [1], "properties": [4], "outcomes": [1] }],

    # Shot off Target
    Action44: [{ "labels": [13], "excluded_properties": [214] }],

    # Won Corner
    Action69: [{ "labels": [6] }],

    # Corners Into box - Successful
    Action29: [{ "labels": [1], "properties": [2, 6], "outcomes": [1] }],

    # Pass - Successful
    Action2: [{ "labels": [1], "excluded_properties": [210,2,4,5,6,107,123,124], "outcomes": [1] }],

    # Foul - Conceded - has to be 0
    Action26: [{ "labels": [4], "outcomes": [0], "excluded_properties": [10] }],

    # 2nd Yellow Card
    Action59: [{ "labels": [17], "properties": [32], "outcomes": [1] }],

    # Yellow Card
    Action58: [{ "labels": [17], "properties": [31], "outcomes": [1] }],

    # Penalty Missed
    Action74: [{ "labels": [15], "properties": [9] }],

    # Own Goal
    Action49: [{ "labels": [16], "properties": [28] }],

    # Red Card
    Action60: [{ "labels": [17], "properties": [33], "outcomes": [1] }],

    # Last Line Save
    Action70: [{ "labels": [10], "properties": [101], "outcomes": [1] }],

    # Last Man Tackle
    Action71: [{ "labels": [7], "properties": [14], "outcomes": [1] }],

    # Defensive Block
    Action36: [{ "labels": [10], "properties": [94], "outcomes": [1] }],

    # Great Skill
    Action61: [{ "labels": [42], "outcomes": [1] }],

    # Shot Blocked
    Action53: [{ "labels": [15], "properties": [82], "outcomes": [1] }],

    # Tackle Won
    Action32: [{ "labels": [7], "outcomes": [1], "excluded_properties": [14] }],

    # Successful Take On
    Action55: [{ "labels": [3], "outcomes": [1] }],

    # Goalkeeper Claim
    Action37: [{ "labels": [11], "properties": [88], "outcomes": [1] }],

    # Interception
    Action31: [{ "labels": [8], "outcomes": [1] }],

    # Tackle - Won (without Possession)
    Action33: [{ "labels": [7], "outcomes": [0] }],

    # Effective Clearance
    Action38: [{ "labels": [12], "outcomes": [1] }],

    # Aerial Duel - Won
    Action18: [{ "labels": [44], "outcomes": [1] }],

    # Foul - Won
    Action25: [{ "labels": [4], "outcomes": [1], "excluded_properties": [9] }],

    # Keeper pick-up
    Action77: [{ "labels": [52], "outcomes": [1] }],

    # Goalkeeper Throw - Successful
    Action85: [{ "labels": [1], "properties": [123], "outcomes": [1] }],

    # Goal Kick Successful
    Action87: [{ "labels": [1], "properties": [124], "outcomes": [1] }],

    # Goal Kick Unsuccessful - has to be 0
    Action88: [{ "labels": [1], "properties": [124], "outcomes": [0] }],

    # Aerial Duel - Lost - has to be 0
    Action19: [{ "labels": [44], "outcomes": [0] }],

    # Unsuccessful dribble - has to be 0
    Action56: [{ "labels": [3], "outcomes": [0] }],

    # Dispossessed
    Action67: [{ "labels": [50], "outcomes": [1] }],

    # Goalkeeper Throw - Unsuccessful - has to be 0
    Action86: [{ "labels": [1], "properties": [123], "outcomes": [0] }],

    # Unsuccessful Crosses Total - has to be 0
    Action6: [{ "labels": [1], "properties": [2], "excluded_properties": [5, 6], "outcomes": [0] }],

    # Pass - Unsuccessful - has to be 0
    Action3: [{ "labels": [1], "excluded_properties": [2, 4, 5, 6, 107, 123, 124], "outcomes": [0] }],

    # Handball Conceded - has to be 0
    Action27: [{ "labels": [4], "properties": [10], "outcomes": [0] }],

    # Caught Offside
    Action65: [{ "labels": [2], "properties": [7], "outcomes": [1] }],

    # Cross not claimed - has to be 1
    Action79: [{ "labels": [53], "outcomes": [1] }],

    # Big Error - lead to shot
    Action62: [{ "labels": [51], "properties": [169], "outcomes": [1] }],

    # Penalty Conceded - has to be 1
    Action57: [{ "labels": [4], "properties": [9], "outcomes": [0] }],

    # Big Error - lead to goal
    Action64: [{ "labels": [51], "properties": [170] }],

    # Big Chance Missed
    Action72: [{ "labels": [13], "properties": [214], "outcomes": [1] }],

    # Goalkeeper Punch
    Action75: [{ "labels": [41], "properties": []}],

    # # Successful Take On
    # Action55: [{ "labels": [3], "properties": [], "outcomes": [1] }],

    # # Aerial Duel - Lost - has to be 0
    # # Action19: [{ "labels": [44], "properties": [], "outcomes": [0] }],

    #   Aerial Total
    #   Action17: [{ "labels": [21], "properties": [25]}],
    #
    #   Clearance Lost - has to be 0
    #   Action39: [{ "labels": [21], "properties": [25]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action30: [{ "labels": [90,9], "properties": [17]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action28: [{ "labels": [], "properties": [17]}],
    #
    #   Crosses Total (Open Delay)
    #   Action4: [{ "labels": [7], "properties": [11]}],
    #
    #   Defensive/backward Passes
    #   Action12: [{ "labels": [], "properties": [11]}],
    #
    #   Fouls Total
    #   Action24: [{ "labels": [], "properties": [10]}],
    #
    #   Free Kicks Taken Total
    #   Action23: [{ "labels": [], "properties": [20, 27]}],
    #
    #   Goals from Open Play
    #   Action46: [{ "labels": [], "properties": [13, 19, 27], "excluded_properties": [82]}],
    #
    #   Goals from Penalties
    #   Action48: [{ "labels": [], "properties": [43, 19]}],
    #
    #   Goals from Set Plays
    #   Action47: [{ "labels": [82], "properties": [13, 27]}],
    #
    #   Ground Duels Lost - has to be 0
    #   Action22: [{ "labels": [22, 23], "properties": [25]}],
    #
    #   Ground Duels Total
    #   Action20: [{ "labels": [22], "properties": [25]}],
    #
    #   Ground Duels Won
    #   Action21: [{ "labels": [22, 24], "properties": [25]}],
    #
    #   Headed Clearance Lost - has to be 0
    #   Action41: [],
    #
    #   Headed Clearance Won
    #   Action40: [],
    #
    #   Headed Shots off Target
    #   Action52: [{ "labels": [3,50], "properties": [13]}],
    #
    #   Headed Shots on Target
    #   Action50: [{ "labels": [3,49], "properties": [13]}],
    #
    #   Headed Shots Total
    #   Action-: [{ "labels": [3], "properties": [13]}],
    #
    #   Long Passes Lost - has to be 0
    #   Action-: [{ "labels": [9,17], "properties": [11]}],
    #
    #   Long Passes total
    #   Action-: [{ "labels": [17], "properties": []}],
    #
    #   Long Passes Won
    #   Action-: [{ "labels": [8], "properties": [11]}],
    #
    #   Offensive Passes Lost - has to be 0
    #   Action-: [{ "labels": [9], "properties": [11]}],
    #
    #   Offensive Passes Total
    #   Action-: [{ "labels": [], "properties": [11]}],
    #
    #   Offensive Passes Won
    #   Action-: [{ "labels": [8], "properties": [11]}],
    #
    #   Passes Total
    #   Action-: [{ "labels": [], "properties": [11]}],
    #
    #   Saves Total
    #   Action-: [{ "labels": [], "properties": [14]}],
    #
    #   Sideway Passes Total
    #   Action-: [{ "labels": [11], "properties": [11]}],
    #
    #   Total Shots
    #   Action-: [{ "labels": [], "properties": [13,19,27]}],
    #
    #   Total Touches
    #   Action-: [{ "labels": [], "properties": [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27]}],
}

def extract_match_events(match, event_body):
    minute = event_body.get("timeMin", 0)
    second = event_body.get("timeSec", 0)
    result = []

    matched_actions = match_actions(match, event_body)

    # calculate how much minutes we should add, this depends on period
    """
    opta values:
    • 1 (First half)
    • 2 (Second half)
    • 3 (Extra time - first half)
    • 4 (Extra time - second half)
    • 5 (Penalty shootout)
    • 10 (Half time)
    • 11 (End of second half - before extra time)
    • 12 (Extra time half time)
    • 13 (End of extra time - before penalties)
    • 14 (Full time)
    • 16 (Pre-match)
    """
    current_period = event_body.get("periodId", 0)

    # reduce matched_actions to action with max points if goal or assist present
    should_reduce = False
    for action in matched_actions:
        if action[0] in (ActionGoal, ActionSelfGoal, Action7, Action43):
            # print("should_reduce action: {}".format(action[0]))
            should_reduce = True
            break

    if should_reduce:
        # print("matched_actions before: {}".format(matched_actions))
        non_point_actions = []
        # find action with biggest points
        max_action = None
        for action in matched_actions:
            if not action[2]:
                non_point_actions.append(action)
                continue
            if max_action is None or action[2] > max_action[2]:
                max_action = action
        matched_actions = [max_action] + non_point_actions
        # print("matched_actions after: {}".format(matched_actions))

    if matched_actions is None:
        print("[matched_actions] IS NONE! - event_body: {}".format(event_body))

    for action in matched_actions:
        try:
            if action is None or action[0] == ActionNoop:
                continue
        except:
            print("[matched_actions] action failed: ", action)

        # try to find player and team by "person_id" and "selection_edition_id"
        player = None
        team = None

        player_id, team_id = None, None

        if action and action[3]:
            player_id = action[3]

        if action and action[4]:
            team_id = action[4]

        if player_id:
            player = get_player_by_person_id(player_id)
        if team_id:
            if match.is_opta_home_selection_from_match(team_id):
                team = match.home_team
            elif match.is_opta_away_selection_from_match(team_id):
                team = match.away_team

        match_event = MatchEvent()
        match_event.player = player
        match_event.team = team
        match_event.type = action[0]
        match_event.points = action[2]
        match_event.x = event_body.get("x", 0)
        match_event.y = event_body.get("y", 0)
        match_event.period = current_period
        match_event.minute = minute
        match_event.second = second
        match_event.payload = json.dumps(action[1])
        match_event.provider_id = event_body.get("id")
        if event_body.get('timeStamp'):
            match_event.timestamp = dateutil.parser.parse(event_body.get('timeStamp'))
            match_event.has_real_timestamp = True
        else:
            match_event.timestamp = timezone.now()
            match_event.has_real_timestamp = False

        result.append(match_event)

    return result

def match_actions(match, event_body):
    actions = []

    def cb(typ, payload=None, points=None, player_id=None, selection_edition_id=None):
        actions.append((typ, payload if payload else {}, points if points else 0, player_id, selection_edition_id))

    for finder in finders:
        finder(match, event_body, cb)

    if len(actions) == 0:
        # print("No action found for event", event_body.get("typeId"))
        actions.append((ActionNoop, {}, 0, None, None))
    return actions

def phase_finder(match, event_body, cb):
    label = event_body.get("typeId")
    periodId = event_body.get("periodId")
    if label == LabelStartPhase:
        cb(ActionPeriodStart, payload={"period_id": periodId})
    elif label == LabelEndPhase:
        cb(ActionPeriodEnd, payload={"period_id": periodId})

    """
    opta values:
    1 - first half
    2 - second half
    3 - first period of extra time
    4 - second period of extra time
    5 - penalty shoot out
    14 - post-game
    15 - pre-game
    16 - pre-match
    """

def goal_finder(match, event_body, cb):
    label = event_body.get("typeId")
    if label == (LabelGoal or LabelOwnGoal):
        for qualifier in event_body.get("qualifier", []):
            qualifierId = qualifier.get("qualifierId")
            if qualifierId == PropertyOwnGoal:
                cb(ActionSelfGoal, {}, Action.get_score_by_id(Action49), event_body.get("playerId"), event_body.get("contestantId"))
                return # set as own goal if done it, else, should be a score for the team
        cb(ActionGoal, {}, Action.get_score_by_id(Action45), event_body.get("playerId"), event_body.get("contestantId"))

def player_action_finder(match, event_body, cb):
        id = event_body.get("id")
        label = event_body.get("typeId")
        properties = event_body.get("qualifier", [])
        outcome = event_body.get("outcome", None)

        player_id = event_body.get("playerId", None)
        selection_edition_id = event_body.get("contestantId", None)
        rr = None
        if player_id is not None or selection_edition_id is not None:
            # iterate over rules and find corresponding actions
            for action_id, rules in ActionRules.items():
                for rule in rules:
                    if match_action(rule, label, properties, outcome, id):
                        cb(action_id, {}, Action.get_score_by_id(action_id),
                            player_id=player_id,
                            selection_edition_id=selection_edition_id)
                        rr = rule
                        break
        # print(f"id: {id} - label: {label} - rule: {rr}")

def match_action(rule, event_label, event_properties, outcome = None, id = None):
    labels = rule.get("labels", [])
    if len(labels) > 0:
        label_matched = False
        for rule_label in labels:
            if rule_label == "*" or rule_label == event_label:
                label_matched = True
                break

        if not label_matched:
            return False

    # check that all properties of rules are present in the event
    rule_properties = rule.get("properties", [])
    if len(rule_properties) > 0 and not all(elem in [e['qualifierId'] for e in event_properties] for elem in rule_properties):
        return False
    # if there are any related property values should match the event qualifier value
    property_values = rule.get("properties_values", None)
    if property_values is not None:
        for e in event_properties:
            values = property_values.get(e['qualifierId'], None)
            if values is not None and isinstance(values, list):
                if str(e.get("value")) not in values:
                    print(False)

    # check that there are no excluded properties present
    rule_excluded_properties = rule.get("excluded_properties", [])
    if len(rule_excluded_properties) > 0 and any(elem in [e['qualifierId'] for e in event_properties] for elem in rule_excluded_properties):
        return False

    possible_outcomes = rule.get("outcomes", [])
    if len(possible_outcomes) > 0 and outcome is not None and outcome not in possible_outcomes:
        return False

    return True

@lru_cache(maxsize=4096)
def get_player_by_person_id(player_id, fn=None, ln=None, nn=None, dob=None):
    try:
        return Player.objects.get(import_id=player_id)
    except Player.DoesNotExist:
        if player_id:
            return Player.objects.create(
                import_id=player_id,
                first_name=fn,
                last_name=ln,
                full_name="{} {}".format(fn, ln),
                nick_name=nn,
                birth_date= dob,
            )

def assist_finder(match, event_body, cb):
    label = event_body.get("typeId")
    if label == LabelPass and event_body.get("assist", 0) == 1 and event_body.get("outcome", 0) == 1:
        cb(Action7, {}, Action.get_score_by_id(Action7), event_body.get("playerId"), event_body.get("contestantId"))

finders = [
    goal_finder,
    phase_finder,
    assist_finder,
    player_action_finder,
]

```

## File: `opta/sync.py`
- **File Size:** 52333 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix finding existing items

```
import asyncio
import json
import logging
import time
import uuid
import traceback
from contextlib import contextmanager
from datetime import timedelta, datetime

from celery import shared_task
from django.conf import settings
from django.core.cache import cache
from django.db import transaction, IntegrityError
from django.utils import timezone
from django.utils.dateparse import parse_datetime, parse_date
from core import const
from core.models import (
    CompetitionConfig,
    Competition,
    CompetitionEdition,
    CompetitionPhase,
    Team,
    Match,
    Season,
    Player,
    OptaFeedItem,
    OptaFeedItemVersion,
    MatchEvent,
    MatchPlayer,
    SelectionTeamPlayer,
    EventThrottler,
    Sport,
    ChatRoom,
    CustomUser
)
from mobile_api.celery import WSocketEnabled
from rabbit.models import AMQPEvent
from opta.conv import POSITION_MAP
from opta.parser import (
    extract_match_events,
    ActionCancel,
    ActionMatchEnd,
    get_player_by_person_id,
    ActionLineUp,
    ActionPeriodStart,
    ActionPeriodEnd,
    ActionSubstitution,
    ActionGoal, ActionSelfGoal
)
from opta.utils import opta_format_parse_date
from util.events import create_amqp_event_from_match_event

logger = logging.getLogger('opta.sync')

MatchEndEventId = -1
HomeLineUpEventId = -200
AwayLineUpEventId = -201

LOCK_EXPIRE = 60 * 1  # Lock expires in 1 minutes

@contextmanager
def memcache_lock(lock_id, oid):
    timeout_at = time.monotonic() + LOCK_EXPIRE - 3
    # cache.add fails if the key already exists
    status = cache.add(lock_id, oid, LOCK_EXPIRE)
    try:
        yield status
    finally:
        # memcache delete is very slow, but we have to use it to take
        # advantage of using add() for atomic locking
        if time.monotonic() < timeout_at and status:
            # don't release the lock if we exceeded the timeout
            # to lessen the chance of releasing an expired lock
            # owned by someone else
            # also don't release the lock if we didn't acquire it
            cache.delete(lock_id)

def sync_competitions(filterBy=None, sportName=None):
    logger.info(f"[sync_competitions] START {datetime.now()}")

    # TODO: change to be multisport
    if sportName is None:
        sportName = "Soccer"

    sport = Sport.objects.get(name=sportName)

    for competition in settings.OPTA_CLIENT.get_competitions().get('competition'):
        filter = competition.get("competitionCode")
        if filterBy is not None and filterBy != filter:
            continue
        try:
            competition_config_record = CompetitionConfig.objects.get(enabled=True, filter=filter)
        except:
            continue
        if competition_config_record is not None:
            known_name = competition.get("knownName", competition.get("name"))
            name = competition.get("name")
            competition_record = update_or_create(
                Competition,
                import_id=competition.get('id'),
                name=known_name,
                short_name=name,
                updated_at=datetime.now(),
                sport=sport,
                config=competition_config_record
            )
            if competition_config_record.import_id is None:
                competition_config_record.import_id = competition.get('id')
                competition_config_record.name = known_name
                competition_config_record.related_competition = competition_record
                competition_config_record.updated_at = datetime.now()
                competition_config_record.save()
            # for each competition query editions
            for edition in competition.get('tournamentCalendar'):
                start_date = opta_format_parse_date(edition.get("startDate"))
                end_date = opta_format_parse_date(edition.get("endDate"))
                edition_record = update_or_create(
                    CompetitionEdition,
                    import_id=edition.get('id'),
                    name=edition.get("name"),
                    competition=competition_record,
                )
                # for each edition query phases
                season_record = None
                for phase in settings.OPTA_CLIENT.get_competition_phases(edition.get('id')).get('stage', []):
                    update_or_create(
                        CompetitionPhase,
                        import_id=phase.get('id'),
                        name=phase.get("name"),
                        competition_edition=edition_record,
                    )
                    season_record = update_or_create(
                        Season,
                        import_id=phase.get('id'),
                        name=phase.get("name"),
                        start_at=start_date,
                        end_at=end_date,
                    )
                if season_record is None and edition_record is not None:
                    season_record = update_or_create(
                        Season,
                        import_id=edition.get('id'),
                        name=edition.get("name"),
                        start_at=start_date,
                        end_at=end_date,
                    )
                # for each edition query schedule
                for matchDate in settings.OPTA_CLIENT.get_schedule(edition.get('id')).get('matchDate'):
                    for match in matchDate.get('match'):
                        try:
                            # from the match_record, we have homeContestantId (id) homeContestantOfficialName (name), homeContestantCode (abbr)
                            home_team = update_team_record(
                                match.get('homeContestantId'),
                                match.get('homeContestantOfficialName'),
                                match.get('homeContestantCode')
                            )
                            # same with awayContestant
                            away_team = update_team_record(
                                match.get('awayContestantId'),
                                match.get('awayContestantOfficialName'),
                                match.get('awayContestantCode')
                            )
                            d = match.get('date')
                            t = match.get('time')
                            if t is None or t == "":
                                t = "12:00:00Z"
                            dt = parse_datetime(f"{d[:-1] if 'Z' in d else d}T{t + 'Z' if 'Z' not in t else t}")
                            import_id = match.get('id')
                            matchInfo = settings.OPTA_CLIENT.get_match_stats(import_id, "no").get('matchInfo')
                            # -1 can be used to detect those matches that are not regular session (dont have week)
                            week = matchInfo.get('week') or -1
                            match_record = update_or_create(
                                Match,
                                import_id=import_id,
                                competition=competition_record,
                                edition=edition_record,
                                season=season_record,
                                home_team=home_team,
                                away_team=away_team,
                                home_team_selection_id=match.get('homeContestantId'),
                                away_team_selection_id=match.get('awayContestantId'),
                                match_time=dt,
                                match_type=Match.MATCH_TYPE_FREE,  # TODO: remove after beta
                                week=week,
                                sport=sport
                            )
                            update_or_create(ChatRoom,
                                             import_id=import_id,
                                             name=f"{home_team.name} v. {away_team.name} - {dt}",
                                             match=match_record)
                            match_record.sync_match_players()
                        except Exception as e:
                            logger.error("[sync_competitions] {}".format(e))

    logger.info("[sync_competitions] END sync {}".format(datetime.now()))

def update_team_record(id, name, abbr):
    return update_or_create(
        Team,
        import_id=id,
        name=name,
        abbr=abbr
        # opta_selection_id=record.get("Id"),
    )

def sync_all_teams():
    logger.info("[sync_all_teams] start - {}".format(datetime.now()))
    matches = Match.objects.filter(
        home_team_selection_id__isnull=False,
        away_team_selection_id__isnull=False,
        competition_id__isnull=False,
        simulation_from_match_id__isnull=True,
        match_time__gt=timezone.now() - timedelta(hours=10 * 24),
        match_time__lt=timezone.now() + timedelta(hours=30 * 24),
    ).select_related("edition").order_by(
        "-match_time")
    if len(matches) > 0:
        # get a list of a union between away_team_selection_id and home_team_selection_id
        combined_ids_dict = {}
        for match in matches:
            if match.edition.import_id in combined_ids_dict:
                combined_ids_dict[match.edition.import_id].extend(
                    [match.away_team_selection_id, match.home_team_selection_id])
                combined_ids_dict[match.edition.import_id] = list(set(combined_ids_dict[match.edition.import_id]))
            else:
                combined_ids_dict[match.edition.import_id] = [match.away_team_selection_id,
                                                              match.home_team_selection_id]

        for tournamentCalendarUuid in combined_ids_dict:
            for contestantUUID in combined_ids_dict[tournamentCalendarUuid]:
                sync_contestant(tournamentCalendarUuid, contestantUUID)

    logger.info(f"[sync_all_teams] END sync {datetime.now()}")

def sync_contestant(matchImportID, teamSelectionID):
    try:
        team_squad = settings.OPTA_CLIENT.get_selection_persons(matchImportID, teamSelectionID)
    except Exception as e:
        logger.error("[sync_all_teams] - failed to get team squad: {}".format(e))
        return
    for squad in team_squad.get('squad'):
        if squad is not None:
            with transaction.atomic():
                # delete all season team players for team
                SelectionTeamPlayer.objects.filter(selection_id=teamSelectionID).delete()
                for person in squad.get("person", []):
                    if person.get("active") == "no" or person.get("type") != "player":
                        continue
                    first_name = person.get("firstName")
                    last_name = person.get("lastName")
                    nick_name = person.get("matchName")
                    full_name = "{} {}".format(first_name, last_name)

                    player_record = update_or_create(
                        Player,
                        import_id=person.get("id"),
                        first_name=first_name,
                        last_name=last_name,
                        full_name=full_name,
                        nick_name=nick_name,
                        birth_date=parse_date(person.get("dateOfBirth")) if person.get(
                            "dateOfBirth") != None else None,
                        updated_at=datetime.now(),
                    )

                    jersey_number = person.get("shirtNumber")
                    active_selection = person.get("active") == "yes"
                    position = POSITION_MAP.get(person.get("position"))
                    if position is None:
                        logger.warn("[sync_all_teams] person with unknown position: {} - {} ".format(
                            person.get("position"), person.get("id")))
                        position = const.POSITION_UNKNOWN
                    # ignore substitute or unknown positions
                    # if position == const.POSITION_SUBSTITUTE or position == const.POSITION_UNKNOWN:
                    #     continue

                    # try to find season team player, if not exists, create new one
                    try:
                        tp = SelectionTeamPlayer.objects.filter(
                            selection_id=teamSelectionID,
                            player=player_record,
                        ).get()

                        if active_selection:
                            tp.jersey_number = jersey_number
                            tp.position = position
                            tp.updated_at = datetime.now()
                            tp.save()
                        else:
                            tp.delete()

                    except SelectionTeamPlayer.DoesNotExist:
                        if active_selection:
                            # create new season team player, if this doesn't exists
                            SelectionTeamPlayer.objects.create(
                                selection_id=teamSelectionID,
                                player=player_record,
                                jersey_number=jersey_number,
                                position=position,
                            )

@shared_task
def handle_ws_match_event_messages(message):
    match_id = message.get('content').get('liveData').get('matchDetails').get('id')
    try:
        match = Match.objects.get(import_id=match_id)
    except Match.DoesNotExist:
        logger.error("Match with import ID", match_id, "does not exist")
        return
    match_live_data = settings.OPTA_CLIENT.get_match_stats(match_id)
    match_live_data = match_live_data.get('liveData')
    process_event_message(message, match, match_live_data)

def prepare_match_event_items(live_events, match_live_data, match_record):
    items = []
    # print('live_events', live_events)
    # print('match_live_data', match_live_data)
    match_status = match_live_data.get('matchDetails', {}).get('matchStatus', [])
    if len(live_events) > 0:
        period_events = {}
        # store the substitution events in a list
        OPTA_SUBSTITUTION_TYPE_ID = 18  # Player off
        substitution_events = []
        for item in live_events:
            if item.get("typeId") == OPTA_SUBSTITUTION_TYPE_ID:
                substitution_events.append(item)
            # parse events
            match_events = extract_match_events(match_record, item)
            if match_events is None:
                logger.warn("[sync_feed] match_events IS NONE! - item: {}".format(item))
            # modify current period based on ActionPeriodStart event
            for ev in match_events:
                if ev.type == ActionPeriodStart:
                    # get payload and try to understand this period just started
                    if ev.payload:
                        payload = json.loads(ev.payload)
                        if payload and payload.get("period_id"):
                            if period_events.get(payload.get("period_id")) is not None:
                                break
                            period_events[payload.get("period_id")] = ev
                elif ev.type == ActionPeriodEnd:
                    # get payload and try to understand this period just ended
                    if ev.payload:
                        payload = json.loads(ev.payload)
                        if payload and payload.get("period_id"):
                            if period_events.get(payload.get("period_id")) is not None:
                                break
                            period_events[payload.get("period_id")] = ev
                elif ev.type in (ActionGoal, ActionSelfGoal):
                    goal = MatchEvent(item.get('match_events'))

                version_hash = new_version_hash(item)

                unique_id = item.get("id")

                items.append(
                    {
                        "unique_id": unique_id,
                        "event_id": unique_id,
                        "version": version_hash,
                        "match_events": match_events,
                    }
                )

        substitutions = match_live_data.get('substitute')
        # parse sustitutions and make events out of these
        if substitutions is not None:
            for substitution in substitutions:
                player_in = substitution.get("playerOnId")
                player_out = substitution.get("playerOffId")
                team_import_id = substitution.get("contestantId")
                # The players must be stored already, from the lineUps
                player_in_record = get_player_by_person_id(player_in)
                player_out_record = get_player_by_person_id(player_out)
                if player_in_record and player_out_record:
                    # find the substition event where the player in and player out are the same as the substitution event
                    substitution_event = next((x for x in substitution_events if x.get("playerId") == player_out), None)
                    if substitution_event is None:
                        continue
                    # create substitution event
                    mev = MatchEvent()
                    mev.team = Team.objects.get(import_id=team_import_id)
                    mev.type = ActionSubstitution
                    mev.provider_id = str(substitution_event.get("id"))
                    mev.timestamp = substitution.get("timestamp")
                    mev.minute, mev.second = int(substitution.get("timeMinSec").split(":")[0]), int(
                        substitution.get("timeMinSec").split(":")[1])
                    mev.x, mev.y = 0, 0
                    mev.payload = json.dumps(
                        {
                            "player_in_id": str(player_in_record.pk),
                            "player_out_id": str(player_out_record.pk),
                        }
                    )
                    items.append(
                        {
                            "unique_id": mev.provider_id,
                            "event_id": mev.provider_id,
                            "version": "1",
                            "match_events": [mev],
                        }
                    )
                else:
                    logger.warn("[sync_feed] Error: player not found for substitution (in/out): {} {}".format(player_in,
                                                                                                              player_out))
                    logger.warn("[sync_feed] Error: substitution object => {}".format(substitution))

        if len(period_events) > 0:
            if match_status == "Played":
                endEvent = period_events.get(max(period_events.keys()))
                mev = MatchEvent()
                mev.type = ActionMatchEnd
                mev.provider_id = endEvent.provider_id
                mev.timestamp = endEvent.timestamp
                mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0
                # insert match ended event
                items.append(
                    {
                        "unique_id": MatchEndEventId,
                        "event_id": MatchEndEventId,
                        "version": "1",
                        "match_events": [mev],
                    }
                )
        return items

def process_event_message(message, match_record, match_live_data):
    live_events = message.get('content').get('liveData').get('matchDetails').get('event', [])
    start_sync = datetime.now()

    items = prepare_match_event_items(live_events, match_live_data, match_record)
    with transaction.atomic():
        # process items inside transaction
        try:
            process_items(match_record, items, delete_not_found_existing=False)
            logger.info("[sync_feed] END  WS sync - import_id: {} - total time: {}".
                        format(match_record.import_id, datetime.now() - start_sync))
        except Exception as e:
            traceback.print_exc()
            logger.error(
                "[sync_feed] - import_id: {} - Error with transaction.atomic: {}".format(match_record.import_id, e))

@shared_task
def start_websocket_listener(import_id):
    cache_id = f"{import_id}-subscribed"

    if cache.get(cache_id):
        print("WebSocket listener is already running.")
        return

    cache.set(cache_id, True, timeout=10800)  # 3hours
    try:
        loop = asyncio.get_event_loop()

        if not loop.is_running():
            print("Starting WebSocket listener.")
            loop.run_until_complete(sync_match_with_ws(import_id))
        else:
            asyncio.run(sync_match_with_ws(import_id))
    finally:
        cache.delete(cache_id)

async def sync_match_with_ws(import_id):
    client = settings.OPTA_WS_CLIENT
    # force_sync_match(Match.objects.get(import_id=import_id))
    await client.connect(import_id, handle_ws_match_event_messages)

def sync_matches(match_time_delta=12, skip_sync_delay=False, competition_code=None, force_SDAPI: bool = False):
    # NOTE: for testing purposes, we can skip sync delay by setting this to True
    # sync feed for all matches within period [now - 12 hours; now + 12 hours]
    dbFilteredMatches = Match.objects.filter(
        match_time__gt=timezone.now() - timedelta(hours=match_time_delta),
        match_time__lt=timezone.now() + timedelta(hours=match_time_delta),
        enabled=True,  # Sync only enabled matches?
    ).order_by("match_time").select_related("competition")
    for match in dbFilteredMatches:
        if not match.competition.enabled:
            # print(f"{match.competition.name} is disabled, skip.")
            continue
        # skip if the competition_code is set and the current match record is NOT from that competition
        if competition_code and match.competition.code != competition_code:
            continue

        if not skip_sync_delay:
            now = timezone.now()
            # calculate sync_delay
            if (match.match_time - now) > timedelta(minutes=30):
                # 30 min before match
                sync_delay = timedelta(seconds=settings.SYNC_DELAY_BEFORE_MATCH)
            else:
                sync_delay = timedelta(seconds=settings.SYNC_DELAY_DURING_MATCH)

            if match.last_synced_at and match.last_synced_at > (now - sync_delay):
                continue

        # ignore ended matches
        if match.status == const.MATCH_STATUS_ENDED:
            continue

        # sync match feed
        try:
            sync_match(match, force_SDAPI)
        except Exception as e:
            logger.error(
                "[sync_matches] Error occurred on sync_match {} - {} error: {}".format(match.pk, match.import_id, e))
            import traceback
            traceback.print_exc()

        match.last_synced_at = timezone.now()
        match.save(update_fields=["last_synced_at"])
        # return #to debug step by step just one match

def sync_match(match_record: Match, force_SDAPI: bool = False):
    if match_record.simulation_from_match is not None:
        return

    lock_id = f"{match_record.pk}-lock-{force_SDAPI}"
    print(f"trying to lock {lock_id}, force_SDAPI: {force_SDAPI}")
    with memcache_lock(lock_id, "match-lock") as acquired:
        if acquired:
            print(f"lock {lock_id} acquired")
            # match = load_json_file("opta/api_responses/matchstats_detailed.jsonc")
            match = settings.OPTA_CLIENT.get_match_stats(match_record.import_id)
            sync_feed(match_record, match, force_SDAPI=force_SDAPI)
        else:
            print(f"lock {lock_id} not acquired")

def force_sync_match_with_lock(match_record: Match):
    if match_record.simulation_from_match is not None:
        return

    lock_id = "{0}-lock".format(match_record.pk)
    with memcache_lock(lock_id, "match-lock") as acquired:
        if acquired:
            force_sync_match(match_record)

def force_sync_match(match_record: Match):
    match = settings.OPTA_CLIENT.get_match_stats(match_record.import_id)
    force_sync_feed(match_record, match)

def make_lineup_item(players, team_id, event_id):
    mev = MatchEvent()
    mev.type = ActionLineUp
    mev.provider_id = str(event_id)
    mev.timestamp = timezone.now()
    mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0
    mev.payload = json.dumps({"players": players})
    mev.team_id = team_id

    return {
        "unique_id": event_id,
        "event_id": event_id,
        "version": "1",
        "match_events": [mev],
    }

def sync_feed(match_record: Match, matchData: dict, data_feed_sim: bool = False, force_SDAPI: bool = False):
    # THIS IS DIRTY HACK TO AVOID MATCH BEING STUCKED
    if force_SDAPI:
        if match_record.rewarded and match_record.status == const.MATCH_STATUS_GAME:
            logger.error("[sync_feed] MATCH BEING STUCKED, MANUALLY SET ENDED")
            time.sleep(5)
            match_record.refresh_from_db()
            if match_record.rewarded and match_record.status == const.MATCH_STATUS_GAME:
                match_record.status = const.MATCH_STATUS_ENDED
                match_record.save(update_fields=["status"])

    startSync = datetime.now()
    logger.info("[sync_feed] START sync - import_id: {}".format(match_record.import_id))
    matchInfo = matchData.get('matchInfo')
    # print(matchInfo)
    matchLiveData = matchData.get('liveData')
    # print(matchLiveData)
    contestants = matchInfo.get('contestant')
    home_team = None
    away_team = None
    # iterate contestants and figure if there are away and home teams
    for contestant in contestants:
        if contestant.get('position') == "home":
            home_team = contestant
        elif contestant.get('position') == "away":
            away_team = contestant
    # if there is no exactly one home team ans one away team then return with an error message
    if not home_team or not away_team:
        return f"Error: There must be exactly one home team and one away team. match: {match_record.pk} - {match_record.import_id}"
    # if the home team and away team are not the same as the match record then return with an error message
    if home_team.get('id') != match_record.home_team_selection_id or away_team.get(
            'id') != match_record.away_team_selection_id:
        return f"Error: Home team or away team is not the same as the match record. match: {match_record.pk} - {match_record.import_id}"

    # sync home and away team
    if force_SDAPI:
        update_team_record(home_team.get('id'), home_team.get('name'), home_team.get('code'))
        update_team_record(away_team.get('id'), away_team.get('name'), away_team.get('code'))

    matchStatus = matchLiveData.get('matchDetails').get('matchStatus')

    if matchStatus == "Played" or matchStatus == "Playing" or matchStatus == "Fixture":
        items = []
        if force_SDAPI:
            # opta's matchevent object
            home_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("home", 0)
            away_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("away", 0)
            match_record.home_score = home_score
            match_record.away_score = away_score
            # sync match players, get it from line ups
            home_lineup_players = []
            away_lineup_players = []
            lineups = matchLiveData.get("lineUp", [])
            # save the score right away
            if not data_feed_sim:
                match_record.save(update_fields=['home_score', 'away_score', 'has_lineups'])

            for lineup in lineups:
                selectionEditionId = lineup.get("contestantId")  # team id
                for player in lineup.get("player"):
                    player_record = get_player_by_person_id(player.get("playerId"), player.get("firstName"),
                                                            player.get("lastName"), player.get("matchName"),
                                                            player.get("dateOfBirth"))
                    position = POSITION_MAP.get(player.get("position"))
                    if position is None:
                        position = const.POSITION_UNKNOWN
                    jersey_number = player.get("shirtNumber")

                    if not match_record.is_opta_selection_from_match(selectionEditionId):
                        continue

                    lineup_player = {
                        "id": str(player_record.pk),
                        "jersey_number": jersey_number,
                        "position": position,
                    }
                    if match_record.is_opta_home_selection_from_match(selectionEditionId):
                        home_lineup_players.append(lineup_player)
                    elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                        away_lineup_players.append(lineup_player)

                    # check existence of match player, if it's not exists - create new one
                    try:
                        mp = MatchPlayer.objects.get(player=player_record, match=match_record)
                        if not mp.from_lineups:
                            mp.position = position
                            mp.jersey_number = jersey_number
                            mp.from_lineups = True
                            mp.updated_at = datetime.now()
                            mp.save()

                    except MatchPlayer.DoesNotExist:
                        match_player_team = None
                        if match_record.is_opta_home_selection_from_match(selectionEditionId):
                            match_player_team = match_record.home_team
                        elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                            match_player_team = match_record.away_team

                        if match_player_team:
                            try:
                                MatchPlayer.objects.create(
                                    match=match_record,
                                    player=player_record,
                                    team=match_player_team,
                                    position=position,
                                    jersey_number=jersey_number,
                                    from_lineups=True,
                                )
                            except IntegrityError:
                                pass
                    except MatchPlayer.MultipleObjectsReturned:
                        pass

            # consider each event as item
            if len(home_lineup_players) > 0:
                items.append(
                    make_lineup_item(home_lineup_players, match_record.home_team_id, HomeLineUpEventId)
                )
            if len(away_lineup_players) > 0:
                items.append(
                    make_lineup_item(away_lineup_players, match_record.away_team_id, AwayLineUpEventId)
                )

        if (not force_SDAPI) and WSocketEnabled and matchStatus != "Played" and (
                match_record.simulation_from_match is None):
            match_time = match_record.match_time
            if (match_time - timedelta(minutes=90)) < timezone.now() < (match_time + timedelta(minutes=180)):
                start_websocket_listener.delay(match_record.import_id)
        elif (not WSocketEnabled and matchStatus != "Played") or force_SDAPI:
            live_events = matchLiveData.get("event", None)
            if live_events is None:
                # live_events = load_json_file("opta/api_responses/match_events.jsonc").get('liveData').get('event')
                try:
                    events_from_provider = settings.OPTA_CLIENT.get_match_events(match_record.import_id)
                except:
                    events_from_provider = {}
                live_events = events_from_provider.get('liveData', {}).get('event', [])

            items.extend(prepare_match_event_items(live_events, matchLiveData, match_record))
            with transaction.atomic():
                # process items inside transaction
                try:
                    process_items(match_record, items, data_feed_sim, delete_not_found_existing=not force_SDAPI)
                    logger.info("[sync_feed] END sync - import_id: {} - total time: {}".
                                format(match_record.import_id, datetime.now() - startSync))
                except Exception as e:
                    traceback.print_exc()
                    logger.error(
                        "[sync_feed] - import_id: {} - Error with transaction.atomic: {}".format(match_record.import_id,
                                                                                                 e))
    else:
        print("[sync_feed] match playing nor played. import_id: {} - status {}".format(match_record.import_id,
                                                                                       matchStatus))

def force_sync_feed(match_record: Match, matchData: dict, data_feed_sim: bool = False):
    startSync = datetime.now()
    logger.info("[sync_feed] START FORCE sync - import_id: {}".format(match_record.import_id))
    matchInfo = matchData.get('matchInfo')
    # print(matchInfo)
    matchLiveData = matchData.get('liveData')
    # print(matchLiveData)
    contestants = matchInfo.get('contestant')
    home_team = None
    away_team = None
    # iterate contestants and figure if there are away and home teams
    for contestant in contestants:
        if contestant.get('position') == "home":
            home_team = contestant
        elif contestant.get('position') == "away":
            away_team = contestant
    # if there is no exactly one home team ans one away team then return with an error message
    if not home_team or not away_team:
        return f"Error: There must be exactly one home team and one away team. match: {match_record.pk} - {match_record.import_id}"
    # if the home team and away team are not the same as the match record then return with an error message
    if home_team.get('id') != match_record.home_team_selection_id or away_team.get(
            'id') != match_record.away_team_selection_id:
        return f"Error: Home team or away team is not the same as the match record. match: {match_record.pk} - {match_record.import_id}"

    # sync home and away team
    update_team_record(home_team.get('id'), home_team.get('name'), home_team.get('code'))
    update_team_record(away_team.get('id'), away_team.get('name'), away_team.get('code'))

    matchStatus = matchLiveData.get('matchDetails').get('matchStatus')

    if matchStatus == "Played" or matchStatus == "Playing" or matchStatus == "Fixture":
        # opta's matchevent object
        home_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("home", 0)
        away_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("away", 0)
        match_record.home_score = home_score
        match_record.away_score = away_score
        # sync match players, get it from line ups
        home_lineup_players = []
        away_lineup_players = []
        lineups = matchLiveData.get("lineUp", [])
        # save the score right away
        if not data_feed_sim:
            match_record.save()
        for lineup in lineups:
            selectionEditionId = lineup.get("contestantId")  # team id
            for player in lineup.get("player"):
                player_record = get_player_by_person_id(player.get("playerId"), player.get("firstName"),
                                                        player.get("lastName"), player.get("matchName"),
                                                        player.get("dateOfBirth"))
                position = POSITION_MAP.get(player.get("position"))
                if position is None:
                    position = const.POSITION_UNKNOWN
                jersey_number = lineup.get("shirtNumber")

                if not match_record.is_opta_selection_from_match(selectionEditionId):
                    continue

                lineup_player = {
                    "id": str(player_record.pk),
                    "jersey_number": jersey_number,
                    "position": position,
                }
                if match_record.is_opta_home_selection_from_match(selectionEditionId):
                    home_lineup_players.append(lineup_player)
                elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                    away_lineup_players.append(lineup_player)

                # check existence of match player, if it's not exists - create new one
                try:
                    mp = MatchPlayer.objects.get(player=player_record, match=match_record)
                    if not mp.from_lineups:
                        mp.position = position
                        mp.jersey_number = jersey_number
                        mp.from_lineups = True
                        mp.updated_at = datetime.now()
                        mp.save()

                except MatchPlayer.DoesNotExist:
                    match_player_team = None
                    if match_record.is_opta_home_selection_from_match(selectionEditionId):
                        match_player_team = match_record.home_team
                    elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                        match_player_team = match_record.away_team

                    if match_player_team:
                        try:
                            MatchPlayer.objects.create(
                                match=match_record,
                                player=player_record,
                                team=match_player_team,
                                position=position,
                                jersey_number=jersey_number,
                                from_lineups=True,
                            )
                        except IntegrityError:
                            pass

        # consider each event as item
        items = []

        if len(home_lineup_players) > 0:
            items.append(
                make_lineup_item(home_lineup_players, match_record.home_team_id, HomeLineUpEventId)
            )
        if len(away_lineup_players) > 0:
            items.append(
                make_lineup_item(away_lineup_players, match_record.away_team_id, AwayLineUpEventId)
            )

        if match_record.simulation_from_match is None:
            live_events = matchLiveData.get("event", None)
            if live_events is None:
                # live_events = load_json_file("opta/api_responses/match_events.jsonc").get('liveData').get('event')
                try:
                    events_from_provider = settings.OPTA_CLIENT.get_match_events(match_record.import_id)
                except:
                    events_from_provider = {}
                live_events = events_from_provider.get('liveData', {}).get('event', [])

            items = prepare_match_event_items(live_events, matchLiveData, match_record)
            with transaction.atomic():
                # process items inside transaction
                try:
                    process_items(match_record, items, data_feed_sim)
                    logger.info("[sync_feed] END sync - import_id: {} - total time: {}".
                                format(match_record.import_id, datetime.now() - startSync))
                except Exception as e:
                    traceback.print_exc()
                    logger.error(
                        "[sync_feed] - import_id: {} - Error with transaction.atomic: {}".format(match_record.import_id,
                                                                                                 e))
    else:
        logger.info("[sync_feed] match playing nor played. import_id: {} - status {}".format(match_record.import_id,
                                                                                             matchStatus))

def process_items(match_record: Match, incoming_events: list, debug: bool = False, delete_not_found_existing=True):
    if incoming_events is None:
        return
    # first of all select all existing items
    existing_items = OptaFeedItem.objects.select_related("current_version").filter(
        match=match_record
    )
    new_added_items = set()

    new_match_events = []
    updated_item_count = 0
    new_item_count = 0

    found_in_incoming = set()

    # handle updated items
    for event in incoming_events:
        existing_item_to_process = None

        # find existing one
        for existing in existing_items:
            if existing.unique_id == str(event.get("unique_id")) and existing.event_id == str(event.get("event_id")):
                # new version for item
                if existing.current_version.version != event.get("version"):
                    existing_item_to_process = existing
                break

        # no changes
        if not existing_item_to_process:
            continue

        # select existing match events for opta_feed_item excluding cancel events
        existing_match_items = MatchEvent.objects.filter(
            opta_feed_item_version=existing_item_to_process.current_version
        )

        to_create, to_delete, non_changed = get_diff_actions(
            existing_match_items, event.get("match_events")
        )

        # calculate status for item
        if len(to_create) == 0 and len(to_delete) == 0:
            new_status = OptaFeedItemVersion.NO_DIFF
        elif len(to_delete) == len(existing_match_items):
            new_status = OptaFeedItemVersion.FULL_CANCEL
        else:
            new_status = OptaFeedItemVersion.PARTIAL_CANCEL

        # update status of item
        existing_item_to_process.current_version.status = new_status
        existing_item_to_process.current_version.save(update_fields=["status"])

        # create new item version
        new_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=event.get("version"),
            last_modified_at=timezone.now(),
            item=existing_item_to_process,
        )

        # update reference from item to version
        existing_item_to_process.current_version = new_version
        existing_item_to_process.save(update_fields=["current_version"])

        # generate cancel event actions as part of new version
        for delete_mev in to_delete:
            new_match_events.append(
                generate_cancel_match_event(delete_mev, new_version)
            )

        for mev in to_create:
            mev.opta_feed_item_version = new_version
            new_match_events.append(mev)

        # change link to new version
        for mev in non_changed:
            mev.opta_feed_item_version = new_version
            mev.save(update_fields=["opta_feed_item_version"])

        updated_item_count += 1

    # handle new items
    for event in incoming_events:
        unique_id = event.get("unique_id")
        event_id = event.get("event_id")
        version = event.get("version")

        if unique_id is None:
            logger.info("[process_items] Error: unique_id is None => {}".format(event.get('match_events')[0].type))
            continue

        found = False
        # find existing one
        for existing in existing_items:
            if existing.unique_id == str(unique_id) and existing.event_id == str(event_id):
                found_in_incoming.add(existing.pk)
                found = True
                break

        if found:
            continue

        if event_id in new_added_items:
            continue

        # concurrency issue, continue, will update on next iteration
        if OptaFeedItem.objects.filter(
                unique_id=unique_id,
                event_id=event_id,
                match=match_record,
        ).exists():
            continue

        # insert feed item
        feed_item = OptaFeedItem.objects.create(
            unique_id=unique_id,
            event_id=event_id,
            match=match_record,
        )
        new_added_items.add(event_id)

        # insert version
        feed_item_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=version,
            last_modified_at=timezone.now(),
            item=feed_item,
        )

        # update feed link
        feed_item.current_version = feed_item_version
        feed_item.save(update_fields=["current_version"])

        for mev in event.get("match_events"):
            mev.opta_feed_item_version = feed_item_version
            new_match_events.append(mev)

        new_item_count += 1

    # delete items that not found in incoming feed
    deleted_item_count = 0
    deleted_events_count = 0

    if delete_not_found_existing:
        for item in existing_items:
            if item.pk in found_in_incoming:
                continue

            # get all match events for current_version
            active_match_events = (
                MatchEvent.objects.filter(
                    opta_feed_item_version=item.current_version_id,
                    status=MatchEvent.ACTIVE,
                )
                .exclude(type=ActionCancel)
                .all()
            )

            if len(active_match_events) == 0:
                # no match_event to delete, it means this event was already cancelled
                continue

            # update status of item
            if item.current_version is not None:
                item.current_version.status = OptaFeedItemVersion.FULL_CANCEL
                item.current_version.save(update_fields=["status"])

            # create new item version
            new_version = OptaFeedItemVersion.objects.create(
                status=OptaFeedItemVersion.ACTIVE,
                # random uuid as new version
                version=uuid.uuid4(),
                last_modified_at=timezone.now(),
                item=item,
            )

            # update reference from item to version
            item.current_version = new_version
            item.save(update_fields=["current_version"])

            for delete_mev in active_match_events:
                new_match_events.append(
                    generate_cancel_match_event(delete_mev, new_version)
                )
                deleted_events_count += 1

            deleted_item_count += 1

    if debug:
        logger.info(f'''[process_items] updated item count: {updated_item_count}
new item count: {new_item_count}
deleted item count: {deleted_item_count}
deleted event count: {deleted_events_count}''')

    # insert match events
    # logger.info("[process_items] new_events len is", len(new_match_events))
    for match_event in new_match_events:
        # empty pk to make sure we're creating new records
        match_event.pk = None
        match_event.match = match_record
        match_event.match_event_id = MatchEvent.objects.filter(match=match_record).count() + 1
        match_event.save()

        # insert amqp event as well
        # TODO: should we disable this? uncommenting the next line will activate:
        create_amqp_event_from_match_event(match_event)

def generate_cancel_match_event(delete_mev, new_version):
    mev = MatchEvent()
    mev.type = ActionCancel
    mev.payload = json.dumps(
        {
            "id": delete_mev.id,
        }
    )
    mev.minute = 0
    mev.second = 0
    mev.opta_feed_item_version = new_version
    mev.timestamp = timezone.now()

    return mev

def get_diff_actions(prev, next):
    # make copy of prev, cause it will be modified
    prev = list(prev)

    to_create = []
    non_changed = []

    for next_event in next:
        # find even in prev
        foundIdx = -1

        for idx, prev_event in enumerate(prev):
            # same event found
            if is_equal(prev_event, next_event):
                foundIdx = idx
                break

        if foundIdx != -1:
            non_changed.append(prev[foundIdx])
            del prev[foundIdx]
        else:
            to_create.append(next_event)

    # all events that are left in prev should be deleted
    to_delete = prev

    return to_create, to_delete, non_changed

def is_equal(a, b):
    # return False
    # #a.get("player_id") == b.get("player_id") and \
    #            #a.get("team_id") == b.get("team_id") and \
    return a.type == b.type and a.points == b.points and a.payload == b.payload

def update_or_create(cls, **kwargs):
    # find pk
    import_id = kwargs.get("import_id")
    with transaction.atomic():
        try:
            obj = cls.objects.select_for_update().get(import_id=import_id)

            changed = False
            for k, v in kwargs.items():
                # check for any change
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    changed = True

            # call save only if there was any changes
            if changed:
                if obj.updated_at is not None:
                    obj.updated_at = datetime.now()
                obj.save()

            return obj

        except cls.DoesNotExist:
            return cls.objects.create(**kwargs)

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

async def process_match_record(match_record):
    lock_id = "{0}-lock".format(match_record.pk)
    with memcache_lock(lock_id, "match-lock") as acquired:
        if acquired:
            match_stats_api = settings.OPTA_CLIENT.get_match_stats(match_record.import_id)
        week = match_stats_api.get('matchInfo').get('week') or -1
        match_record = update_or_create(
            Match,
            import_id=match_record.import_id,
            week=week,
        )

async def sync_match_no_week():
    import asyncio
    match_records = Match.objects.filter(week=0, simulation_from_match__isnull=True)
    tasks = []
    for match_record in match_records:
        task = asyncio.create_task(process_match_record(match_record))
        tasks.append(task)

    await asyncio.gather(*tasks)

def calculate_unique_id(*args):
    return calculate_hash(*args)[:48]

def calculate_hash(*args):
    # make sure all args are transofrmed to string
    args = [str(arg) for arg in args]
    import hashlib
    concatenated_string = '::'.join(args)
    hash_obj = hashlib.sha512()
    hash_obj.update(concatenated_string.encode('utf-8'))
    return hash_obj.hexdigest()

def process_event_throttling():
    events = EventThrottler.objects.filter(processing=False).order_by('created_at')
    if len(events) > 0:
        sleep_delta = settings.AMQP_THROTTLING_THRESHOLD / len(events)
        EventThrottler.objects.filter(id__in=events).update(processing=True)
        for event in events:
            time.sleep(sleep_delta)
            AMQPEvent.objects.create(
                exchange=event.exchange,
                event_type=event.event_type,
                data=event.data
            )
            event.delete()

def new_version_hash(item):
    lastModified = item.get("lastModified")
    timeStamp = item.get("timeStamp")
    # if the timestamp AND lastModified date string ends with the character "Z", remove it to ensure it's the same as SDDP
    if lastModified and lastModified[-1] == 'Z':
        lastModified = lastModified[:-1]
    if timeStamp and timeStamp[-1] == 'Z':
        timeStamp = timeStamp[:-1]

    parts = [
        item.get("typeId"), item.get("periodId"), item.get("timeMin"), item.get("timeSec"),
        item.get("contestantId"), item.get("playerId"), item.get("outcome"), item.get("assist", "0"),
        timeStamp, lastModified
    ]

    item_qualifiers = item.get("qualifier", [])
    qualifiers = sorted(item_qualifiers, key=lambda x: x.get("qualifierId"))

    paired_qualifiers = [
        f'{q.get("qualifierId", "0")}:{q.get("value", "None")}' for q in qualifiers
    ]

    parts.extend(paired_qualifiers)

    return '#'.join([str(p) for p in parts])

```

## File: `opta/utils.py`
- **File Size:** 334 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix division users

```
from datetime import datetime
import pytz

def opta_format_parse_date(date_str: str) -> datetime:
    # Parse the date string assuming it's in the format YYYY-MM-DDZ
    parsed_date = datetime.strptime(date_str, "%Y-%m-%dZ")
    # Set the timezone to UTC
    parsed_date = parsed_date.replace(tzinfo=pytz.UTC)
    return parsed_date

```

## File: `opta/websocket.py`
- **File Size:** 3117 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** read from websocket with timeout

```
from django.conf import settings
from django.core.cache import cache
import asyncio
import websockets
import json
from websockets_proxy import Proxy, proxy_connect
from concurrent.futures import TimeoutError

class OptaWebSocketClient:
    def __init__(self, outlet_auth_key):
        self.uri = 'wss://content.performgroup.io'
        self.outletAuthKey = outlet_auth_key
        self.feedName = ['MatchEvent']
        self.ws_conn = None

    async def connect(self, import_id, handler):
        proxy_url = f"http://{settings.OPTA_PROXY}"
        proxy = Proxy.from_url(proxy_url)

        print(f"connecting to import_id {import_id} using proxy {proxy_url}")
        is_available = False
        is_authorized = False
        is_subscribed = False
        async with proxy_connect(self.uri, proxy=proxy) as websocket:
            self.ws_conn = websocket

            if not is_available:
                resp = await websocket.recv()
                msg = json.loads(resp)
                print(resp)
                if msg['welcome'] is not None:
                    is_available = True
                else:
                    asyncio.sleep(1)
            if not is_authorized:
                outlet_object = {'outlet': {'OutletKeyService': {'outletid': self.outletAuthKey}}}
                req = json.dumps(outlet_object)
                await self.ws_conn.send(req)
                resp = await self.ws_conn.recv()
                msg = json.loads(resp)
                print(msg)
                if 'outlet' in msg:
                    if msg.get('outlet', {}).get('msg') == "is_authorised":
                        print("Authorized successfully.")
                        is_authorized = True

            if not is_subscribed:
                subscription_obj = {
                    "name": "subscribe",
                    "feed": self.feedName,
                    "fixtureUuid": import_id,
                }

                req = json.dumps({"content": subscription_obj})
                await self.ws_conn.send(req)
                resp = await self.ws_conn.recv()
                msg = json.loads(resp)
                print(msg)
                if msg.get("content", {}).get('msg') == "is_subscribed":
                    match_id = msg.get("content").get('fixture')
                    if match_id and (import_id == match_id):
                        print(f"Match {match_id} is subscribed.")
                        is_subscribed = True
            print(is_available, is_authorized, is_subscribed)
            if is_available and is_authorized and is_subscribed:
                print('while for handle messages')
                while True:
                    try:
                        message = await asyncio.wait_for(self.ws_conn.recv(), 60)
                        print('listen messages')
                        msg = json.loads(message)
                        print(msg)
                        handler.apply_async(args=[msg])
                        continue
                    except TimeoutError as e:
                        print('timeout happens reading ws messages')

```

## File: `ortec/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `ortec/api.py`
- **File Size:** 2225 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
import logging
import requests
from cachetools import TTLCache

logger = logging.getLogger()

class OrtecAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # 30 minutes cache
        self.token_cache = TTLCache(maxsize=10, ttl=60 * 30)

    @staticmethod
    def _build_url(path):
        return 'https://sports.ortec-hosting.com/EIADataFeedApi{}'.format(path)

    def get_token(self):
        try:
            return self.token_cache['token']
        except KeyError:
            token = self.generate_new_token()
            self.token_cache['token'] = token
            return token

    def generate_new_token(self):
        url = self._build_url('/api/token')
        res = requests.post(url, json={"username": self.username, "password": self.password})
        return res.json()

    def get_competitions(self):
        return self._process_request('/api/Competition')

    def get_competition_editions(self, competition_id):
        return self._process_request('/api/Competition/competitioneditions/{}'.format(competition_id))

    def get_competition_phases(self, competition_edition_id):
        return self._process_request('/api/Competition/competitionphases/{}'.format(competition_edition_id))

    def get_registrations(self, competition_phase_id):
        return self._process_request('/api/Competition/competitionphases/{}/registrations'.format(competition_phase_id))

    def get_registration(self, registration_id):
        return self._process_request('/api/RegistrationData/{}'.format(registration_id))

    def get_selection_persons(self, selection_id):
        return self._process_request('/api/selections/persons/{}'.format(selection_id))

    def _process_request(self, path, data=None):
        final_url = self._build_url(path)
        logger.info("Making request to {}".format(final_url))

        res = requests.get(final_url, data, headers={
            'Authorization': 'Session {}'.format(self.get_token())
        })

        if res.status_code != 200:
            raise Exception(
                'Received invalid status code {} for {}: {}'.format(res.status_code, final_url, res.content))
        return res.json()

```

## File: `ortec/conv.py`
- **File Size:** 1979 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from core import const

POSITION_MAP = {
    1: const.POSITION_GOALKEEPER,  # goalkeeper
    2: const.POSITION_DEFENDER,  # sweeper
    3: const.POSITION_DEFENDER,  # left-back
    4: const.POSITION_DEFENDER,  # left-centre-back
    5: const.POSITION_DEFENDER,  # centre-back
    6: const.POSITION_DEFENDER,  # right-centre-back
    7: const.POSITION_DEFENDER,  # right-back
    8: const.POSITION_DEFENDER,  # left-wing-back
    9: const.POSITION_DEFENDER,  # right-wing-back
    10: const.POSITION_MIDFIELDER,  # defensive-midfield-centre-left
    11: const.POSITION_MIDFIELDER,  # defensive-midfield-centre
    12: const.POSITION_MIDFIELDER,  # defensive-midfield-centre-right
    13: const.POSITION_MIDFIELDER,  # left-midfield
    14: const.POSITION_MIDFIELDER,  # left-centre-midfield
    15: const.POSITION_MIDFIELDER,  # centre-midfield
    16: const.POSITION_MIDFIELDER,  # right-centre-midfield
    17: const.POSITION_MIDFIELDER,  # right-midfield
    18: const.POSITION_MIDFIELDER,  # attacking-midfield-left
    19: const.POSITION_MIDFIELDER,  # attacking-midfield-centre-left
    20: const.POSITION_MIDFIELDER,  # attacking-midfield
    21: const.POSITION_MIDFIELDER,  # attacking-midfield-centre-right
    22: const.POSITION_MIDFIELDER,  # attacking-midfield-right
    23: const.POSITION_FORWARD,  # left-winger
    24: const.POSITION_FORWARD,  # second striker
    25: const.POSITION_FORWARD,  # right-winger
    26: const.POSITION_FORWARD,  # centre-forward-left
    27: const.POSITION_FORWARD,  # centre-forward
    28: const.POSITION_FORWARD,  # centre-forward-right
    29: const.POSITION_SUBSTITUTE,  # bench
    30: const.POSITION_UNKNOWN,  # assistent referee
    31: const.POSITION_UNKNOWN,  # fourth official
    32: const.POSITION_UNKNOWN,  # goal line referee
    33: const.POSITION_UNKNOWN,  # referee
}

POSITION_DEFENDER = 'd'
POSITION_MIDFIELDER = 'm'
POSITION_FORWARD = 'f'
POSITION_GOALKEEPER = 'g'
POSITION_SUBSTITUTE = 's'
POSITION_UNKNOWN = 'u'

```

## File: `ortec/parser.py`
- **File Size:** 19059 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** BETA fix for matches

```
import json
import logging
from functools import lru_cache
from django.utils import timezone
from core.models import MatchEvent, Player, Action
import dateutil.parser

logger = logging.getLogger()

LabelStartPhase = 1
LabelEndPhase = 2
LabelGoal = 3
LabelOwnGoal = 4
LabelYellowCard = 5
LabelRedCard = 6
LabelSubIn = 7
LabelSubOut = 8
LabelOutOfPlay = 9
LabelFoul = 10
LabelPass = 11
LabelReception = 12
LabelGoalAttempt = 13
LabelSaveOnGoalAttempt = 14
LabelInterception = 15
LabelGoalKick = 16
LabelCorner = 17
LabelThrowIn = 18
LabelPenalty = 19
LabelFreeKick = 20
LabelTouch = 21
LabelDribble = 22
LabelClearance = 23
LabelDefensiveBlock = 24
LabelDuel = 25
LabelOffside = 26
LabelFreeKickOnGoal = 27

# properties
PropertyRightFoot = 1
PropertyLeftFoot = 2
PropertyHead = 3
PropertyHigh = 4
PropertyDirect = 5
PropertyFakePass = 6
PropertyCross = 7
PropertyCompleted = 8
PropertyNotCompleted = 9
PropertyDirectionForwards = 10
PropertyDirectionWide = 11
PropertyDirectionBack = 12
PropertyDiagonalForwardDirection = 13
PropertyDiagonalBackDirection = 14
PropertyLengthShort = 15
PropertyLengthMedium = 16
PropertyLengthLong = 17
PropertyBadControl = 18
PropertyError = 19
PropertyBigChance = 20
PropertyAirDuel = 21
PropertyGroundDuel = 22
PropertyDuelWon = 23
PropertyDuelLost = 24
PropertyBody = 25
PropertySliding = 26
PropertyTouched = 27
PropertyUntouched = 28
PropertyShieldOpponent = 29
PropertyOvertakeOpponentLeft = 30
PropertyOvertakeOpponentRight = 31
PropertyBlocked = 32
PropertySaveAGoal = 33
PropertyTrajectoryUnchanged = 34
PropertyPossessionRegain = 35
PropertyPossessionLost = 36
PropertyInterception = 37
PropertyCurvedIn = 38
PropertyCurvedOut = 39
PropertyStraight = 40
PropertyAssist = 41
PropertyKeyAction = 42
PropertyGoal = 43
PropertySaved = 44
PropertyOnThePost = 45
PropertyOnTheCrossBar = 46
PropertyWide = 47
PropertyOver = 48
PropertyShotOnTarget = 49
PropertyShotOffTarget = 50
PropertyDisallowedGoal = 51
PropertyIncorrect = 52
PropertyOnDeepPass = 53
PropertyOnCrossPass = 54
PropertyPunched = 55
PropertyCaught = 56
PropertyGround = 57
PropertyStanding = 58
PropertyDiving = 59
PropertySixSecondRule = 60
PropertyDangerousPlay = 61
PropertyHands = 62
PropertyObstruction = 63
PropertyProtest = 64
PropertySimulation = 65
PropertyTimeDelay = 66
PropertySuccessfulSave = 67
PropertyUnsuccessfulSave = 68
PropertyOffensivePart = 69
PropertyDefensivePart = 70
PropertyCornerShort = 71
PropertyPassThrow = 72
PropertySubjectedToFoul = 73
PropertyFiftyFiftyDuels = 74
PropertyThrowinKeepPossession = 75
PropertyShotBlocked = 76
PropertyPassFromHand = 77
PropertyGoalAttemptFromBuildUp = 78
PropertyGoalAttemptFromOffensive = 79
PropertyGoalAttemptFromCounter = 80
PropertyGoalAttemptFromTurnOver = 81
PropertyGoalAttemptFromSetPlay = 82
PropertyThrowinLong = 83
PropertyThrowInToOpponentBox = 84
PropertyFinalThirdEntry = 85

# player ones
Action70 = 70  # Last Line Save
Action71 = 71  # Last Man Tackle
Action36 = 36  # Defensive Block
Action32 = 32  # Tackle - Won
Action31 = 31  # Interception
Action33 = 33  # Tackle - Won (without Possession)
Action38 = 38  # Effective Clearance
Action18 = 18  # Aerial Duel - Won
Action19 = 19  # Aerial Duel - Lost
Action26 = 26  # Foul - Conceded
Action57 = 57  # Penalty Conceded
Action49 = 49  # Own Goal
Action27 = 27  # Handball Conceded
Action58 = 58  # Yellow Card
Action59 = 59  # 2nd Yellow Card
Action60 = 60  # Red Card
Action69 = 69  # Won Corner
Action73 = 73  # Penalty Won
Action61 = 61  # Great Skill
Action55 = 55  # Successful Take On (dribble)
Action25 = 25  # Foul - Won
Action67 = 67  # Dispossessed
Action56 = 56  # Unsuccessful dribble
Action62 = 62  # Big Error - lead to shot
Action80 = 80  # Goalkeeper Save
Action37 = 37  # Goalkeeper Claim
Action75 = 75  # Goalkeeper Punch
Action77 = 77  # Keeper pick-up
Action87 = 87  # Goal Kick  Successful
Action85 = 85  # Goalkeeper Throw - Successful
Action88 = 88  # Goal Kick Unsuccessful
Action79 = 79  # Cross not claimed
Action7 = 7  # Assist
Action8 = 8  # Key Pass
Action68 = 68  # Through Ball
Action5 = 5  # Successful Cross - Bonus
Action29 = 29  # Corners Into box - Successful
Action2 = 2  # Pass - Successful
Action3 = 3  # Pass - Unsuccessful
Action6 = 6  # Unsuccessful Crosses Total (excl corners & freekicks)
Action86 = 86  # Goalkeeper Throw - Unsuccessful
Action64 = 64  # Big Error - lead to goal
Action45 = 45  # Goal
Action63 = 63  # Shot hit the Post
Action43 = 43  # Shot on Target
Action53 = 53  # Shot Blocked
Action44 = 44  # Shot off Target
Action65 = 65  # Caught Offside
Action72 = 72  # Big Chance Missed
Action74 = 74  # Penalty Missed

# system ones
ActionPeriodStart = 10001
ActionPeriodEnd = 10002
ActionGoal = 10003
ActionSelfGoal = 10004
ActionLineUp = 10005
ActionMatchEnd = 10006
ActionSubstitution = 10007

# no operation
ActionNoop = 20000

# cancel
ActionCancel = 30000

ActionRules = {
    # Goal
    Action45: [{"properties": [], "labels": [3]}],

    # Assist
    Action7: [{"properties": [41], "labels": []}],

    # Penalty Won
    Action73: [{"properties": [89], "labels": []}],

    # Shot Hit Post
    Action63: [{"properties": [45], "labels": [13, 19, 27]},
               {"properties": [46], "labels": [13, 19, 27]}],

    # Shot On Target
    Action43: [{"properties": [49], "labels": [13, 19, 27]}],

    # Goalkeeper Save
    Action80: [{"properties": [67], "labels": [14]}],

    # Last Line Save
    Action70: [{"properties": [33], "labels": [24]}],

    # Shot Blocked
    Action53: [{"properties": [76], "labels": [13, 27]}],

    # Defensive Block
    Action36: [{"properties": [32], "labels": [24]}],

    # Tackle Won
    Action32: [{"properties": [22, 23, 70, 35], "labels": [25]}],

    # Successful Take On
    Action55: [{"properties": [30, 23], "labels": [25]},
               {"properties": [31, 23], "labels": [25]}],

    # Goalkeeper Claim
    Action37: [{"properties": [4, 56], "labels": [15]}],

    # Interception
    Action31: [{"properties": [37], "labels": []}],

    # Key Pass
    Action8: [{"properties": [42], "labels": []}],

    # Tackle - Won (without Possession)
    Action33: [{"properties": [22, 23, 70], "labels": [25], "excluded_properties": [35]}],

    # Shot off Target
    Action44: [{"properties": [47], "labels": [13, 19, 27]},
               {"properties": [48], "labels": [13, 19, 27]}],

    # Successful Cross - Bonus
    Action5: [{"properties": [7, 8], "labels": [11]}],

    # Goalkeeper Punch
    Action75: [{"properties": [55], "labels": [15]}],

    # Through Ball
    Action68: [{"properties": [91], "labels": [11]}],

    # Won Corner
    Action69: [{"properties": [86], "labels": []}],

    # Corners Into box - Successful
    Action29: [{"properties": [8, 90], "labels": [17]}],

    # Effective Clearance
    Action38: [{"properties": [], "labels": [23]}],

    # Aerial Duel - Won
    Action18: [{"properties": [21, 23], "labels": [25]}],

    # Foul - Won
    Action25: [{"properties": [73], "labels": [25]}],

    # Keeper pick-up
    Action77: [{"properties": [53, 56], "labels": [15], "excluded_properties": [4]}],

    # Goalkeeper Throw - Successful
    Action85: [{"properties": [8, 72], "labels": [11]}],

    # Goal Kick Successful
    Action87: [{"properties": [8], "labels": [16]}],

    # Pass - Successful
    Action2: [{"properties": [8], "labels": [11], "excluded_properties": [7]}],

    # Goal Kick Unsuccessful
    Action88: [{"properties": [9], "labels": [16]}],

    # Unsuccessful dribble
    Action56: [{"properties": [36], "labels": [22]}],

    # Unsuccessful Crosses Total
    Action6: [{"properties": [7, 9], "labels": [11]}],

    # Dispossessed
    Action67: [{"properties": [22, 36, 69], "labels": [25]}],

    # Foul - Conceded
    Action26: [{"properties": [], "labels": [10], "excluded_properties": [62, 88]}],

    # Aerial Duel - Lost
    Action19: [{"properties": [21, 22], "labels": [25]}],

    # Pass - Unsuccessful
    Action3: [{"properties": [9], "labels": [11], "excluded_properties": [7]}],

    # Handball Conceded
    Action27: [{"properties": [62], "labels": [10]}],

    # Caught Offside
    Action65: [{"properties": [], "labels": [26]}],

    # 2nd Yellow Card
    Action59: [{"properties": [92], "labels": [5]}],

    # Big Error - lead to shot
    Action62: [{"properties": [19], "labels": ["*"]}],

    # Yellow Card
    Action58: [{"properties": [], "labels": [5]}],

    # Penalty Conceded
    Action57: [{"properties": [88], "labels": [10]}],

    # Big Chance Missed
    Action72: [{"properties": [20], "labels": [13, 19, 27], "excluded_properties": [43]}],

    # Penalty Missed
    Action74: [{"properties": [], "labels": [19], "excluded_properties": [43]}],

    # Own Goal
    Action49: [{"properties": [], "labels": [4]}],

    # Red Card
    Action60: [{"properties": [], "labels": [6]}],

    #   Aerial Total
    #   Action17: [{"properties": [21], "labels": [25]}],
    #
    #   Clearance Lost
    #   Action39: [{"properties": [21], "labels": [25]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action30: [{"properties": [90,9], "labels": [17]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action28: [{"properties": [], "labels": [17]}],
    #
    #   Crosses Total (Open Delay)
    #   Action4: [{"properties": [7], "labels": [11]}],
    #
    #   Defensive/backward Passes
    #   Action12: [{"properties": [], "labels": [11]}],
    #
    #   Fouls Total
    #   Action24: [{"properties": [], "labels": [10]}],
    #
    #   Free Kicks Taken Total
    #   Action23: [{"properties": [], "labels": [20, 27]}],
    #
    #   Goals from Open Play
    #   Action46: [{"properties": [], "labels": [13, 19, 27], "excluded_properties": [82]}],
    #
    #   Goals from Penalties
    #   Action48: [{"properties": [], "labels": [43, 19]}],
    #
    #   Goals from Set Plays
    #   Action47: [{"properties": [82], "labels": [13, 27]}],
    #
    #   Ground Duels Lost
    #   Action22: [{"properties": [22, 23], "labels": [25]}],
    #
    #   Ground Duels Total
    #   Action20: [{"properties": [22], "labels": [25]}],
    #
    #   Ground Duels Won
    #   Action21: [{"properties": [22, 24], "labels": [25]}],
    #
    #   Headed Clearance Lost
    #   Action41: [],
    #
    #   Headed Clearance Won
    #   Action40: [],
    #
    #   Headed Shots off Target
    #   Action52: [{"properties": [3,50], "labels": [13]}],
    #
    #   Headed Shots on Target
    #   Action50: [{"properties": [3,49], "labels": [13]}],
    #
    #   Headed Shots Total
    #   Action-: [{"properties": [3], "labels": [13]}],
    #
    #   Long Passes Lost
    #   Action-: [{"properties": [9,17], "labels": [11]}],
    #
    #   Long Passes total
    #   Action-: [{"properties": [17], "labels": []}],
    #
    #   Long Passes Won
    #   Action-: [{"properties": [8], "labels": [11]}],
    #
    #   Offensive Passes Lost
    #   Action-: [{"properties": [9], "labels": [11]}],
    #
    #   Offensive Passes Total
    #   Action-: [{"properties": [], "labels": [11]}],
    #
    #   Offensive Passes Won
    #   Action-: [{"properties": [8], "labels": [11]}],
    #
    #   Passes Total
    #   Action-: [{"properties": [], "labels": [11]}],
    #
    #   Saves Total
    #   Action-: [{"properties": [], "labels": [14]}],
    #
    #   Sideway Passes Total
    #   Action-: [{"properties": [11], "labels": [11]}],
    #
    #   Total Shots
    #   Action-: [{"properties": [], "labels": [13,19,27]}],
    #
    #   Total Touches
    #   Action-: [{"properties": [], "labels": [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27]}],
}

def extract_match_events(match, current_period, event_body):
    annotation = get_annotation(event_body)
    if not annotation:
        return []

    minute, second = get_min_sec(event_body.get("Time", 0))
    result = []
    idx = 1

    matched_actions = match_actions(match, event_body)

    # calculate how much minutes we should add, this depends on period
    """
     ortec values:
    1 - 1st half
    2 - 2nd half
    3 - 1st extra time
    4 - 2nd extra time
    5 - penalties
    """
    add_min = 0
    if current_period == 1:
        add_min = 0
    elif current_period == 2:
        add_min = 45
    elif current_period == 3:
        add_min = 90
    elif current_period == 4:
        add_min = 105
    elif current_period == 5:
        add_min = 120

    # reduce matched_actions to action with max points if goal or assist present
    should_reduce = False
    for action in matched_actions:
        if action[0] in (ActionGoal, ActionSelfGoal, Action7, Action43):
            should_reduce = True
            break

    if should_reduce:
        non_point_actions = []

        # find action with biggest points
        max_action = None
        for action in matched_actions:
            if not action[2]:
                non_point_actions.append(action)
                continue

            if max_action is None or action[2] > max_action[2]:
                max_action = action

        matched_actions = [max_action] + non_point_actions

    for action in matched_actions:
        # try to find player and team by "person_id" and "selection_edition_id"
        player = None
        team = None

        player_id, team_id = None, None
        if action[3]:
            player_id = action[3]
        elif "PersonId" in annotation:
            player_id = str(annotation.get("PersonId"))

        if action[4]:
            team_id = action[4]
        elif "SelectionEditionId" in annotation:
            team_id = str(annotation.get("SelectionEditionId"))

        if player_id:
            player = get_player_by_person_id(player_id)
        if team_id:
            if match.is_ortec_home_selection_from_match(team_id):
                team = match.home_team
            elif match.is_ortec_away_selection_from_match(team_id):
                team = match.away_team

        match_event = MatchEvent()
        match_event.player = player
        match_event.team = team
        match_event.type = action[0]
        match_event.points = action[2]
        match_event.x = annotation.get("LocationX", 0)
        match_event.y = annotation.get("LocationY", 0)
        match_event.minute = minute + add_min
        match_event.second = second
        match_event.payload = json.dumps(action[1])
        match_event.provider_id = "{}_{}".format(annotation.get("Id"), idx)
        if event_body.get('DateTime'):
            match_event.timestamp = dateutil.parser.parse(event_body.get('DateTime'))
            match_event.has_real_timestamp = True
        else:
            match_event.timestamp = timezone.now()
        match_event.period = current_period
        result.append(match_event)

        idx += 1

    return result

def get_annotation(event_body):
    annotations = event_body.get("Annotations", [])
    if len(annotations) == 0:
        return None

    return annotations[0]

def get_min_sec(millis):
    mins = int(millis / 1000 / 60)
    secs = int(millis / 1000 % 60)
    return mins, secs

def match_actions(match, event_body):
    actions = []

    def cb(typ, payload=None, points=None, player_id=None, selection_edition_id=None):
        actions.append((typ, payload if payload else {}, points if points else 0, player_id, selection_edition_id,))

    for finder in finders:
        finder(match, event_body, cb)

    if len(actions) == 0:
        actions.append((ActionNoop, {}, 0, None, None))

    return actions

def phase_finder(match, event_body, cb):
    phase = event_body.get("Phase")
    label = get_annotation(event_body).get("Label")

    # convert phase to opta format
    if phase == 1:
        phase_converted = 1
    elif phase == 2:
        phase_converted = 2
    elif phase == 3:
        phase_converted = 3
    elif phase == 4:
        phase_converted = 4
    elif phase == 5:
        phase_converted = 5
    else:
        phase_converted = 0

    if label == LabelStartPhase:
        cb(ActionPeriodStart, payload={"period_id": phase_converted})
    elif label == LabelEndPhase:
        cb(ActionPeriodEnd, payload={"period_id": phase_converted})

    """
    ortec values:
    1 - 1st half
    2 - 2nd half
    3 - 1st extra time
    4 - 2nd extra time
    5 - penalties

    opta values:
    1 - first half
    2 - second half
    3 - first period of extra time
    4 - second period of extra time
    5 - penalty shoot out
    14 - post-game
    15 - pre-game
    16 - pre-match
    """

def goal_finder(match, event_body, cb):
    label = get_annotation(event_body).get("Label")

    # goal
    if label == 3:
        cb(ActionGoal)
    elif label == 4:
        cb(ActionSelfGoal)

def player_action_finder(match, event_body, cb):
    annotations = event_body.get("Annotations", [])
    for an in annotations:
        label = an.get("Label")
        properties = an.get("Properties", [])

        player_id = str(an.get("PersonId"))
        selection_edition_id = str(an.get("SelectionEditionId"))

        # iterate over rules and find corresponding actions
        for action_id, rules in ActionRules.items():
            for rule in rules:
                if match_action(rule, label, properties):
                    cb(action_id, {}, Action.get_score_by_id(action_id),
                       player_id=player_id,
                       selection_edition_id=selection_edition_id)
                    break

def match_action(rule, event_label, event_properties):
    labels = rule.get("labels", [])

    if len(labels) > 0:
        label_matched = False
        for rule_label in labels:
            if rule_label == "*" or rule_label == event_label:
                label_matched = True
                break

        if not label_matched:
            return False

    # check that all properties of rules is present
    for p in rule.get("properties", []):
        if not (p in event_properties):
            return False

    # check that there are no excluded properties present
    for p in rule.get("excluded_properties", []):
        if p in event_properties:
            return False

    return True

def substitution_finder(match, event_body, cb):
    annotations = event_body.get("Annotations", [])

    sub_in, sub_out = None, None
    for an in annotations:
        if an.get("Label") == LabelSubIn:
            sub_in = an
        elif an.get("Label") == LabelSubOut:
            sub_out = an

    if not sub_in or not sub_out:
        return

    player_in = get_player_by_person_id(sub_in.get("PersonId"))
    player_out = get_player_by_person_id(sub_out.get("PersonId"))

    cb(ActionSubstitution, {
        "in_player_id": str(player_in.id),
        "out_player_id": str(player_out.id),
    })

@lru_cache(maxsize=4096)
def get_player_by_person_id(person_id):
    try:
        return Player.objects.get(import_id=person_id)
    except Player.DoesNotExist:
        return Player.objects.create(
            import_id=person_id,
            first_name="John",
            last_name="Doe",
        )

finders = [
    phase_finder,
    goal_finder,
    substitution_finder,
    player_action_finder,
]

```

## File: `ortec/sync.py`
- **File Size:** 22044 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Completed the feed parser

```
import json
import logging
import hashlib
import time
import traceback
import uuid
from contextlib import contextmanager
from datetime import timedelta
from django.conf import settings
from django.core.cache import cache
from django.db import transaction, IntegrityError
from django.utils import timezone
from django.utils.dateparse import parse_datetime, parse_date
from core import const
from core.models import Competition, CompetitionEdition, CompetitionPhase, Team, Match, Season, Player, \
    OptaFeedItem, OptaFeedItemVersion, MatchEvent, MatchPlayer, SelectionTeamPlayer
from ortec.conv import POSITION_MAP
from ortec.parser import extract_match_events, ActionCancel, ActionMatchEnd, get_player_by_person_id, \
    ActionLineUp, ActionPeriodStart
from util.events import create_amqp_event_from_match_event

logger = logging.getLogger()

MatchEndEventId = -1
HomeLineUpEventId = -200
AwayLineUpEventId = -201

LOCK_EXPIRE = 60 * 1  # Lock expires in 1 minutes

@contextmanager
def memcache_lock(lock_id, oid):
    timeout_at = time.monotonic() + LOCK_EXPIRE - 3
    # cache.add fails if the key already exists
    status = cache.add(lock_id, oid, LOCK_EXPIRE)
    try:
        yield status
    finally:
        # memcache delete is very slow, but we have to use it to take
        # advantage of using add() for atomic locking
        if time.monotonic() < timeout_at and status:
            # don't release the lock if we exceeded the timeout
            # to lessen the chance of releasing an expired lock
            # owned by someone else
            # also don't release the lock if we didn't acquire it
            cache.delete(lock_id)

def sync_competitions():
    for competition in settings.ORTEC_CLIENT.get_competitions():
        competition_record = update_or_create(
            Competition,
            import_id=competition.get("Id"),
            name=competition.get("Name"),
        )

        # for each competition query editions
        for edition in settings.ORTEC_CLIENT.get_competition_editions(competition.get("Id")):
            edition_record = update_or_create(
                CompetitionEdition,
                import_id=edition.get("Id"),
                name=edition.get("Name"),
                competition=competition_record,
            )

            # for each edition query phases
            for phase in settings.ORTEC_CLIENT.get_competition_phases(edition.get("Id")):
                update_or_create(
                    CompetitionPhase,
                    import_id=phase.get("Id"),
                    name=phase.get("Name"),
                    competition_edition=edition_record,
                )

def sync_registrations():
    phases = CompetitionPhase.objects.filter(
        enabled=True,
        competition_edition__enabled=True,
        competition_edition__competition__enabled=True,
    ).order_by("-created_at", "-import_id").all()

    for phase in phases:
        try:
            sync_phase(phase)
        except Exception:
            print("Cannot sync phase {}".format(phase.pk))
            print(traceback.format_exc())

def sync_phase(phase):
    # query registrations
    for reg in settings.ORTEC_CLIENT.get_registrations(phase.import_id):
        try:
            home_team_record = reg.get("HomeTeam")
            away_team_record = reg.get("AwayTeam")

            home_team = update_team_record(home_team_record)
            away_team = update_team_record(away_team_record)

            # parse date time
            t = parse_datetime(reg.get("DateTime"))

            match = update_or_create(
                Match,
                import_id=reg.get("Id"),
                competition=phase.competition_edition.competition,
                season=Season.current_season(),
                home_team=home_team,
                away_team=away_team,
                home_team_selection_id=home_team_record.get("Id"),
                away_team_selection_id=away_team_record.get("Id"),
                match_time=t,
            )
            match.sync_match_players()
            print("Match {} successfully synced".format(reg.get("Id")))
        except Exception:
            print("Cannot sync match {}".format(reg.get("Id")))
            print(traceback.format_exc())

def update_team_record(record):
    return update_or_create(
        Team,
        import_id=record.get("UId"),
        name=record.get("DisplayName"),
        abbr=record.get("Abbreviation"),
        # ortec_selection_id=record.get("Id"),
    )

def sync_all_teams():
    # delete all season team players before syncing
    SelectionTeamPlayer.objects.all().delete()

    home_selections = list(
        Match.objects.filter(home_team_selection_id__isnull=False).values_list("home_team_selection_id",
                                                                               flat=True).distinct())
    away_selections = list(
        Match.objects.filter(home_team_selection_id__isnull=False).values_list("away_team_selection_id",
                                                                               flat=True).distinct())
    unique_selections = home_selections + list(set(away_selections) - set(home_selections))

    for selection_id in unique_selections:
        try:
            sync_players(selection_id)
        except Exception as e:
            print('Error occurred on sync players for selection {}'.format(selection_id), e)

def sync_players(ortec_selection_id):
    if not ortec_selection_id:
        return

    for person in settings.ORTEC_CLIENT.get_selection_persons(ortec_selection_id):
        first_name = person.get("FirstName")
        last_name = person.get("SurName")
        nick_name = person.get("NickName")

        if nick_name:
            full_name = nick_name
        else:
            full_name = "{} {}".format(first_name, last_name)

        player = update_or_create(
            Player,
            import_id=person.get("Id"),
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            nick_name=nick_name,
            birth_date=parse_date(person.get("DateOfBirth")),
        )

        jersey_number = person.get("DefaultShirtNumber")
        active_selection = person.get("ActiveSelection")
        position = POSITION_MAP.get(int(person.get("DefaultPosition", 0)))

        # ignore substitute or unknown positions
        if position == const.POSITION_SUBSTITUTE or position == const.POSITION_UNKNOWN:
            continue

        # try to find season team player, if not exists, create new one
        try:
            tp = SelectionTeamPlayer.objects.filter(
                selection_id=ortec_selection_id,
                player=player,
            ).get()

            if active_selection:
                tp.jersey_number = jersey_number
                tp.position = position
                tp.save()
            else:
                tp.delete()

        except SelectionTeamPlayer.DoesNotExist:
            if active_selection:
                # create new season team player, if this doesn't exists
                SelectionTeamPlayer.objects.create(
                    selection_id=ortec_selection_id,
                    player=player,
                    jersey_number=jersey_number,
                    position=position,
                )

def sync_matches():
    # sync feed for all matches within period [now - 12 hours; now + 12 hours]
    for match in Match.objects.filter(
            match_time__gt=timezone.now() - timedelta(hours=12),
            match_time__lt=timezone.now() + timedelta(hours=12)).order_by("match_time"):

        now = timezone.now()

        # calculate sync_delay
        if (match.match_time - now) > timedelta(minutes=30):
            # 30 min before match
            sync_delay = timedelta(seconds=settings.SYNC_DELAY_BEFORE_MATCH)
        else:
            sync_delay = timedelta(seconds=settings.SYNC_DELAY_DURING_MATCH)

        if match.last_synced_at and match.last_synced_at > (now - sync_delay):
            continue

        # ignore ended matches
        if match.status == const.MATCH_STATUS_ENDED:
            continue

        # sync match feed
        try:
            sync_match(match)
        except Exception as e:
            print('Error occurred on sync match {}'.format(match.pk), e)

        match.last_synced_at = now
        match.save(update_fields=['last_synced_at'])

def sync_match(match):
    lock_id = '{0}-lock'.format(match.pk)
    with memcache_lock(lock_id, 'match-lock') as acquired:
        if acquired:
            registration_data = settings.ORTEC_CLIENT.get_registration(match.import_id)
            sync_feed(match, registration_data)

def make_lineup_item(players, team_id, event_id):
    mev = MatchEvent()
    mev.type = ActionLineUp
    mev.provider_id = str(event_id)
    mev.timestamp = timezone.now()
    mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0
    mev.payload = json.dumps({"players": players})
    mev.team_id = team_id

    return {
        "unique_id": event_id,
        "event_id": event_id,
        "version": '1',
        "match_events": [mev],
    }

def sync_feed(match, body):
    if not body.get("HomeTeam"):
        logger.error("feed do not have HomeTeam field, match {}".format(match.pk))
        return
    elif not body.get("AwayTeam"):
        logger.error("feed do not have AwayTeam field, match {}".format(match.pk))
        return

    # sync home and away team
    update_team_record(body.get("HomeTeam"))
    update_team_record(body.get("AwayTeam"))

    # sync match players, get it from line ups
    home_lineup_players = []
    away_lineup_players = []
    for lineup in body.get("LineUp"):
        player = get_player_by_person_id(lineup.get("Person"))
        selectionEditionId = lineup.get("SelectionEdition")
        position = POSITION_MAP.get(lineup.get("Position"))
        jersey_number = lineup.get("ShirtNumber")

        if not match.is_ortec_selection_from_match(selectionEditionId):
            continue

        lineup_player = {
            "id": str(player.pk),
            "jersey_number": jersey_number,
            "position": position,
        }
        if match.is_ortec_home_selection_from_match(selectionEditionId):
            home_lineup_players.append(lineup_player)
        elif match.is_ortec_away_selection_from_match(selectionEditionId):
            away_lineup_players.append(lineup_player)

        # check existence of match player, if it's not exists - create new one
        try:
            mp = MatchPlayer.objects.get(player=player, match=match)
            if not mp.from_lineups:
                mp.from_lineups = True
                mp.save()

        except MatchPlayer.DoesNotExist:
            match_player_team = None
            if match.is_ortec_home_selection_from_match(selectionEditionId):
                match_player_team = match.home_team
            elif match.is_ortec_away_selection_from_match(selectionEditionId):
                match_player_team = match.away_team

            if match_player_team:
                try:
                    MatchPlayer.objects.create(
                        match=match,
                        player=player,
                        team=match_player_team,
                        position=position,
                        jersey_number=jersey_number,
                        from_lineups=True
                    )
                except IntegrityError:
                    pass

    # consider each event as item
    items = []

    if len(home_lineup_players) > 0:
        items.append(make_lineup_item(home_lineup_players, match.home_team_id, HomeLineUpEventId))
    if len(away_lineup_players) > 0:
        items.append(make_lineup_item(away_lineup_players, match.away_team_id, AwayLineUpEventId))

    current_period = 1
    for item in body.get("Events"):
        # parse events
        match_events = extract_match_events(match, current_period, item)

        # modify current period based on ActionPeriodStart event
        for ev in match_events:
            if ev.type == ActionPeriodStart:
                # get payload and try to understand this period just started
                if ev.payload:
                    payload = json.loads(ev.payload)
                    if payload and payload.get("periodId"):
                        current_period = payload.get("periodId")

        # make consistent hash of item
        if match.import_id == '121829':
            version_hash = hashlib.sha1(json.dumps(item, sort_keys=True).encode('utf8')).hexdigest()
        else:
            version_hash = calculate_hash(item)

        items.append({
            "unique_id": item.get("Id"),
            "event_id": item.get("Id"),
            "version": version_hash,
            "match_events": match_events,
        })

    if body.get("AnalysisFinished"):
        mev = MatchEvent()
        mev.type = ActionMatchEnd
        mev.provider_id = str(MatchEndEventId)
        mev.timestamp = timezone.now()
        mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0

        # insert match ended event
        items.append({
            "unique_id": MatchEndEventId,
            "event_id": MatchEndEventId,
            "version": '1',
            "match_events": [mev],
        })

    with transaction.atomic():
        # process items inside transaction
        process_items(match, items)

def process_items(match, incoming_events):
    # first of all select all existing items
    existing_items = OptaFeedItem.objects.select_related('current_version').filter(match=match)

    new_match_events = []
    updated_item_count = 0
    new_item_count = 0

    found_in_incoming = set()

    # handle updated items
    for event in incoming_events:
        existing_item_to_process = None

        # find existing one
        for existing in existing_items:
            if existing.unique_id == event.get("unique_id") and existing.event_id == event.get("event_id"):
                # new version for item
                if existing.current_version.version != event.get("version"):
                    existing_item_to_process = existing
                break

        # no changes
        if not existing_item_to_process:
            continue

        # select existing match events for opta_feed_item excluding cancel events
        existing_match_items = MatchEvent.objects.filter(
            opta_feed_item_version=existing_item_to_process.current_version)

        to_create, to_delete, non_changed = get_diff_actions(existing_match_items, event.get("match_events"))

        # calculate status for item
        if len(to_create) == 0 and len(to_delete) == 0:
            new_status = OptaFeedItemVersion.NO_DIFF
        elif len(to_delete) == len(existing_match_items):
            new_status = OptaFeedItemVersion.FULL_CANCEL
        else:
            new_status = OptaFeedItemVersion.PARTIAL_CANCEL

        # update status of item
        existing_item_to_process.current_version.status = new_status
        existing_item_to_process.current_version.save(update_fields=['status'])

        # create new item version
        new_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=event.get("version"),
            last_modified_at=timezone.now(),
            item=existing_item_to_process,
        )

        # update reference from item to version
        existing_item_to_process.current_version = new_version
        existing_item_to_process.save(update_fields=['current_version'])

        # generate cancel event actions as part of new version
        for delete_mev in to_delete:
            new_match_events.append(generate_cancel_match_event(delete_mev, new_version))

        for mev in to_create:
            mev.opta_feed_item_version = new_version
            new_match_events.append(mev)

        # change link to new version
        for mev in non_changed:
            mev.opta_feed_item_version = new_version
            mev.save(update_fields=['opta_feed_item_version'])

        updated_item_count += 1

    # handle new items
    for event in incoming_events:
        unique_id = event.get("unique_id")
        event_id = event.get("event_id")
        version = event.get("version")

        found = False
        # find existing one
        for existing in existing_items:
            if existing.unique_id == unique_id and existing.event_id == event_id:
                found_in_incoming.add(existing.pk)
                found = True
                break

        if found:
            continue

        # insert feed item
        feed_item = OptaFeedItem.objects.create(
            unique_id=unique_id,
            event_id=event_id,
            match=match,
        )

        # insert version
        feed_item_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=version,
            last_modified_at=timezone.now(),
            item=feed_item,
        )

        # update feed link
        feed_item.current_version = feed_item_version
        feed_item.save(update_fields=['current_version'])

        for mev in event.get("match_events"):
            mev.opta_feed_item_version = feed_item_version
            new_match_events.append(mev)

        new_item_count += 1

    # delete items that not found in incoming feed
    deleted_item_count = 0
    deleted_events_count = 0

    for item in existing_items:
        if item.pk in found_in_incoming:
            continue

        # get all match events for current_version
        active_match_events = MatchEvent.objects.filter(
            opta_feed_item_version=item.current_version_id,
            status=MatchEvent.ACTIVE,
        ).exclude(type=ActionCancel).all()

        if len(active_match_events) == 0:
            # no match_event to delete, it means this event was already cancelled
            continue

        # update status of item
        item.current_version.status = OptaFeedItemVersion.FULL_CANCEL
        item.current_version.save(update_fields=['status'])

        # create new item version
        new_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            # random uuid as new version
            version=uuid.uuid4(),
            last_modified_at=timezone.now(),
            item=item,
        )

        # update reference from item to version
        item.current_version = new_version
        item.save(update_fields=['current_version'])

        for delete_mev in active_match_events:
            new_match_events.append(generate_cancel_match_event(delete_mev, new_version))
            deleted_events_count += 1

        deleted_item_count += 1

    print("updated item count", updated_item_count)
    print("new item count", new_item_count)
    print("deleted item count", deleted_item_count)
    print("deleted event count", deleted_events_count)

    # calc next match event_id
    next_match_event_id = MatchEvent.objects.filter(match=match).count() + 1

    # insert match events
    print("new_events len is", len(new_match_events))
    for match_event in new_match_events:
        # empty pk to make sure we're creating new records
        match_event.pk = None
        match_event.match = match
        match_event.match_event_id = next_match_event_id
        match_event.save()

        next_match_event_id += 1

        # insert amqp event as well
        create_amqp_event_from_match_event(match_event)

def generate_cancel_match_event(delete_mev, new_version):
    mev = MatchEvent()
    mev.type = ActionCancel
    mev.payload = json.dumps({
        "id": delete_mev.id,
    })
    mev.minute = 0
    mev.second = 0
    mev.opta_feed_item_version = new_version
    mev.timestamp = timezone.now()

    return mev

def get_diff_actions(prev, next):
    # make copy of prev, cause it will be modified
    prev = list(prev)

    to_create = []
    non_changed = []

    for next_event in next:
        # find even in prev
        foundIdx = -1

        for idx, prev_event in enumerate(prev):
            # same event found
            if is_equal(prev_event, next_event):
                foundIdx = idx
                break

        if foundIdx != -1:
            non_changed.append(prev[foundIdx])
            del prev[foundIdx]
        else:
            to_create.append(next_event)

    # all events that are left in prev should be deleted
    to_delete = prev

    return to_create, to_delete, non_changed

def is_equal(a, b):
    # return False
    # #a.get("player_id") == b.get("player_id") and \
    #            #a.get("team_id") == b.get("team_id") and \
    return a.type == b.type and \
           a.points == b.points and \
           a.payload == b.payload

def update_or_create(cls, **kwargs):
    # find pk
    import_id = kwargs.get("import_id")
    with transaction.atomic():
        try:
            obj = cls.objects.select_for_update().get(import_id=import_id)

            changed = False
            for k, v in kwargs.items():
                # check for any change
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    changed = True

            # call save only if there was any changes
            if changed:
                obj.save()

            return obj

        except cls.DoesNotExist:
            return cls.objects.create(**kwargs)

def calculate_hash(ev):
    annotations = ev.get('Annotations', [])
    parts = [
        ev.get('DateTime', '')
    ]
    for an in annotations:
        parts.append(calculate_hash_for_annotation(an))
    return '#'.join(parts)

def calculate_hash_for_annotation(ev):
    parts = [
        ev.get('Id', ''),
        ev.get('PersonId', ''),
        ev.get('NextPersonId', ''),
        ev.get('SelectionEditionId', ''),
        ev.get('NextSelectionEdition', ''),
        ev.get('Label', ''),
        ','.join([str(el) for el in ev.get('Properties', [])]),
    ]
    return ';'.join([str(p) for p in parts])

```

## File: `playersabi.json`
- **File Size:** 12607 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** change the setup for assigned player

```
[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "AddressEmptyCode",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "ERC1967InvalidImplementation",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "ERC1967NonPayable",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "ERC721IncorrectOwner",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ERC721InsufficientApproval",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "approver",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidApprover",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidOperator",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidOwner",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "receiver",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidReceiver",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "sender",
        "type": "address"
      }
    ],
    "name": "ERC721InvalidSender",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ERC721NonexistentToken",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "FailedInnerCall",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "InvalidInitialization",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "NotInitializing",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "OwnableInvalidOwner",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "OwnableUnauthorizedAccount",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "UUPSUnauthorizedCallContext",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "slot",
        "type": "bytes32"
      }
    ],
    "name": "UUPSUnsupportedProxiableUUID",
    "type": "error"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "approved",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "approved",
        "type": "bool"
      }
    ],
    "name": "ApprovalForAll",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint64",
        "name": "version",
        "type": "uint64"
      }
    ],
    "name": "Initialized",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "Upgraded",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "UPGRADE_INTERFACE_VERSION",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256[]",
        "name": "tokenIds",
        "type": "uint256[]"
      }
    ],
    "name": "batchMint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "getApproved",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "initialOwner",
        "type": "address"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      }
    ],
    "name": "isApprovedForAll",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ownerOf",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "proxiableUUID",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "renounceOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "safeMint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "safeTransferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "safeTransferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "operator",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "approved",
        "type": "bool"
      }
    ],
    "name": "setApprovalForAll",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "interfaceId",
        "type": "bytes4"
      }
    ],
    "name": "supportsInterface",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "tokenURI",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "transferOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newImplementation",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "upgradeToAndCall",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
]

```

## File: `rabbit/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```

```

## File: `rabbit/apps.py`
- **File Size:** 81 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
from django.apps import AppConfig

class Rabbit(AppConfig):
    name = 'rabbit'

```

## File: `rabbit/migrations/0001_create_events_table.py`
- **File Size:** 1122 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 05:45
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AMQPEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('send_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Pending'), (2, 'Complete')], default=1)),
                ('exchange', models.CharField(max_length=32)),
                ('event_type', models.CharField(db_column='type', max_length=32)),
                ('data', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'amqp_events',
            },
        ),
    ]

```

## File: `rabbit/migrations/0002_create_event_index.py`
- **File Size:** 521 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 05:45
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('rabbit', '0001_create_events_table'),
    ]

    atomic = False
    operations = [
        migrations.RunSQL("""create index concurrently idx_amqp_events_pending on amqp_events(id) where status = 1;""",
                          reverse_sql="""drop index concurrently idx_amqp_events_pending;"""),
    ]

```

## File: `rabbit/migrations/0003_create_trigger_func.py`
- **File Size:** 638 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 05:56
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0002_create_event_index'),
    ]

    atomic = False
    operations = [
        migrations.RunSQL("""CREATE OR REPLACE FUNCTION notify_amqp_event() RETURNS TRIGGER AS $$
    BEGIN
        IF TG_OP = 'INSERT' THEN
            PERFORM pg_notify('amqp_events', (NEW.id)::varchar);
        END IF;

        RETURN NEW;
    END; $$ LANGUAGE plpgsql;""", reverse_sql="""DROP FUNCTION notify_amqp_event();"""),
    ]

```

## File: `rabbit/migrations/0004_create_trigger.py`
- **File Size:** 541 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 05:56
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0003_create_trigger_func'),
    ]

    atomic = False
    operations = [
        migrations.RunSQL(""" CREATE TRIGGER trg_notify_amqp_event
      after insert on amqp_events for each row
      EXECUTE PROCEDURE notify_amqp_event();""", reverse_sql="""DROP TRIGGER trg_notify_amqp_event ON amqp_events;"""),
    ]

```

## File: `rabbit/migrations/0005_auto_20190314_1318.py`
- **File Size:** 853 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-03-14 13:18
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('rabbit', '0004_create_trigger'),
    ]

    atomic = False
    operations = [
        migrations.RunSQL(
            """drop index concurrently idx_amqp_events_pending;""",
            reverse_sql="""create index concurrently idx_amqp_events_pending on amqp_events(id) where status = 1;""",
        ),
        migrations.RemoveField(
            model_name='amqpevent',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='amqpevent',
            name='send_date',
        ),
        migrations.RemoveField(
            model_name='amqpevent',
            name='status',
        ),

    ]

```

## File: `rabbit/migrations/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```

```

## File: `rabbit/models.py`
- **File Size:** 450 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** new changes

```
from django.db import models

class AMQPEvent(models.Model):
    exchange = models.CharField(max_length=32, null=False, blank=False)
    event_type = models.CharField(max_length=32, null=False, blank=False, db_column='type')
    data = models.TextField(null=False, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'amqp_events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

```

## File: `requirements.txt`
- **File Size:** 480 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add mixpanel to notifiactions on the admin

```
urllib3==1.26.6
importlib-metadata==4.8.3
Django==2.2
django-rest-framework==0.1.0
djangorestframework==3.9.1
gunicorn==19.9.0
psycopg2==2.8.6
PyJWT==1.7.1
pytz==2020.1
websockets_proxy==0.1.2

Pillow==8.0
django-statsd-mozilla==0.4.0
celery==4.4.7
django-celery-beat==2.0.0
web3==6.20.0
boto3==1.34
requests~=2.31.0
python-dateutil~=2.8.2
websockets==11.0.3
cachetools~=5.3.3
django-admin-csvexport==2.2
ortools~=9.10.4067
protobuf>=5.26.1
firebase-admin>=2.16.0
mixpanel>=4.10.1
```

## File: `revenue_cat/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `revenue_cat/api.py`
- **File Size:** 882 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
import logging
import requests
from cachetools import TTLCache

logger = logging.getLogger()

class RevenueCatAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def _build_url(path):
        return 'https://api.revenuecat.com{}'.format(path)

    def get_subscriber(self, user_id):
        return self._process_request('/v1/subscribers/{}'.format(user_id))

    def _process_request(self, path, data=None):
        final_url = self._build_url(path)
        logger.info("Making request to {}".format(final_url))

        res = requests.get(final_url, data, headers={
            'Authorization': 'Bearer {}'.format(self.api_key)
        })

        if res.status_code != 200:
            raise Exception(
                'Received invalid status code {} for {}: {}'.format(res.status_code, final_url, res.content))
        return res.json()

```

## File: `revenue_cat/sync.py`
- **File Size:** 5620 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Assist correct parsing (#138)

```
import json

from django.conf import settings
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from core import const
from core.models import Subscription, SubscriptionRequest, CustomUser

def process_subscription_requests():
    for req in SubscriptionRequest.objects.all()[:100]:
        print('Syncing subscription {}'.format(req.user_id))
        sync_subscription(req.user_id, req.app_user)
        # delete request after syncing
        req.delete()

def expire_subscriptions():
    # check subscription that are active, but expiration time is less than current time
    for sub in Subscription.objects.filter(active=True, expiration_time__lt=timezone.now()).all():
        # find user that has this subscription
        for usr in CustomUser.objects.filter(subscription=sub).all():
            try:
                sync_subscription(sub.user_id, usr)
            except CustomUser.DoesNotExist:
                print('Not found user for subscription {}: user_id = {}'.format(sub.pk, sub.user_id))

def sync_subscription(user_id, app_user):
    subscription = sync_subscription_with_revenue_cat(user_id)

    # update premium flag of user
    if app_user:
        with transaction.atomic():
            locked_user = CustomUser.objects.select_for_update().get(pk=app_user.pk)
            # remove that subscription from all other users
            for user in CustomUser.objects.filter(subscription=subscription).exclude(pk=app_user.pk).all():
                user.subscription = None
                user.update_premium()
            locked_user.subscription = subscription
            locked_user.save(update_fields=['subscription', 'updated_at'])
            locked_user.update_premium()

def sync_subscription_with_revenue_cat(user_id):
    res = settings.REVENUE_CAT_CLIENT.get_subscriber(user_id)
    last_billing_update = find_last_billing_update(res)
    expiration_time, subscriptier_tier = find_expiration_and_tier(res)
    raw_data = json.dumps(res.get("subscriber", {}), sort_keys=True)
    is_active = expiration_time > timezone.now()

    # try to find subscription in database
    try:
        s = Subscription.objects.get(user_id=user_id)

        # update subscription if any of meaningful fields are changed
        if s.raw_data != raw_data or \
                s.last_billing_update != last_billing_update or \
                s.expiration_time != expiration_time or \
                s.active != is_active or \
                s.tier != subscriptier_tier:
            s.last_billing_update = last_billing_update
            s.expiration_time = expiration_time
            s.raw_data = raw_data
            s.active = is_active
            s.tier = subscriptier_tier
            s.save()

        return s

    except Subscription.DoesNotExist:
        # create new one
        return Subscription.objects.create(
            user_id=user_id,
            expiration_time=expiration_time,
            raw_data=raw_data,
            last_billing_update=last_billing_update,
            active=is_active,
            tier=subscriptier_tier,
        )

def check_is_active(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    for k, v in subscriber_info.get("subscriber", {}).get("entitlements", {}).items():
        dat = parse_date(v.get("expires_date"))
        if dat > timezone.now():
            return True

    return False

def find_expiration_time(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    dates = []
    for k, v in subscriber_info.get("subscriber", {}).get("subscriptions", {}).items():
        expires_date = parse_date(v.get("expires_date"))
        if expires_date:
            dates.append(expires_date)

    return max(dates) if len(dates) > 0 else None

def find_expiration_and_tier(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    max_expires_date = None
    tier = const.TIER_NONE

    for k, v in subscriber_info.get("subscriber", {}).get("entitlements", {}).items():
        expires_date = parse_date(v.get("expires_date"))

        if max_expires_date is None or max_expires_date < expires_date:
            max_expires_date = expires_date
            if k == "lite":
                tier = const.TIER_LITE
            elif k == "premium":
                tier = const.TIER_PREMIUM

    return max_expires_date, tier

def find_last_billing_update(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    # build array of possible candidates for last billing update
    dates = []

    def add_date(dat):
        parsed_date = parse_date(dat)
        if parsed_date:
            dates.append(parsed_date)

    s = subscriber_info.get("subscriber", {})
    entitlements = s.get("entitlements", {})

    for k, v in entitlements.items():
        add_date(v.get("expires_date"))
        add_date(v.get("purchase_date"))
        add_date(v.get("grace_period_expires_date"))

    subscriptions = subscriber_info.get("subscriptions", {})

    for k, v in subscriptions.items():
        add_date(v.get("expires_date"))
        add_date(v.get("original_purchase_date"))
        add_date(v.get("purchase_date"))
        add_date(v.get("grace_period_expires_date"))
        add_date(v.get("billing_issues_detected_at"))
        add_date(v.get("unsubscribe_detected_at"))

    return max(dates) if len(dates) > 0 else None

def parse_date(dat):
    if not dat:
        return None

    # try to parse date
    return parse_datetime(dat)

```

## File: `scripts/dev.sh`
- **File Size:** 307 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** debugging goal_finder

```
set -o allexport; source .env; \
# python manage.py makemigrations
# python manage.py migrate; \
gunicorn --reload -b :8082 mobile_api.wsgi --timeout 240; \
# celery -A mobile_api worker -l info
# celery -A mobile_api beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
set +o allexport
```

## File: `scripts/makemigrations.sh`
- **File Size:** 87 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add correct RMQ_USER env var corrected scripts for dev and migrations gitignore for venv (virtualenv) for python local instalations

```
set -o allexport; source .env; \
python manage.py makemigrations $1; \
set +o allexport
```

## File: `scripts/migrate.sh`
- **File Size:** 80 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add correct RMQ_USER env var corrected scripts for dev and migrations gitignore for venv (virtualenv) for python local instalations

```
set -o allexport; source .env; \
python manage.py migrate $1; \
set +o allexport
```

## File: `soccer_wiki/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `soccer_wiki/apps.py`
- **File Size:** 96 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.apps import AppConfig

class SoccerWikiConfig(AppConfig):
    name = 'soccer_wiki'

```

## File: `soccer_wiki/migrations/0001_initial.py`
- **File Size:** 1149 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-02 21:04

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoccerWikiPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.IntegerField(unique=True)),
                ('first_name', models.TextField(null=True)),
                ('second_name', models.TextField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('image', models.TextField(null=True)),
                ('internal_image_status', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Success'), (3, 'Error')], default=1)),
                ('internal_image_url', models.TextField(null=True)),
            ],
            options={
                'db_table': 'soccer_wiki_players',
            },
        ),
    ]

```

## File: `soccer_wiki/migrations/0002_auto_20190404_1225.py`
- **File Size:** 404 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
# Generated by Django 2.1.7 on 2019-04-04 12:25

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('soccer_wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soccerwikiplayer',
            name='birth_date',
            field=models.DateField(db_index=True, null=True),
        ),
    ]

```

## File: `soccer_wiki/migrations/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `soccer_wiki/models.py`
- **File Size:** 909 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.db import models

class SoccerWikiPlayer(models.Model):
    STATUS_UNKNOWN = 1
    STATUS_SUCCESS = 2
    STATUS_ERROR = 3

    STATUSES = (
        (STATUS_UNKNOWN, 'Unknown'),
        (STATUS_SUCCESS, 'Success'),
        (STATUS_ERROR, 'Error'),
    )

    import_id = models.IntegerField(unique=True)
    first_name = models.TextField(null=True)
    second_name = models.TextField(null=True)
    birth_date = models.DateField(null=True, db_index=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    image = models.TextField(null=True)
    internal_image_status = models.IntegerField(choices=STATUSES, default=STATUS_UNKNOWN)
    internal_image_url = models.TextField(null=True)

    def __str__(self):
        return "[{}] - {} {}".format(self.import_id, self.first_name, self.second_name)

    class Meta:
        db_table = 'soccer_wiki_players'

```

## File: `soccer_wiki/sync.py`
- **File Size:** 6035 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix boto upload

```
import logging
import pathlib
import uuid
import json
from datetime import datetime
from multiprocessing.pool import ThreadPool

import requests
from django.conf import settings
from django.db import transaction

from soccer_wiki.models import SoccerWikiPlayer
from util import gce

logger = logging.getLogger("soccerwiki")

def sync_players():
    print('sync_players')
    logger.info('downloading players from soccerwiki')
    r = requests.get(
        "https://en.soccerwiki.org/download-data.php?format=1&options%5B%5D=PlayerData&countryId=&submit=Download+Data")
    if r.status_code == 200:
        sync_players_from_json(r.json())

def sync_players_from_json(data):
    player_data = data.get('PlayerData', [])
    count = 0
    logger.info('syncing {} players'.format(len(player_data)))
    print('syncing {} players'.format(len(player_data)))
    for el in player_data:
        try:
            player_id = int(el.get("ID", "0"))
            first_name = el.get("Forename", "")
            second_name = el.get("Surname", "")
            birth_date = el.get("Birthdate", "")  # Assuming Birthdate field exists, correct if different
            height = int(el.get("Height", "0"))         # Assuming Height field exists, correct if different
            weight = int(el.get("Weight", "0"))         # Assuming Weight field exists, correct if different
            image = el.get("ImageURL", "")
        except ValueError:
            logger.error("Invalid data encountered for player with raw ID: {}".format(el.get("ID", "")))
            print("Invalid data encountered for player with raw ID: {}".format(el.get("ID", "")))
            continue

        try:
            birth_date_parsed = datetime.strptime(birth_date, "%Y-%m-%d") if birth_date else None
        except Exception:
            birth_date_parsed = None

        try:
            player = SoccerWikiPlayer.objects.get(import_id=player_id)
            update_fields = []
            if first_name != player.first_name:
                update_fields.append('first_name')
                player.first_name = first_name

            if second_name != player.second_name:
                update_fields.append('second_name')
                player.second_name = second_name

            if birth_date_parsed != player.birth_date:
                update_fields.append('birth_date')
                player.birth_date = birth_date_parsed

            if height != player.height:
                update_fields.append('height')
                player.height = height

            if weight != player.weight:
                update_fields.append('weight')
                player.weight = weight

            if image != player.image:
                update_fields += ['image', 'internal_image_status', 'internal_image_url']
                player.image = image
                player.internal_image_status = SoccerWikiPlayer.STATUS_UNKNOWN
                player.internal_image_url = image

            if len(update_fields) > 0:
                player.save(update_fields=update_fields)

        except SoccerWikiPlayer.DoesNotExist:
            SoccerWikiPlayer.objects.create(
                import_id=player_id,
                first_name=first_name,
                second_name=second_name,
                birth_date=birth_date_parsed,
                height=height,
                weight=weight,
                image=image,
            )

        count += 1

        if count % 1000 == 0:
            logger.info('processed {} out of {}'.format(count, len(player_data)))
    logger.info('synced {} players'.format(count))
    print('synced {} players'.format(count))
    return count
def process_soccer_wiki_player(player_id):
    bucket = settings.GCE_PLAYER_IMAGES_BUCKET

    # lock for processing
    with transaction.atomic():
        player = SoccerWikiPlayer.objects.select_for_update().get(pk=player_id)

        if player.internal_image_status != SoccerWikiPlayer.STATUS_UNKNOWN:
            return

        if not player.image:
            player.internal_image_status = SoccerWikiPlayer.STATUS_ERROR
            player.save(update_fields=['internal_image_status'])
            return

        # download image
        try:
            image_url = player.image
            res = requests.get(image_url, timeout=(3, 20))

            if res.status_code != 200:
                logger.info('cannot get image {}: {}'.format(image_url, res.status_code))
                player.internal_image_status = 4
                player.save(update_fields=['internal_image_status'])
                return
        except Exception:
            logger.error('cannot get image {}'.format(player.image))
            player.internal_image_status = 4
            player.save(update_fields=['internal_image_status'])
            return

        # get extension of file
        extension = pathlib.Path(player.image).suffix

        # upload image to gce
        new_filename = str(uuid.uuid4()) + extension

        try:
            new_image_url = gce.upload_file(bucket, new_filename, res.content, res.headers['content-type'])
            player.internal_image_status = SoccerWikiPlayer.STATUS_SUCCESS
            player.internal_image_url = new_image_url
            player.save(update_fields=['internal_image_status', 'internal_image_url'])
        except Exception:
            logger.exception("cannot upload image to gce")
            player.internal_image_status = 5
            player.save(update_fields=['internal_image_status'])

    logger.info("{} processed".format(player_id))
    print("{} processed".format(player_id))

def upload_soccer_wiki_photos():
    logger.info('uploading soccer wiki photos')
    print('uploading soccer wiki photos')
    player_ids = SoccerWikiPlayer.objects. \
        filter(internal_image_status=SoccerWikiPlayer.STATUS_UNKNOWN).values_list("id", flat=True)

    pool = ThreadPool(10)
    pool.map(process_soccer_wiki_player, player_ids)
    logger.info('uploaded {} photos'.format(len(player_ids)))
    return len(player_ids)

```

## File: `soccer_wiki/tests.py`
- **File Size:** 60 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.test import TestCase

# Create your tests here.

```

## File: `soccer_wiki/views.py`
- **File Size:** 63 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from django.shortcuts import render

# Create your views here.

```

## File: `util/__init__.py`
- **File Size:** 0 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```

```

## File: `util/calc.py`
- **File Size:** 346 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
def get_rank_dict(values):
    values = sorted(values, reverse=True)

    val_dict = dict()
    position, real_position = 0, 0
    prev_score = None
    for val in values:
        real_position += 1
        if prev_score != val:
            position = real_position
        prev_score = val

        val_dict[val] = position

    return val_dict

```

## File: `util/drf.py`
- **File Size:** 309 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

class AuthAPIView(APIView):
    permission_classes = (IsAuthenticated,)

class AuthGenericViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)

```

## File: `util/events.py`
- **File Size:** 852 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** add comprehensive logging level and format for our service

```
from rabbit.models import AMQPEvent
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from core.models import EventThrottler
from core.serializers import MatchEventSerializer

def create_amqp_event(exchange, event_type, data):
    if settings.AMQP_THROTTLING_ENABLED:
        EventThrottler.objects.create(
            exchange=exchange,
            event_type=event_type,
            data=JSONRenderer().render(data).decode("utf-8"),
        )
    else:
        AMQPEvent.objects.create(
            exchange=exchange,
            event_type=event_type,
            data=JSONRenderer().render(data).decode("utf-8"),
        )

def create_amqp_event_from_match_event(match_event):
    create_amqp_event(
        settings.AMQP_MATCH_EVENTS_EXCHANGE,
        "new",
        MatchEventSerializer(match_event).data,
    )

```

## File: `util/gce.py`
- **File Size:** 572 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** fix boto upload

```
import boto3

from django.conf import settings

def upload_file(bucket, name, data, content_type):
    s3 = boto3.resource(
        's3',
        region_name='ams3',
        endpoint_url='https://ams3.digitaloceanspaces.com',
        aws_access_key_id=settings.DO_SPACE_API_KEY,
        aws_secret_access_key=settings.DO_SPACE_API_SECRET,
    )
    s3.Object(bucket, name).put(Body=data, ACL='public-read', ContentType=content_type)
    return get_file_url(bucket, name)

def get_file_url(bucket, name):
    return f"https://{bucket}.ams3.digitaloceanspaces.com/{name}"

```

## File: `util/json.py`
- **File Size:** 404 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
import json

from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)

        return super().default(o)

def model_to_json(instance):
    return json.dumps(instance, cls=ExtendedEncoder)

```

## File: `util/middlewares.py`
- **File Size:** 5903 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
import inspect
import logging
import time
import os as os_fn

from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin
from django_statsd.clients import statsd
from django_statsd.middleware import is_authenticated

logger = logging.getLogger("healthz")

class HealthCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.method == "GET":
            if request.path == "/readiness":
                return self.readiness(request)
            elif request.path == "/healthz":
                return self.healthz(request)
        return self.get_response(request)

    def healthz(self, request):
        """
        Returns that the server is alive.
        """
        return HttpResponse("OK")

    def readiness(self, request):
        # # Connect to each database and do a generic standard SQL query
        # # that doesn't write any data and doesn't depend on any tables
        # # being present.
        # try:
        #     from django.db import connections
        #     for name in connections:
        #         cursor = connections[name].cursor()
        #         cursor.execute("SELECT 1;")
        #         row = cursor.fetchone()
        #         if row is None:
        #             return HttpResponseServerError("db: invalid response")
        # except Exception as e:
        #     logger.exception(e)
        #     return HttpResponseServerError("db: cannot connect to database.")
        #
        # # Call get_stats() to connect to each memcached instance and get it's stats.
        # # This can effectively check if each is online.
        # try:
        #     from django.core.cache import caches
        #     from django.core.cache.backends.memcached import BaseMemcachedCache
        #     for cache in caches.all():
        #         if isinstance(cache, BaseMemcachedCache):
        #             stats = cache._cache.get_stats()
        #             if len(stats) != len(cache._servers):
        #                 return HttpResponseServerError("cache: cannot connect to cache.")
        # except Exception as e:
        #     logger.exception(e)
        #     return HttpResponseServerError("cache: cannot connect to cache.")

        return HttpResponse("OK")

class MetricMiddleware(MiddlewareMixin):
    """statsd's timing data per view."""

    def process_view(self, request, view_func, view_args, view_kwargs):
        view = view_func
        if not inspect.isfunction(view_func):
            view = view.__class__
        try:
            view_name = view.__name__
            # for class based view try to find real function name under class
            if hasattr(view_func, 'actions'):
                func_name = view_func.actions.get(request.method.lower(), None)
                if func_name is not None:
                    view_name = '%s.%s' % (view_name, func_name)

            request._view_module = view.__module__
            request._view_name = view_name
            request._start_time = time.time()
        except AttributeError:
            pass

    def process_response(self, request, response):
        self._record_metrics(request, response.status_code)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            status_code = 404
        else:
            status_code = 500
        self._record_metrics(request, status_code)

    @staticmethod
    def metric_name(tpl, **kwargs):
        # add `env` and `os` tags to template and format
        return (tpl + ',env={env},os={os},lang=python').format(**kwargs)

    def _record_metrics(self, request, status_code):
        os = '-'
        if hasattr(request, 'ios_agent') and request.ios_agent:
            os = 'ios'
        elif hasattr(request, 'android_agent') and request.android_agent:
            os = 'android'
        code_group = int(status_code / 100)
        data = dict(status_code=status_code, code_group=code_group,
                    env=os_fn.getenv('DJANGO_SETTINGS_MODULE'), os=os, )

        # log exact status code (e.g. 200, 400)
        statsd.incr(self.metric_name('response.{status_code}', **data))
        # log group of response (e.g. 2xx, 4xx)
        statsd.incr(self.metric_name('response.{code_group}xx', **data))
        if hasattr(request, 'user') and is_authenticated(request.user):
            statsd.incr(self.metric_name('response.auth.{status_code}', **data))

        if hasattr(request, '_start_time'):
            data.update(
                module=request._view_module,
                name=request._view_name,
                method=request.method,
            )
            ms = int((time.time() - request._start_time) * 1000)

            statsd.timing(self.metric_name('response.timing', **data), ms)
            statsd.timing(self.metric_name('response.{status_code}.timing', **data), ms)
            statsd.timing(self.metric_name('response.{code_group}xx.timing', **data), ms)
            statsd.timing(self.metric_name('view.{module}.{name}.{method}.timing', **data), ms)
            statsd.incr(self.metric_name('view.{module}.{name}.{method}.count', **data))
            statsd.incr(self.metric_name('view.{module}.{name}.{method}.{status_code}.count', **data))

            # cache hit/miss data
            if hasattr(request, '_cache_hit'):
                statsd.incr(self.metric_name('view.{module}.{name}.{method}.cache_count', **data))
                statsd.incr(self.metric_name('response.cache_count', **data))
            else:
                statsd.incr(self.metric_name('view.{module}.{name}.{method}.non_cache_count', **data))
                statsd.incr(self.metric_name('response.non_cache_count', **data))

```

## File: `util/parse.py`
- **File Size:** 311 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** debug delays in opta events enhancements for logging

```
from datetime import datetime

def parse_event_timestamp(event, field = "timeStamp"):
    return datetime.fromisoformat(event[field].replace('Z', '+00:00'))

def parse_event_id(event, field = "eventId", type = "int"):
    if type == "int":
        return int( event[field])
    else:
        return event[field]
```

## File: `util/sort.py`
- **File Size:** 504 bytes
- **Last Modified:** Tue Apr 22 2025 10:27:57 GMT-0500 (Peru Standard Time)
- **Last Commit:** Implement bug fix for issue #123

```
from core import const

def sort_players(players):
    return sorted(players,
                  key=lambda x: (get_position_sort(x.position), x.jersey_number if x.jersey_number else 999))

def get_position_sort(position):
    if position == const.POSITION_GOALKEEPER:
        return 1
    elif position == const.POSITION_DEFENDER:
        return 2
    elif position == const.POSITION_MIDFIELDER:
        return 3
    elif position == const.POSITION_FORWARD:
        return 4
    else:
        return 5

```
